    const selectEstado = document.getElementById('id_estado');
    const selectCidade = document.getElementById('id_cidade');

    async function carregarCidades() {
        const uf = selectEstado.value;

        if (!uf) {
            selectCidade.innerHTML = '<option value="">Selecione primeiro o estado</option>';
            selectCidade.disabled = true;
            return;
        }

        selectCidade.innerHTML = '<option value="">Carregando cidades...</option>';
        selectCidade.disabled = true;

        try {
            const url = `https://servicodados.ibge.gov.br/api/v1/localidades/estados/${uf}/municipios`;
            const resposta = await fetch(url);
            const cidades = await resposta.json();

            selectCidade.innerHTML = '<option value="">Selecione a Cidade...</option>';
            selectCidade.disabled = false; 

            cidades.forEach(cidade => {
                const option = document.createElement('option');
                option.value = cidade.nome;
                option.textContent = cidade.nome;
                selectCidade.appendChild(option);
            });

        } catch (erro) {
            console.error("Erro ao buscar cidades:", erro);
            selectCidade.innerHTML = '<option value="">Erro ao carregar cidades</option>';
        }
    }

    // 2. Atrelamos a mesma função aos dois eventos!
    selectEstado.addEventListener('change', carregarCidades);
    selectEstado.addEventListener('input', carregarCidades);

    document.addEventListener('DOMContentLoaded', () => {
        // 3. Chamamos a função para carregar as cidades caso o estado já esteja selecionado
        if (selectEstado.value) {
            carregarCidades();
        }
        else {
            selectCidade.innerHTML = '<option value="">Selecione primeiro o Estado</option>';
            selectCidade.disabled = true;
        }
    });