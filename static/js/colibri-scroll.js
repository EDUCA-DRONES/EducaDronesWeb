function iniciarCanvas() {
  const sec = document.getElementById('colibri-scroll');
  const can = document.getElementById('colibriCanvas');
  const card = sec && sec.querySelector('.colibri-card');
  if (!card || !can) return;

  const ctx = can.getContext('2d');
  const total = 171;
  const pasta = sec.dataset.frames; 
  const html = document.documentElement;
  const body = document.body;
  const overflow = html.style.overflow;
  const padding = body.style.paddingRight;
  const imgs = [];

  let alvo = 0, atual = 0, ultimo = -1;
  let travado = false, lado = -1, toqueY = 0, pausa = 0;

  const frameAtual = () => Math.round(atual * (total - 1));

  const centro = () => {
    const r = card.getBoundingClientRect();
    return Math.round(window.pageYOffset + r.top - (window.innerHeight - r.height) / 2);
  };

  const irPara = (y) => window.scrollTo({ top: y, behavior: 'instant' });

  function desenhar(num) {
    const img = imgs[num];
    if (!img || !img.naturalWidth) return;

    if (can.width !== img.naturalWidth) {
      can.width = img.naturalWidth;
      can.height = img.naturalHeight;
    }
    ctx.clearRect(0, 0, can.width, can.height);
    ctx.drawImage(img, 0, 0);
    ultimo = num;
  }

  function travar() {
    const barra = window.innerWidth - html.clientWidth;

    if (Math.abs(window.pageYOffset - centro()) > 2) irPara(centro());

    if (barra > 0) {
      body.style.paddingRight = (parseFloat(getComputedStyle(body).paddingRight) || 0) + barra + 'px';
    }
    html.style.overflow = 'hidden';
    travado = true;
  }

  function liberar(direcao) {
    travado = false;
    html.style.overflow = overflow;
    body.style.paddingRight = padding;

    if (direcao != 0) {
      lado = direcao;
    } 
    else {
      if (window.pageYOffset < centro()) {
        lado = -1;
      } 
      else {
        lado = 1;
      }
    }
  }

  function mover(delta) {
    if (!delta) return false;

    const noLimite = (alvo >= 1 && delta > 0) || (alvo <= 0 && delta < 0);

    if (noLimite) {
      if (Math.abs(atual - alvo) < 0.001) {

        if(delta > 1) {
          liberar(1);
        }
        else {
          liberar(-1);
        }
        
        return false;
      }
      return true;
    }

    alvo = Math.min(1, Math.max(0, alvo + delta / (window.innerHeight * 2)));
    return true;
  }

  function lerScroll() {
    if (travado) return;

    const y = window.pageYOffset;
    const pos = centro();

    if (Date.now() > pausa) {
      if ((lado < 0 && y > pos && alvo < 1) || (lado > 0 && y < pos && alvo > 0)) {
        travar();
        return;
      }
    }

    if (y > pos + 2) lado = 1;
    if (y < pos - 2) lado = -1;
  }

  function aoGirar(e) {
    if (!travado || e.ctrlKey) return;

    let d = e.deltaY * [1, 16, window.innerHeight][e.deltaMode];
    d = Math.max(-120, Math.min(120, d));

    if (mover(d) && e.cancelable) e.preventDefault();
  }

  function aoTocar(e) {
    const y = e.touches[0].clientY;
    const d = toqueY - y;
    toqueY = y;

    if (travado && mover(d) && e.cancelable) e.preventDefault();
  }

  function aoApertar(e) {
    if (!travado || e.ctrlKey || e.metaKey || e.altKey) return;
    if (e.target.matches('input, textarea, select') || e.target.isContentEditable) return;

    const h = window.innerHeight;
    const teclas = {
      ArrowDown: 60,
      ArrowUp: -60,
      PageDown: h * 0.8,
      PageUp: -h * 0.8,
      ' ': h * 0.8,
      End: h * 3,
      Home: -h * 3
    };
    if (e.key === ' ' && e.shiftKey) {
      teclas[' '] = -h * 0.8;
    }

    if (teclas[e.key] !== undefined && mover(teclas[e.key])) e.preventDefault();
  }

  function animar() {
    atual += (alvo - atual) * 0.2;

    const num = frameAtual();
    if (num !== ultimo) desenhar(num);

    requestAnimationFrame(animar);
  }

  for (let i = 0; i < total; i++) {
    const img = new Image();
    imgs[i] = img;

    img.onload = () => {
      if (i === frameAtual() || (ultimo === -1 && i === 0)) desenhar(i);
    };
    img.onerror = () => console.error('Erro ao carregar frame:', img.src);
    img.src = pasta + 'f' + String(i + 1).padStart(3, '0') + '.webp';
  }

  if (window.pageYOffset > centro()) {
    alvo = atual = 1;
    lado = 1;
  }

  document.addEventListener('click', (e) => {
    if (e.target.closest('a[href^="#"]')) {
      pausa = Date.now() + 1500;
      if (travado) liberar(0);
    }
  });

  window.addEventListener('scroll', lerScroll, { passive: true });
  window.addEventListener('resize', () => travado && irPara(centro()));
  window.addEventListener('wheel', aoGirar, { passive: false });
  window.addEventListener('touchstart', (e) => { toqueY = e.touches[0].clientY; }, { passive: true });
  window.addEventListener('touchmove', aoTocar, { passive: false });
  window.addEventListener('keydown', aoApertar);

  animar();
}

// 2. O observador de Lazy Load que vai disparar a sua função
document.addEventListener("DOMContentLoaded", function() {
  var sectionAlvo = document.getElementById('colibri-scroll');

  if (sectionAlvo) {
    var observerOptions = {
      root: null,
      rootMargin: "1500px 0px", // Começa a carregar 1500px antes da seção aparecer
      threshold: 0
    };

    var observer = new IntersectionObserver(function(entries, obs) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          
          // Dispara a função que criamos com o SEU código
          iniciarCanvas();
          
          // Remove o observador para garantir que sua função rode apenas uma vez
          obs.unobserve(entry.target);
        }
      });
    }, observerOptions);

    observer.observe(sectionAlvo);
  }
});