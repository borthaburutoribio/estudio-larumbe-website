(function () {
  'use strict';
  var WA = '5492926412120';
  var root = document.documentElement;
  root.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Menú móvil */
  var toggle = document.querySelector('.nav-toggle');
  var list = document.getElementById('menu');
  if (toggle && list) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      toggle.textContent = open ? 'Menú' : 'Cerrar';
      list.classList.toggle('is-open', !open);
    });
    list.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        toggle.setAttribute('aria-expanded', 'false');
        toggle.textContent = 'Menú';
        list.classList.remove('is-open');
      }
    });
  }

  /* Entradas por sección: título, texto, imagen, escalonados */
  var items = document.querySelectorAll('.rise, .tiles img, .mosaic img, .about-photo img, .contact-pic img, .faq-band, .cmp-row, .sq');
  if ('IntersectionObserver' in window) {
    var groups = new Map();
    items.forEach(function (el) {
      var sec = el.closest('section') || document.body;
      var n = groups.get(sec) || 0;
      groups.set(sec, n + 1);
      el.style.setProperty('--d', (el.classList.contains('sq') ? Math.min(n, 140) * 6 : Math.min(n, 10) * 75) + 'ms');
      el.classList.add('pre');
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    items.forEach(function (el) { io.observe(el); });
  }

  /* Vencimientos */
  var V = window.VENCIMIENTOS;
  var DIAS = ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'];
  function parse(s) { var p = s.split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function today() { var t = new Date(); return new Date(t.getFullYear(), t.getMonth(), t.getDate()); }
  function fmt(d) { return DIAS[d.getDay()] + ' ' + ('0' + d.getDate()).slice(-2) + '/' + ('0' + (d.getMonth() + 1)).slice(-2); }
  function short(d) { return ('0' + d.getDate()).slice(-2) + '/' + ('0' + (d.getMonth() + 1)).slice(-2); }
  function rowsFor(dig) {
    return V.filas.map(function (r) {
      return { que: r.que, d: parse(r.todos || r.f[dig]) };
    }).sort(function (a, b) { return a.d - b.d; });
  }
  function estado(d) {
    var t = today();
    if (d < t) return { txt: 'Vencido', cls: 'is-past' };
    if (+d === +t) return { txt: 'Hoy', cls: 'is-today' };
    return { txt: 'Faltan ' + Math.round((d - t) / 864e5) + ' días', cls: 'is-next' };
  }

  var body = document.getElementById('sh-body');
  var shD = document.getElementById('sh-d');
  var sheet = document.getElementById('sheet');
  var waBtn = document.getElementById('dues-wa');
  var digits = document.querySelectorAll('.digit');

  function render(dig) {
    if (!V || !body) return;
    var html = '';
    var firstNext = true;
    rowsFor(dig).forEach(function (r) {
      var e = estado(r.d);
      var mark = '';
      if (e.cls !== 'is-past' && firstNext) { mark = ' is-first'; firstNext = false; }
      html += '<tr class="' + e.cls + mark + '"><td>' + r.que + '</td><td>' + fmt(r.d) + '</td><td>' + e.txt + '</td></tr>';
    });
    if (firstNext) {
      html += '<tr class="is-next"><td colspan="3">Ya pasaron los vencimientos de ' + V.mesCorto + '. La agenda del mes que viene la cargamos apenas la publica ARCA.</td></tr>';
    }
    var swap = function () {
      body.innerHTML = html;
      shD.textContent = dig;
      sheet.classList.remove('is-swapping');
    };
    if (reduce || !sheet.classList.contains('ready')) { swap(); sheet.classList.add('ready'); }
    else { sheet.classList.add('is-swapping'); setTimeout(swap, 180); }
    digits.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-d') === String(dig))); });
    if (waBtn) {
      waBtn.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent('Hola, mi CUIT termina en ' + dig + '. Me pueden avisar cuando se me vence algo?');
    }
  }
  digits.forEach(function (b) {
    b.addEventListener('click', function () { render(+b.getAttribute('data-d')); });
  });
  if (V && body) {
    var ex = sheet.querySelector('.sh-row-extra'); if (ex) ex.textContent = V.arba;
    var ft = sheet.querySelector('.sh-foot'); if (ft) ft.textContent = V.fuente;
    var tt = sheet.querySelector('.sh-title'); if (tt) tt.textContent = 'Vencimientos de ' + V.mes;
    render(0);
  }

  /* Próximo vencimiento en el hero (el primero que no pasó, de cualquier CUIT) */
  (function () {
    if (!V) return;
    var t = today(), best = null;
    V.filas.forEach(function (r) {
      var groups = {};
      for (var i = 0; i < 10; i++) {
        var s = r.todos || r.f[i];
        (groups[s] = groups[s] || []).push(i);
      }
      Object.keys(groups).forEach(function (s) {
        var d = parse(s);
        if (d >= t && (!best || d < best.d)) best = { d: d, que: r.que.split(' · ')[0], dig: groups[s], all: !!r.todos };
      });
    });
    var fig = document.getElementById('nd-fig'), txt = document.getElementById('nd-text');
    if (!fig || !txt) return;
    if (!best) { fig.textContent = 'ARCA'; txt.textContent = 'Consultá tus vencimientos del mes según tu CUIT'; return; }
    fig.textContent = +best.d === +t ? 'Hoy' : short(best.d);
    var who = best.all ? 'para todos los CUIT' : 'para los CUIT terminados en ' + best.dig.join(', ').replace(/, (\d)$/, ' y $1');
    txt.textContent = 'Vence ' + best.que + ' ' + who;
  })();

  /* Botón fijo de WhatsApp: aparece después del hero */
  var fab = document.querySelector('.wa-fab'), hero = document.querySelector('.hero');
  if (fab && hero) {
    var onScroll = function () { fab.classList.toggle('show', window.scrollY > hero.offsetHeight * 0.8); };
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  }

  /* Compartir */
  var share = document.getElementById('share');
  if (share) {
    share.addEventListener('click', function () {
      var data = { title: document.title, url: location.href };
      if (navigator.share) { navigator.share(data).catch(function () {}); }
      else if (navigator.clipboard) {
        navigator.clipboard.writeText(location.href).then(function () { share.textContent = 'Link copiado'; });
      }
    });
  }
})();
