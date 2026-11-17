# Textos de las páginas internas. Datos fiscales verificados el 16/11/2026:
# - Monotributo: tabla de ARCA "Valores de aplicación desde el 1/08/2026" (arca.gob.ar/monotributo/categorias.asp)
# - Vencimientos: agenda de ARCA de noviembre 2026 (vencimientos.js)
# Lo que dice "A CONFIRMAR" lo tiene que confirmar el estudio.

SITE = 'https://borthaburutoribio.github.io/estudio-larumbe-website/'
WA = '5492926412120'
WA_TXT = 'Hola Mariano, te escribo desde la web del estudio.'
NAV = [('Soluciones', 'soluciones/'), ('Monotributo', 'monotributo/'), ('Sueldos', 'sueldos/'),
       ('Campo', 'campo/'), ('Vencimientos', 'vencimientos/')]

# Monotributo: (categoría, tope de ingresos brutos anuales, cuota total servicios, cuota total venta de cosas muebles)
MONO = [('A', 12009410.45, 49527.18, 49527.18), ('B', 17595182.74, 56379.08, 56379.08), ('C', 24670494.31, 66020.12, 64530.58),
        ('D', 30628651.43, 84612.93, 82564.81), ('E', 36028231.33, 119811.45, 108267.51), ('F', 45151659.41, 150784.21, 129930.65),
        ('G', 53995798.87, 230312.94, 158815.05), ('H', 81924660.37, 522706.68, 317895.01), ('I', 91699761.90, 963747.86, 474992.78),
        ('J', 105012519.20, 1167299.76, 580793.69), ('K', 126610838.75, 1614446.04, 702103.24)]


def ars(n):
    s = f'{n:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return '$' + s


mono_rows = ''.join(f'<tr><th scope="row">{c}</th><td data-l="Ingresos hasta">{ars(t)}</td><td data-l="Servicios">{ars(s)}</td><td data-l="Venta de cosas">{ars(v)}</td></tr>' for c, t, s, v in MONO)

TOOL_MONO = f'''<section class="tool" id="calculadora" aria-labelledby="t-mono">
  <div class="tool-pick">
    <h2 id="t-mono" class="h-head rise">¿En qué categoría estás?</h2>
    <p class="tool-help">Con los valores de ARCA vigentes desde el 1 de agosto de 2026.</p>
    <form class="calc" data-calc="mono" novalidate>
      <fieldset class="seg">
        <legend>Qué hacés</legend>
        <label><input type="radio" name="act" value="s" checked><span>Servicios</span></label>
        <label><input type="radio" name="act" value="v"><span>Vendo cosas</span></label>
      </fieldset>
      <label class="field"><span>Lo que facturaste en los últimos 12 meses</span>
        <input type="text" inputmode="numeric" name="ing" placeholder="$ 0" autocomplete="off" data-money></label>
    </form>
  </div>
  <div class="tool-stage">
    <article class="sheet" data-ui aria-live="polite">
      <p class="sh-from">Estudio Contable Mariano A. Larumbe · Sarmiento 449</p>
      <p class="sh-title">Tu categoría de monotributo</p>
      <div class="res-big"><span class="res-fig" data-out="cat">–</span><span class="res-lab" data-out="catlab">Poné cuánto facturaste</span></div>
      <table class="sh-table res-table"><tbody>
        <tr><td>Cuota mensual total</td><td data-out="cuota">–</td></tr>
        <tr><td>Tope de la categoría</td><td data-out="tope">–</td></tr>
        <tr><td>Te quedan para facturar</td><td data-out="margen">–</td></tr>
      </tbody></table>
      <p class="sh-foot" data-out="nota">La categoría también depende de la superficie del local, la energía y los alquileres. Esta cuenta mira solo los ingresos.</p>
      <a class="btn btn-ink sheet-cta" data-wa="mono" href="https://wa.me/{WA}" target="_blank" rel="noopener">Revisar mi categoría con el estudio</a>
    </article>
  </div>
</section>
<section class="cats" aria-labelledby="t-cats">
  <h2 id="t-cats" class="h-head rise">Las 11 categorías</h2>
  <div class="cats-wrap rise"><table class="cats-table">
    <thead><tr><th scope="col">Categoría</th><th scope="col">Ingresos brutos anuales hasta</th><th scope="col">Cuota por mes, servicios</th><th scope="col">Cuota por mes, venta de cosas</th></tr></thead>
    <tbody>{mono_rows}</tbody></table></div>
  <p class="note">Fuente: ARCA, valores de aplicación desde el 1/08/2026. La cuota incluye impuesto integrado, jubilación (SIPA) y obra social.</p>
</section>'''

TOOL_SUELDO = f'''<section class="tool" id="calculadora" aria-labelledby="t-sue">
  <div class="tool-pick">
    <h2 id="t-sue" class="h-head rise">Sueldo y aguinaldo</h2>
    <p class="tool-help">Cuenta orientativa para empleados en relación de dependencia.</p>
    <form class="calc" data-calc="sueldo" novalidate>
      <label class="field"><span>Sueldo bruto del mes</span>
        <input type="text" inputmode="numeric" name="bruto" placeholder="$ 0" autocomplete="off" data-money></label>
      <label class="field"><span>Mejor sueldo bruto del semestre</span>
        <input type="text" inputmode="numeric" name="mejor" placeholder="Igual al de arriba" autocomplete="off" data-money></label>
      <label class="field"><span>Meses trabajados del semestre</span>
        <select name="meses"><option>6</option><option>5</option><option>4</option><option>3</option><option>2</option><option>1</option></select></label>
      <label class="check"><input type="checkbox" name="sind"><span>Está afiliado al sindicato (2 %)</span></label>
    </form>
  </div>
  <div class="tool-stage">
    <article class="sheet" data-ui aria-live="polite">
      <p class="sh-from">Estudio Contable Mariano A. Larumbe · Sarmiento 449</p>
      <p class="sh-title">Recibo estimado</p>
      <table class="sh-table res-table"><tbody>
        <tr><td>Sueldo bruto</td><td data-out="bruto">–</td></tr>
        <tr><td>Jubilación (11 %)</td><td data-out="jub">–</td></tr>
        <tr><td>Ley 19.032, PAMI (3 %)</td><td data-out="pami">–</td></tr>
        <tr><td>Obra social (3 %)</td><td data-out="os">–</td></tr>
        <tr><td>Sindicato</td><td data-out="sin">–</td></tr>
        <tr class="is-first"><td>Sueldo neto</td><td data-out="neto">–</td></tr>
        <tr><td>Aguinaldo de diciembre, bruto</td><td data-out="sac">–</td></tr>
        <tr class="is-first"><td>Aguinaldo de diciembre, neto</td><td data-out="sacneto">–</td></tr>
      </tbody></table>
      <p class="sh-foot">Cada convenio suma sus propios ítems (adicionales, seguro de vida, aportes del convenio). El recibo real lo liquidamos con el tuyo.</p>
      <a class="btn btn-ink sheet-cta" data-wa="sueldo" href="https://wa.me/{WA}" target="_blank" rel="noopener">Que el estudio liquide mis sueldos</a>
    </article>
  </div>
</section>'''

TOOL_CAMPO = f'''<section class="tool" id="calculadora" aria-labelledby="t-arr">
  <div class="tool-pick">
    <h2 id="t-arr" class="h-head rise">Arrendamiento en quintales</h2>
    <p class="tool-help">Pasá a pesos lo que se paga en quintales por hectárea.</p>
    <form class="calc" data-calc="arr" novalidate>
      <label class="field"><span>Hectáreas</span>
        <input type="text" inputmode="numeric" name="ha" placeholder="0" autocomplete="off" data-num></label>
      <label class="field"><span>Quintales por hectárea por año</span>
        <input type="text" inputmode="decimal" name="qq" placeholder="0" autocomplete="off" data-num></label>
      <label class="field"><span>Precio del grano, en pesos por tonelada</span>
        <input type="text" inputmode="numeric" name="precio" placeholder="El de la pizarra del día" autocomplete="off" data-money></label>
      <label class="field"><span>Cuotas por año</span>
        <select name="cuotas"><option>2</option><option>1</option><option>3</option><option>4</option></select></label>
    </form>
  </div>
  <div class="tool-stage">
    <article class="sheet" data-ui aria-live="polite">
      <p class="sh-from">Estudio Contable Mariano A. Larumbe · Sarmiento 449</p>
      <p class="sh-title">Cuánto da el arrendamiento</p>
      <table class="sh-table res-table"><tbody>
        <tr><td>Quintales por año</td><td data-out="qqt">–</td></tr>
        <tr><td>Toneladas por año</td><td data-out="tn">–</td></tr>
        <tr class="is-first"><td>Total por año, en pesos</td><td data-out="total">–</td></tr>
        <tr><td>Cada cuota</td><td data-out="cuota">–</td></tr>
      </tbody></table>
      <p class="sh-foot">Un quintal son 100 kilos. El precio de referencia es el que fije el contrato (por ejemplo, la pizarra de Bahía Blanca o de Rosario el día anterior al pago).</p>
      <a class="btn btn-ink sheet-cta" data-wa="arr" href="https://wa.me/{WA}" target="_blank" rel="noopener">Declarar el arrendamiento con el estudio</a>
    </article>
  </div>
</section>
<section class="papers" id="papeles" aria-labelledby="t-pap">
  <div class="papers-head">
    <h2 id="t-pap" class="h-head rise">¿Qué papeles tenés?</h2>
    <p class="body rise">Marcá lo que ya juntaste de la campaña. Le mandamos la lista al estudio y te dicen qué falta.</p>
  </div>
  <form class="papers-list" data-calc="papeles">
    <label><input type="checkbox" value="Liquidaciones de granos"><span>Liquidaciones de granos</span></label>
    <label><input type="checkbox" value="Cartas de porte"><span>Cartas de porte</span></label>
    <label><input type="checkbox" value="Contratos de arrendamiento"><span>Contratos de arrendamiento</span></label>
    <label><input type="checkbox" value="Facturas de insumos y contratistas"><span>Facturas de insumos y contratistas</span></label>
    <label><input type="checkbox" value="Constancia del SISA"><span>Constancia del SISA</span></label>
    <label><input type="checkbox" value="Movimientos de hacienda (DTe)"><span>Movimientos de hacienda (DTe)</span></label>
    <label><input type="checkbox" value="Extractos del banco"><span>Extractos del banco</span></label>
    <label><input type="checkbox" value="Recibos de sueldo de peones"><span>Recibos de sueldo de peones</span></label>
    <a class="btn btn-ink" data-wa="papeles" href="https://wa.me/{WA}" target="_blank" rel="noopener">Mandarle la lista al estudio</a>
  </form>
</section>'''

TOOL_VENC = '''<section class="dues" id="calculadora" aria-labelledby="v-title">
  <div class="dues-pick">
    <h2 id="v-title" class="h-head rise">Tus vencimientos</h2>
    <p class="dues-help">Noviembre de 2026. Tocá el último número de tu CUIT.</p>
    <div class="digits" role="group" aria-label="Último número del CUIT">''' + ''.join(f'<button type="button" class="digit" data-d="{d}">{d}</button>' for d in range(10)) + f'''</div>
    <a class="btn btn-paper" id="dues-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">Que me avisen por WhatsApp</a>
  </div>
  <div class="dues-stage">
    <article class="sheet" data-ui id="sheet" aria-live="polite">
      <header class="sh-head">
        <p class="sh-from">Estudio Contable Mariano A. Larumbe<br>Sarmiento 449 · Coronel Suárez</p>
        <p class="sh-title">Vencimientos de noviembre de 2026</p>
        <p class="sh-cuit">CUIT terminado en <strong id="sh-d">0</strong></p>
      </header>
      <table class="sh-table">
        <thead><tr><th scope="col">Qué vence</th><th scope="col">Fecha</th><th scope="col">Estado</th></tr></thead>
        <tbody id="sh-body"><tr><td>IVA · declaración y pago</td><td>Mié 18/11</td><td>Próximo</td></tr></tbody>
      </table>
      <!-- A CONFIRMAR: fechas de ARBA del mes -->
      <p class="sh-row-extra">Ingresos Brutos ARBA · Lorem ipsum</p>
      <p class="sh-foot">Fuente: agenda de vencimientos de ARCA, consultada el 16/11/2026.</p>
    </article>
  </div>
</section>
<section class="cats" aria-labelledby="t-iva">
  <h2 id="t-iva" class="h-head rise">IVA de noviembre</h2>
  <div class="cats-wrap rise"><table class="cats-table">
    <thead><tr><th scope="col">CUIT terminado en</th><th scope="col">Presentación y pago</th></tr></thead>
    <tbody><tr><th scope="row">0 y 1</th><td>Miércoles 18/11</td></tr><tr><th scope="row">2 y 3</th><td>Jueves 19/11</td></tr><tr><th scope="row">4 y 5</th><td>Viernes 20/11</td></tr><tr><th scope="row">6 y 7</th><td>Martes 24/11</td></tr><tr><th scope="row">8 y 9</th><td>Miércoles 25/11</td></tr></tbody></table></div>
  <p class="note">Fuente: agenda de vencimientos de ARCA de noviembre de 2026.</p>
</section>'''

TOOL_SOL = None  # la página de soluciones usa su propia lista

SOLUCIONES = [
    ('Me vence algo y no sé qué ni cuándo.', 'Te avisamos por WhatsApp antes de cada vencimiento de tu CUIT y te mandamos el VEP listo para pagar desde el home banking.', 'Ver mis vencimientos', 'vencimientos/'),
    ('Facturo más y no sé si me pasé de categoría.', 'Revisamos tu facturación antes de cada recategorización, en enero y en julio, y te decimos si subís, si bajás o si te conviene pasar a inscripto.', 'Calcular mi categoría', 'monotributo/'),
    ('Vendí la cosecha y tengo una pila de liquidaciones.', 'Ordenamos liquidaciones de granos, retenciones y cartas de porte, y las cruzamos con lo que ARCA ya tiene tuyo antes de presentar el IVA.', 'Ver lo que hacemos para el campo', 'campo/'),
    ('Arriendo el campo y cobro en quintales.', 'Pasamos los quintales a pesos con el valor de cada pago, registramos el contrato en ARCA y lo incluimos en tu declaración.', 'Calcular el arrendamiento', 'campo/#calculadora'),
    ('Tengo empleados y se viene el aguinaldo.', 'Liquidamos sueldos, aguinaldo y el formulario 931 todos los meses, de comercio y de peones rurales.', 'Calcular sueldo y aguinaldo', 'sueldos/'),
    ('Quiero armar una sociedad con un socio.', 'Te explicamos las opciones, la inscribimos y después llevamos los libros y el balance de cada año.', 'Consultar por WhatsApp', None),
    ('Me llegó una intimación de ARCA o de ARBA.', 'La leemos con vos, vemos qué piden y la contestamos dentro del plazo.', 'Consultar por WhatsApp', None),
    ('No tengo tiempo de ir al estudio cada vez.', 'Nos mandás todo por WhatsApp, en fotos o en PDF. Para firmar algo, nos vemos en Sarmiento 449.', 'Escribir ahora', None),
]

sol_items = ''.join(
    f'<li class="sol"><p class="sol-p rise">{p}</p><div class="sol-a rise"><p>{a}</p>'
    + (f'<a class="link" href="../{u}">{l}</a>' if u else f'<a class="link" href="https://wa.me/{WA}?text=' + __import__('urllib.parse', fromlist=['quote']).quote('Hola Mariano, ' + p[0].lower() + p[1:]) + f'" target="_blank" rel="noopener">{l}</a>')
    + '</div></li>' for p, a, l, u in SOLUCIONES)

TOOL_SOLUCIONES = f'''<section class="sols" id="calculadora" aria-labelledby="t-sol">
  <h2 id="t-sol" class="h-head rise">Lo que nos traen</h2>
  <!-- A CONFIRMAR: que el estudio preste todos estos servicios (sociedades, intimaciones, avisos por WhatsApp) -->
  <ul class="sol-list">{sol_items}</ul>
</section>'''

PAGES = [
  dict(slug='soluciones', band=[('cosechadora-en-trigo.jpg','Cosechadora levantando trigo en un lote'),('libro-contable-antiguo.jpg','Libro contable abierto sobre un escritorio de madera'),('estacion-coronel-suarez.jpg','La estación de tren de Coronel Suárez')], crumb='Soluciones', og='Soluciones · Estudio Larumbe, Coronel Suárez',
       title='Soluciones contables para Coronel Suárez | Estudio Larumbe',
       desc='Vencimientos que se pasan, recategorizaciones, liquidaciones de granos, arrendamientos, sueldos e intimaciones de ARCA: cómo lo resuelve el Estudio Larumbe en Coronel Suárez.',
       h1=['Soluciones'], lead='Lo que más nos consultan, y cómo lo resolvemos. Si lo tuyo no está en la lista, escribinos igual.',
       chips=['Avisos por WhatsApp', 'VEP listo para pagar', 'Campo, comercio y monotributo'],
       wa='Hola Mariano, quiero consultar por el estudio.', tool_id='calculadora', tool_link='Ver la lista',
       img='atardecer-campo-pampeano.jpg', img_w=1400, img_h=2100, img_alt='Atardecer sobre un campo sembrado en la llanura',
       summary=[('Para quién', 'Productores agropecuarios, comercios, monotributistas y empleadores de Coronel Suárez y la zona.'),
                ('Cómo se trabaja', 'Por WhatsApp para lo de todos los meses; en Sarmiento 449 para firmar.'),
                ('Herramientas', 'Calculadora de monotributo, de sueldo y aguinaldo, de arrendamiento en quintales y vencimientos por CUIT.'),
                ('Contacto', 'WhatsApp 2926 41-2120 · Fijo (02926) 42-2292')],
       tool=TOOL_SOLUCIONES,
       sections=[('Antes de que venza', '<p>Casi todo lo que sale caro en impuestos es lo que se presenta tarde: intereses por cada día, multas por no presentar y, en el monotributo, una categoría vieja que ya no corresponde. Por eso trabajamos con el calendario de tu CUIT a la vista y te escribimos antes.</p><p>Lo de todos los meses (IVA, cuota del monotributo, sueldos, Ingresos Brutos) lo resolvemos sin que tengas que venir. Lo de una vez por año (Ganancias, Bienes Personales, el balance) lo empezamos con tiempo.</p>')],
       faq=[('¿Cuánto cobran?', 'Depende de lo que haya que llevar: no es lo mismo un monotributista que una sociedad con campo y empleados. Escribinos y te pasamos el honorario mensual para tu caso. <!-- A CONFIRMAR: honorarios -->'),
            ('¿Puedo cambiarme de contador en cualquier momento?', 'Sí. Nos das acceso con tu clave fiscal, pedimos lo que haga falta al estudio anterior y seguimos desde ahí.'),
            ('¿Atienden fuera de Coronel Suárez?', 'Sí. Lo de todos los meses se resuelve por WhatsApp y nos vemos en el estudio cuando hace falta firmar algo.')],
       related=[('Monotributo', 'monotributo/', 'Calculá tu categoría y tu cuota'), ('Sueldos y aguinaldo', 'sueldos/', 'El neto y el aguinaldo de diciembre'), ('Campo', 'campo/', 'Arrendamiento en quintales y papeles de la campaña'), ('Vencimientos', 'vencimientos/', 'Las fechas de tu CUIT este mes')],
       say='Contanos qué te pasa con tus impuestos y te decimos cómo lo resolvemos.'),

  dict(slug='monotributo', band=[('libro-contable-antiguo.jpg','Libro contable abierto sobre un escritorio de madera'),('silos-junto-a-la-ruta.jpg','Silos de cereal junto a una ruta'),('estacion-coronel-suarez.jpg','La estación de tren de Coronel Suárez')], crumb='Monotributo', og='Monotributo: categoría y cuota · Estudio Larumbe',
       title='Monotributo en Coronel Suárez: categoría y cuota 2026 | Estudio Larumbe',
       desc='Calculá en qué categoría del monotributo estás según lo que facturaste en los últimos 12 meses y cuánto pagás por mes. Valores de ARCA desde el 1/08/2026.',
       h1=['Monotributo'], lead='Poné lo que facturaste en los últimos 12 meses y te decimos en qué categoría estás y cuánto pagás por mes. El alta, la recategorización y la baja te las hacemos nosotros.',
       chips=['Cuota el 20 de cada mes', 'Recategorización en enero y julio', 'Categorías de la A a la K'],
       wa='Hola Mariano, quiero consultar por el monotributo.', tool_id='calculadora', tool_link='Calcular mi categoría',
       img='calculadora-y-lapicera.jpg', img_w=2000, img_h=1333, img_alt='Calculadora y lapicera sobre una hoja con cuentas',
       summary=[('Qué es', 'Un régimen simplificado: una sola cuota por mes con impuesto, jubilación y obra social.'),
                ('Cuándo se paga', 'El 20 de cada mes, para todas las terminaciones de CUIT. En noviembre de 2026, el viernes 20.'),
                ('Recategorización', 'En enero y en julio, mirando lo que facturaste en los últimos 12 meses.'),
                ('Tope', 'Categoría K: $126.610.838,75 de ingresos brutos por año.'),
                ('Factura', 'Factura C, electrónica.')],
       tool=TOOL_MONO,
       sections=[('Cómo se recategoriza', '<p>Dos veces por año, en enero y en julio, hay que mirar lo que facturaste en los últimos 12 meses, la superficie del local, la energía que consumiste y los alquileres que pagaste. Si alguno pasó el tope de tu categoría, subís. Si bajaron, podés bajar y pagar menos.</p><p>Nosotros hacemos la cuenta antes de que abra la recategorización y te avisamos qué te conviene.</p>'),
                 ('Lo que hacemos', '<p>Alta en el monotributo y en Ingresos Brutos, factura electrónica configurada, recategorización de enero y julio, la baja si cerrás y el paso a responsable inscripto si tu facturación lo pide. <!-- A CONFIRMAR: servicios del estudio --></p>')],
       faq=[('¿Qué pasa si me paso del tope de la K?', 'Quedás afuera del monotributo y pasás al régimen general: IVA y Ganancias. Conviene verlo antes de que pase, con tus números.'),
            ('¿Cuándo vence la cuota?', 'El 20 de cada mes, para todas las terminaciones de CUIT. Si cae feriado o fin de semana, se corre al día hábil siguiente.'),
            ('¿Un productor agropecuario puede ser monotributista?', 'Sí, mientras lo que factura no pase el tope. Lo vemos con tus liquidaciones de granos y de hacienda.')],
       related=[('Vencimientos', 'vencimientos/', 'Las fechas de tu CUIT este mes'), ('Soluciones', 'soluciones/', 'Lo que resolvemos en el estudio'), ('Sueldos y aguinaldo', 'sueldos/', 'El neto y el aguinaldo de diciembre')],
       say='Escribinos y revisamos tu categoría antes de la recategorización de enero.'),

  dict(slug='sueldos', band=[('tractor-al-anochecer.jpg','Tractor trabajando un lote al anochecer'),('libro-contable-antiguo.jpg','Libro contable abierto sobre un escritorio de madera'),('vainas-de-soja.jpg','Vainas de soja en la planta')], crumb='Sueldos y aguinaldo', og='Sueldos y aguinaldo · Estudio Larumbe',
       title='Sueldos, aguinaldo y formulario 931 en Coronel Suárez | Estudio Larumbe',
       desc='Calculá el sueldo neto y el aguinaldo de diciembre de tus empleados. El Estudio Larumbe liquida sueldos de comercio y de peones rurales y presenta el F.931.',
       h1=['Sueldos', 'y aguinaldo'], lead='Liquidamos los sueldos de tu comercio o de tu campo todos los meses y presentamos el formulario 931. Acá podés calcular el neto de un sueldo y el aguinaldo de diciembre.',
       chips=['Aguinaldo: hasta el 18 de diciembre', 'F.931 todos los meses', 'Comercio y peones rurales'],
       wa='Hola Mariano, quiero consultar por la liquidación de sueldos.', tool_id='calculadora', tool_link='Calcular sueldo y aguinaldo',
       img='revision-de-formulario.jpg', img_w=2000, img_h=1333, img_alt='Dos personas revisando un formulario sobre un escritorio',
       summary=[('Descuentos al empleado', '17 %: jubilación 11 %, Ley 19.032 (PAMI) 3 % y obra social 3 %, más el sindicato si corresponde.'),
                ('Formulario 931', 'Todos los meses. En noviembre de 2026 vence el 11, el 12 o el 13 según tu CUIT.'),
                ('Aguinaldo', 'Dos cuotas por año: hasta el 30 de junio y hasta el 18 de diciembre. Es la mitad del mejor sueldo del semestre.'),
                ('Personal rural', 'Su propio régimen: el de Trabajo Agrario, Ley 26.727, con sus convenios.')],
       tool=TOOL_SUELDO,
       sections=[('Cómo se calcula el aguinaldo', '<p>Es la mitad del mejor sueldo bruto que cobró el empleado en el semestre. Si no trabajó el semestre completo, se paga en proporción a lo trabajado. Lleva los mismos descuentos que el sueldo.</p><p>La cuota de diciembre se paga hasta el 18. Te la dejamos liquidada antes, con los recibos listos para firmar.</p>'),
                 ('Lo que hacemos', '<p>Alta temprana de cada empleado, recibos de sueldo, aguinaldo, vacaciones, liquidaciones finales y el formulario 931 de cada mes, para comercio y para peones rurales. <!-- A CONFIRMAR: servicios del estudio --></p>')],
       faq=[('¿El aguinaldo tiene descuentos?', 'Sí, los mismos que el sueldo: jubilación, PAMI, obra social y sindicato si corresponde.'),
            ('¿Qué necesito para tomar a alguien?', 'Su CUIL, darlo de alta en ARCA antes de que empiece a trabajar y tener la ART contratada. El alta la hacemos nosotros.'),
            ('¿Liquidan peones rurales?', 'Sí, con el régimen de Trabajo Agrario y su convenio. <!-- A CONFIRMAR -->')],
       related=[('Campo', 'campo/', 'Arrendamiento en quintales y papeles de la campaña'), ('Vencimientos', 'vencimientos/', 'Las fechas de tu CUIT este mes'), ('Soluciones', 'soluciones/', 'Lo que resolvemos en el estudio')],
       say='Pasanos los recibos de este mes y te dejamos el aguinaldo liquidado.'),

  dict(slug='campo', band=[('cosechadora-en-trigo.jpg','Cosechadora levantando trigo en un lote'),('vainas-de-soja.jpg','Vainas de soja en la planta'),('tractor-al-anochecer.jpg','Tractor trabajando un lote al anochecer')], crumb='Productores agropecuarios', og='Contador para productores agropecuarios · Estudio Larumbe',
       title='Contador para productores agropecuarios en Coronel Suárez | Estudio Larumbe',
       desc='Liquidaciones de granos, SISA, arrendamientos en quintales, hacienda y peones rurales. Calculá tu arrendamiento en pesos y mandale al estudio la lista de papeles de la campaña.',
       h1=['Campo'], lead='Granos, hacienda, arrendamientos y el SISA, junto con los impuestos de todos los meses. Para productores de Coronel Suárez y la zona.',
       chips=['SISA', 'Liquidaciones de granos', 'Arrendamientos en quintales'],
       wa='Hola Mariano, tengo campo y quiero consultar.', tool_id='calculadora', tool_link='Calcular el arrendamiento',
       img='espigas-de-trigo.jpg', img_w=2000, img_h=1333, img_alt='Espigas de trigo a contraluz',
       summary=[('SISA', 'El Sistema de Información Simplificado Agrícola de ARCA. Todo el que produce granos tiene que estar inscripto.'),
                ('Granos', 'Cada venta llega con su liquidación y sus retenciones, que se cruzan con el IVA del mes.'),
                ('Arrendamientos', 'El contrato se registra en ARCA y lo que se cobra va en tu declaración, aunque se pague en quintales.'),
                ('Hacienda', 'Cada movimiento lleva su documento de tránsito y se valúa a fin de año para Ganancias y Bienes Personales.')],
       tool=TOOL_CAMPO,
       sections=[('Lo que hacemos para el campo', '<p>Alta y actualización en el SISA, el IVA de cada mes con tus liquidaciones de granos y retenciones, los contratos de arrendamiento registrados, Ganancias y Bienes Personales con el campo, la hacienda y el cereal valuados, y los sueldos de peones rurales. <!-- A CONFIRMAR: servicios del estudio --></p><p>Si el campo está a nombre de una sociedad, llevamos también sus libros y el balance.</p>')],
       faq=[('¿Qué es el estado en el SISA?', 'Es la calificación que te da ARCA según tu información. Define, entre otras cosas, cuánto te retienen de IVA cuando vendés granos. Por eso conviene tenerlo al día.'),
            ('Cobro el arrendamiento en quintales. ¿Cómo lo declaro?', 'Lo pasamos a pesos con el valor de cada pago y va en tu declaración. Guardá el comprobante de cada cobro.'),
            ('¿Me sirven las fotos de las liquidaciones?', 'Sí. Mandalas por WhatsApp como las tengas y las cruzamos con lo que ARCA ya tiene cargado.')],
       related=[('Sueldos y aguinaldo', 'sueldos/', 'Peones rurales y aguinaldo de diciembre'), ('Vencimientos', 'vencimientos/', 'Las fechas de tu CUIT este mes'), ('Monotributo', 'monotributo/', 'Calculá tu categoría y tu cuota')],
       say='Traé la carpeta de la campaña o mandala en fotos: lo que falte, te lo pedimos.'),

  dict(slug='vencimientos', band=[('estacion-coronel-suarez.jpg','La estación de tren de Coronel Suárez'),('libro-contable-antiguo.jpg','Libro contable abierto sobre un escritorio de madera'),('espigas-de-trigo.jpg','Espigas de trigo a contraluz')], crumb='Vencimientos', og='Vencimientos de ARCA por CUIT · Estudio Larumbe',
       title='Vencimientos de ARCA de noviembre 2026 por CUIT | Estudio Larumbe',
       desc='Tocá el último número de tu CUIT y mirá qué vence en noviembre de 2026: IVA, monotributo, autónomos, empleadores y Ganancias. Fechas de la agenda oficial de ARCA.',
       h1=['Vencimientos', 'de ARCA'], lead='Las fechas de noviembre de 2026 para tu CUIT, copiadas de la agenda oficial. Las cargamos de nuevo cada mes.',
       chips=['Monotributo: el 20', 'IVA: del 18 al 25', 'Autónomos: 5, 11 o 12'],
       wa='Hola Mariano, quiero que me avisen mis vencimientos.', tool_id='calculadora', tool_link='Ver mis fechas',
       img='silos-y-cielo.jpg', img_w=2000, img_h=1236, img_alt='Silos de chapa bajo un cielo con nubes',
       summary=[('IVA', 'Del 18 al 25 de noviembre, según la terminación del CUIT.'),
                ('Monotributo', 'Viernes 20 de noviembre, para todos.'),
                ('Autónomos', 'Jueves 5 (CUIT 0 a 3), miércoles 11 (4 a 6) o jueves 12 (7 a 9).'),
                ('Empleadores (F.931)', 'Miércoles 11 (CUIT 0 a 3), jueves 12 (4 a 6) o viernes 13 (7 a 9).'),
                ('Ingresos Brutos (ARBA)', 'Lorem ipsum <!-- A CONFIRMAR -->')],
       tool=TOOL_VENC,
       sections=[('Cómo se paga', '<p>Cada vencimiento se paga con un VEP, el Volante Electrónico de Pago: se genera en ARCA y se paga desde el home banking o la billetera del banco. Te lo mandamos armado por WhatsApp con el monto y la fecha.</p>')],
       faq=[('¿Qué pasa si pago tarde?', 'Se cobran intereses resarcitorios por cada día de atraso. Si además no presentaste la declaración, puede haber multa.'),
            ('¿Qué es el VEP?', 'El Volante Electrónico de Pago. Lo generás en ARCA y lo pagás desde el home banking. Si querés, te lo armamos nosotros.'),
            ('¿Cada cuánto actualizan las fechas?', 'Todos los meses, apenas ARCA publica la agenda.')],
       related=[('Monotributo', 'monotributo/', 'Calculá tu categoría y tu cuota'), ('Sueldos y aguinaldo', 'sueldos/', 'El 931 y el aguinaldo de diciembre'), ('Soluciones', 'soluciones/', 'Lo que resolvemos en el estudio')],
       say='Pasanos tu CUIT y te avisamos antes de cada vencimiento.'),
]
