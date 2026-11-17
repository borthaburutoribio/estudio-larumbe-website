/* Agenda del mes. Se actualiza una vez por mes con la agenda oficial de ARCA
   (https://www.arca.gob.ar/vencimientos/). Cada fila: qué vence, y la fecha
   para cada terminación de CUIT (0 a 9). Fechas en formato AAAA-MM-DD.
   Noviembre 2026: copiado de la agenda de ARCA el 16/11/2026. */
window.VENCIMIENTOS = {
  mes: 'noviembre de 2026',
  mesCorto: 'noviembre',
  fuente: 'Fuente: agenda de vencimientos de ARCA, consultada el 16/11/2026. Si cae feriado, se corre al día hábil siguiente.',
  arba: 'Ingresos Brutos ARBA · Lorem ipsum', // A CONFIRMAR: fechas de ARBA del mes
  filas: [
    { que: 'Autónomos · pago mensual',
      f: ['2026-11-05','2026-11-05','2026-11-05','2026-11-05','2026-11-11','2026-11-11','2026-11-11','2026-11-12','2026-11-12','2026-11-12'] },
    { que: 'Empleadores · formulario 931',
      f: ['2026-11-11','2026-11-11','2026-11-11','2026-11-11','2026-11-12','2026-11-12','2026-11-12','2026-11-13','2026-11-13','2026-11-13'] },
    { que: 'Casas particulares · pago obligatorio', todos: '2026-11-11' },
    { que: 'Ganancias · declaración jurada 2025', todos: '2026-11-16' },
    { que: 'IVA · declaración y pago',
      f: ['2026-11-18','2026-11-18','2026-11-19','2026-11-19','2026-11-20','2026-11-20','2026-11-24','2026-11-24','2026-11-25','2026-11-25'] },
    { que: 'Monotributo · cuota mensual', todos: '2026-11-20' }
  ]
};
