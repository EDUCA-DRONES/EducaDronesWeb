document.addEventListener("DOMContentLoaded", async function () {
const elemento = document.getElementById("impact-map");
const status = document.getElementById("impact-map-status");

if (!elemento || typeof L === "undefined") {
    if (status) status.textContent = "Não foi possível carregar o mapa.";
    return;
}

const mapa = L.map(elemento, {
    scrollWheelZoom: false
}).setView([-14.2, -51.9], 4);

L.tileLayer("https://tile.openstreetmap.de/{z}/{x}/{y}.png", {
attribution: '&copy; OpenStreetMap contributors',
maxZoom: 19
}).addTo(mapa);

try {
    const resposta = await fetch("/visitas/api/mapa-impacto/");

    if (!resposta.ok) {
    throw new Error("Falha ao buscar os dados.");
    }

    const dados = await resposta.json();

    document.getElementById("impact-total-pessoas").textContent =
    Number(dados.total_pessoas || 0).toLocaleString("pt-BR");

    document.getElementById("impact-total-cidades").textContent =
    Number(dados.total_cidades || 0).toLocaleString("pt-BR");

    const locais = dados.locais || [];

    if (locais.length === 0) {
    status.textContent =
        "Ainda não há cidades com coordenadas cadastradas para exibir.";
    return;
    }

    const maiorTotal = Math.max(...locais.map(local => local.total));

    const pontosCalor = locais.map(local => [
    local.latitude,
    local.longitude,
    Math.max(0.15, local.total / maiorTotal)
    ]);

    if (typeof L.heatLayer === "function") {
    L.heatLayer(pontosCalor, {
        radius: 35,
        blur: 25,
        maxZoom: 8
    }).addTo(mapa);
    }

    locais.forEach(local => {
    L.circleMarker([local.latitude, local.longitude], {
        radius: Math.min(16, 5 + Math.sqrt(local.total)),
        color: "#1264a3",
        fillColor: "#1264a3",
        fillOpacity: 0.75,
        weight: 1
    })
        .bindPopup(
        `<strong>${local.cidade}/${local.estado}</strong><br>` +
        `${Number(local.total).toLocaleString("pt-BR")} pessoa(s) registrada(s)`
        )
        .addTo(mapa);
    });

    status.textContent = "Selecione um ponto para consultar os dados da cidade.";
} catch (erro) {
    status.textContent =
    "Não foi possível carregar os dados. Verifique a conexão e tente novamente.";
}
});
