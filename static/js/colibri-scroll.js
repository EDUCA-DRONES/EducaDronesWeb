var sec = document.getElementById('colibri-scroll');
var can = document.getElementById('colibriCanvas');

if (sec && can) {
  var ctx = can.getContext('2d');
  var total = 171;
  var pasta = sec.getAttribute('data-frames');
  var imgs = [];
  var alvo = 0;
  var atual = 0;
  var ultimo = -1;

  function desenhar(num) {
    var img = imgs[num];

    if (!img || !img.complete) {
      return;
    }
    if (can.width !== img.naturalWidth) {
      can.width = img.naturalWidth;
      can.height = img.naturalHeight;
    }

    ctx.drawImage(img, 0, 0);
    ultimo = num;
  }

  function carregarImagens() {
    var i;
    var nome;
    var img;

    for (i = 0; i < total; i++) {
      nome = String(i + 1);

      while (nome.length < 3) {
        nome = '0' + nome;
      }

      img = new Image();
      img.src = pasta + 'f' + nome + '.webp';
      imgs[i] = img;
      img.onload = function () {
        if (this === imgs[0]) {
          desenhar(0);
        }
      };
    }
  }

  function lerScroll() {
    var percurso = sec.offsetHeight - window.innerHeight;
    var andado = -sec.getBoundingClientRect().top;

    if (percurso <= 0) {
        alvo = 0;
    } else {
        alvo = andado / percurso;

        if (alvo < 0) {
            alvo = 0;
        }
    }
  }
  
  function animar() {
    atual = atual + (alvo - atual) * 0.15;
    var num = Math.round(atual * (total - 1));
    
    if (num !== ultimo) {
      desenhar(num);
    }

    requestAnimationFrame(animar);
  }
  
  carregarImagens();
  window.addEventListener('scroll', lerScroll);
  window.addEventListener('resize', lerScroll);
  lerScroll();
  animar();
}
