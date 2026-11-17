/* Calculadoras del estudio: monotributo, sueldo y aguinaldo, arrendamiento y lista de papeles.
   Monotributo: valores de ARCA de aplicación desde el 1/08/2026. */
(function () {
  'use strict';
  var WA = '5492926412120';
  var MONO = [
    ['A', 12009410.45, 49527.18, 49527.18], ['B', 17595182.74, 56379.08, 56379.08], ['C', 24670494.31, 66020.12, 64530.58],
    ['D', 30628651.43, 84612.93, 82564.81], ['E', 36028231.33, 119811.45, 108267.51], ['F', 45151659.41, 150784.21, 129930.65],
    ['G', 53995798.87, 230312.94, 158815.05], ['H', 81924660.37, 522706.68, 317895.01], ['I', 91699761.90, 963747.86, 474992.78],
    ['J', 105012519.20, 1167299.76, 580793.69], ['K', 126610838.75, 1614446.04, 702103.24]
  ];
  var fmt0 = new Intl.NumberFormat('es-AR', { maximumFractionDigits: 0 });
  var fmt2 = new Intl.NumberFormat('es-AR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  function ars(n) { return '$ ' + fmt0.format(Math.round(n)); }
  function money(el) { return +(el.value || '').replace(/\D/g, '') || 0; }
  function num(el) { return parseFloat((el.value || '').replace(/\./g, '').replace(',', '.')) || 0; }
  function wa(text) { return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(text); }

  /* Formato de miles mientras se escribe */
  document.querySelectorAll('[data-money]').forEach(function (el) {
    el.addEventListener('input', function () {
      var d = el.value.replace(/\D/g, '');
      el.value = d ? '$ ' + fmt0.format(+d) : '';
    });
  });

  function outs(form) {
    var sec = form.closest('section');
    var o = {};
    sec.querySelectorAll('[data-out]').forEach(function (e) { o[e.getAttribute('data-out')] = e; });
    o.cta = sec.querySelector('[data-wa]');
    return o;
  }
  function set(o, k, v) { if (o[k]) o[k].textContent = v; }

  /* Monotributo */
  document.querySelectorAll('form[data-calc="mono"]').forEach(function (f) {
    var o = outs(f);
    function run() {
      var ing = money(f.ing);
      var serv = f.querySelector('input[name="act"]:checked').value === 's';
      var col = serv ? 2 : 3;
      if (!ing) {
        set(o, 'cat', '–'); set(o, 'catlab', 'Poné cuánto facturaste');
        ['cuota', 'tope', 'margen'].forEach(function (k) { set(o, k, '–'); });
        o.cta.href = wa('Hola Mariano, quiero revisar mi categoría del monotributo.');
        return;
      }
      var row = null;
      for (var i = 0; i < MONO.length; i++) { if (ing <= MONO[i][1]) { row = MONO[i]; break; } }
      if (!row) {
        set(o, 'cat', '—'); set(o, 'catlab', 'Pasaste el tope del monotributo');
        set(o, 'cuota', 'Régimen general'); set(o, 'tope', ars(MONO[10][1])); set(o, 'margen', 'Te pasaste por ' + ars(ing - MONO[10][1]));
        set(o, 'nota', 'Con esa facturación corresponde el régimen general: IVA y Ganancias. Escribinos y lo vemos con tus números.');
        o.cta.href = wa('Hola Mariano, facturé ' + ars(ing) + ' en los últimos 12 meses y la calculadora dice que pasé el tope del monotributo. Lo vemos?');
        return;
      }
      set(o, 'cat', row[0]);
      set(o, 'catlab', 'Categoría ' + row[0] + (serv ? ', servicios' : ', venta de cosas'));
      set(o, 'cuota', '$ ' + fmt2.format(row[col]));
      set(o, 'tope', ars(row[1]));
      set(o, 'margen', ars(row[1] - ing));
      set(o, 'nota', 'La categoría también depende de la superficie del local, la energía y los alquileres. Esta cuenta mira solo los ingresos.');
      o.cta.href = wa('Hola Mariano, facturé ' + ars(ing) + ' en los últimos 12 meses (' + (serv ? 'servicios' : 'venta de cosas') + ') y la calculadora me da la categoría ' + row[0] + '. Me ayudás a revisarla?');
    }
    f.addEventListener('input', run); f.addEventListener('change', run); run();
  });

  /* Sueldo y aguinaldo */
  document.querySelectorAll('form[data-calc="sueldo"]').forEach(function (f) {
    var o = outs(f);
    function run() {
      var b = money(f.bruto), m = money(f.mejor) || b, n = +f.meses.value || 6, s = f.sind.checked ? 0.02 : 0;
      if (!b && !m) {
        ['bruto', 'jub', 'pami', 'os', 'sin', 'neto', 'sac', 'sacneto'].forEach(function (k) { set(o, k, '–'); });
        o.cta.href = wa('Hola Mariano, quiero que el estudio liquide los sueldos de mis empleados.');
        return;
      }
      var jub = b * 0.11, pami = b * 0.03, os = b * 0.03, sin = b * s, neto = b - jub - pami - os - sin;
      var sac = m / 2 * n / 6, sacNeto = sac * (1 - 0.17 - s);
      set(o, 'bruto', ars(b)); set(o, 'jub', '− ' + ars(jub)); set(o, 'pami', '− ' + ars(pami)); set(o, 'os', '− ' + ars(os));
      set(o, 'sin', s ? '− ' + ars(sin) : 'No'); set(o, 'neto', ars(neto)); set(o, 'sac', ars(sac)); set(o, 'sacneto', ars(sacNeto));
      o.cta.href = wa('Hola Mariano, quiero que el estudio liquide sueldos y aguinaldo. Tengo un sueldo bruto de ' + ars(b) + '.');
    }
    f.addEventListener('input', run); f.addEventListener('change', run); run();
  });

  /* Arrendamiento en quintales */
  document.querySelectorAll('form[data-calc="arr"]').forEach(function (f) {
    var o = outs(f);
    function run() {
      var ha = num(f.ha), qq = num(f.qq), p = money(f.precio), c = +f.cuotas.value || 1;
      var qqt = ha * qq, tn = qqt / 10;
      set(o, 'qqt', qqt ? fmt0.format(qqt) + ' qq' : '–');
      set(o, 'tn', tn ? fmt2.format(tn) + ' t' : '–');
      set(o, 'total', tn && p ? ars(tn * p) : '–');
      set(o, 'cuota', tn && p ? ars(tn * p / c) + ' (' + c + (c === 1 ? ' pago' : ' pagos') + ')' : '–');
      o.cta.href = wa(qqt ? 'Hola Mariano, tengo un arrendamiento de ' + fmt0.format(ha) + ' ha a ' + fmt2.format(qq) + ' qq por ha. Me ayudás a declararlo?' : 'Hola Mariano, quiero consultar por un arrendamiento.');
    }
    f.addEventListener('input', run); f.addEventListener('change', run); run();
  });

  /* Lista de papeles de la campaña */
  document.querySelectorAll('form[data-calc="papeles"]').forEach(function (f) {
    var btn = f.querySelector('[data-wa]');
    function run() {
      var all = [].slice.call(f.querySelectorAll('input[type="checkbox"]'));
      var si = all.filter(function (i) { return i.checked; }).map(function (i) { return i.value; });
      var no = all.filter(function (i) { return !i.checked; }).map(function (i) { return i.value; });
      var t = 'Hola Mariano, junto los papeles de la campaña.';
      if (si.length) t += '\nYa tengo: ' + si.join(', ') + '.';
      if (no.length && si.length) t += '\nTodavía no: ' + no.join(', ') + '.';
      t += '\nQué me falta?';
      btn.href = wa(t);
    }
    f.addEventListener('change', run); run();
  });
})();
