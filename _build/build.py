# Genera las páginas internas del sitio y comparte barra, pie y scripts con la home.
# Uso: python -I _build/build.py   (desde la carpeta del sitio)
# Todo el texto de las páginas internas está en _build/content.py.
import re, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / '_build'))
from content import PAGES, SITE, WA, WA_TXT, NAV  # noqa: E402

V = '5'  # versión de css/js (el preview cachea)


def wa(text):
    from urllib.parse import quote
    return f'https://wa.me/{WA}?text={quote(text)}'


def header(px):
    links = ''.join(f'<li><a href="{px}{u}">{t}</a></li>' for t, u in NAV)
    return f'''<header class="bar">
  <a class="wordmark" href="{px or './'}" aria-label="Estudio Larumbe, inicio">
    <span class="wm-name">Larumbe</span>
    <span class="wm-sub">Estudio contable</span>
  </a>
  <nav class="nav" aria-label="Secciones">
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu">Menú</button>
    <ul id="menu" class="nav-list">{links}</ul>
  </nav>
  <a class="btn btn-ink bar-cta" href="{wa(WA_TXT)}" target="_blank" rel="noopener">WhatsApp</a>
</header>'''


def footer(px):
    col1 = ''.join(f'<li><a href="{px}{u}">{t}</a></li>' for t, u in NAV[:3])
    col2 = ''.join(f'<li><a href="{px}{u}">{t}</a></li>' for t, u in NAV[3:])
    return f'''<footer class="foot">
  <p class="foot-name" aria-hidden="true">Larumbe</p>
  <div class="foot-row">
    <ul class="foot-places">
      <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
      <li><a href="tel:+542926422292">(02926) 42-2292</a></li>
      <li><a href="https://maps.google.com/?q=Sarmiento+449,+Coronel+Su%C3%A1rez" target="_blank" rel="noopener">Sarmiento 449</a></li>
    </ul>
    <div class="foot-cols">
      <ul>{col1}</ul>
      <ul>{col2}<li><button type="button" class="share" id="share">Compartir</button></li></ul>
      <p class="credits">Fotos: Facu.Morando (estación, CC BY-SA 4.0) y Roberto Pampa (afueras de Coronel Suárez, CC BY-SA 3.0), vía Wikimedia Commons; el resto, Unsplash; video de trigo, Pexels. Todas con tratamiento de color propio.</p>
    </div>
  </div>
  <div class="foot-legal">
    <p>Estudio Contable Mariano A. Larumbe · Coronel Suárez · Sitio de muestra hecho por Tranquera Digital</p>
    <a href="#inicio">Volver arriba</a>
  </div>
</footer>

<a class="wa-fab" href="{wa(WA_TXT)}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">WhatsApp</a>'''


def scripts(px, extra=()):
    tags = [f'<script src="{px}vencimientos.js?v={V}"></script>', f'<script src="{px}script.js?v={V}"></script>']
    tags += [f'<script src="{px}{e}?v={V}"></script>' for e in extra]
    return '\n'.join(tags)


def faq_html(items):
    bands = ''.join(f'<div class="faq-band"><h3 class="q">{q}</h3><p class="a">{a}</p></div>' for q, a in items)
    return f'<section class="faq" id="preguntas" aria-labelledby="q-title"><div class="faq-band faq-head"><h2 id="q-title" class="faq-title rise">Preguntas</h2></div>{bands}</section>'


def faq_schema(items):
    strip = lambda t: re.sub('<[^>]+>', '', t)
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in items]}


def page(p):
    px = '../'
    url = f"{SITE}{p['slug']}/"
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": p['crumb'], "item": url}]}
    service = {"@context": "https://schema.org", "@type": "Service", "name": p['crumb'], "serviceType": p['crumb'],
               "provider": {"@type": "AccountingService", "name": "Estudio Contable Mariano A. Larumbe", "telephone": "+54 2926 42-2292",
                            "address": {"@type": "PostalAddress", "streetAddress": "Sarmiento 449", "addressLocality": "Coronel Suárez", "postalCode": "7540", "addressRegion": "Buenos Aires", "addressCountry": "AR"}},
               "areaServed": "Partido de Coronel Suárez"}
    ld = [crumbs, service] + ([faq_schema(p['faq'])] if p.get('faq') else [])
    ld_html = '\n'.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    chips = ''.join(f'<li>{c}</li>' for c in p['chips'])
    summary = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in p['summary'])
    sections = ''.join(f'<section class="txt" aria-labelledby="s-{i}"><h2 id="s-{i}" class="h-head rise">{h}</h2><div class="txt-body rise">{body}</div></section>' for i, (h, body) in enumerate(p['sections']))
    band = '<section class="band" aria-label="Fotos">' + ''.join(f'<figure><img src="{px}assets/img/{f}" alt="{a}" loading="lazy" decoding="async"></figure>' for f, a in p['band']) + '</section>'
    related = ''.join(f'<li><a href="{px}{u}"><span>{t}</span><span class="rel-d">{d}</span></a></li>' for t, u, d in p['related'])
    html = f'''<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<!-- Sitio de muestra: no indexar hasta que el estudio lo apruebe -->
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{p['og']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:image" content="{SITE}assets/img/{p['img']}">
<meta property="og:locale" content="es_AR">
<meta name="theme-color" content="#14275a">
<link rel="icon" href="{px}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://api.fontshare.com">
<link rel="preconnect" href="https://cdn.fontshare.com" crossorigin>
<link href="https://api.fontshare.com/v2/css?f[]=boska@400,500&f[]=switzer@400,500,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{px}styles.css?v={V}">
{ld_html}
</head>
<body class="sub">
<a class="skip" href="#contenido">Ir al contenido</a>
<!--HEADER--><!--/HEADER-->
<main id="contenido">
<section class="ph" id="inicio">
  <div class="ph-text">
    <h1 class="ph-title"><span class="line"><span>{p['h1'][0]}</span></span>{f'<span class="line"><span>{p["h1"][1]}</span></span>' if len(p['h1']) > 1 else ''}</h1>
    <p class="standfirst reveal-late">{p['lead']}</p>
    <ul class="chips reveal-late">{chips}</ul>
    <div class="hero-actions reveal-late">
      <a class="btn btn-ink" href="{wa(p['wa'])}" target="_blank" rel="noopener">Consultá por WhatsApp</a>
      <a class="link" href="#{p['tool_id']}">{p['tool_link']}</a>
    </div>
  </div>
  <figure class="ph-img"><img src="{px}assets/img/{p['img']}" width="{p['img_w']}" height="{p['img_h']}" alt="{p['img_alt']}" fetchpriority="high"></figure>
</section>

<section class="sum" aria-labelledby="sum-t">
  <h2 id="sum-t" class="h-head rise">En resumen</h2>
  <table class="sum-table rise"><tbody>{summary}</tbody></table>
</section>

{p['tool']}

{band}

{sections}

{faq_html(p['faq'])}

<section class="rel" aria-labelledby="rel-t">
  <h2 id="rel-t" class="h-head rise">Seguí por acá</h2>
  <ul class="rel-list">{related}</ul>
</section>

<section class="contact" id="contacto" aria-labelledby="k-title">
  <h2 id="k-title" class="sr">Contacto</h2>
  <p class="contact-say rise">{p['say']}</p>
  <figure class="contact-pic"><img src="{px}assets/img/calculadora-y-lapicera.jpg" width="2000" height="1333" alt="Calculadora y lapicera sobre una hoja con cuentas" loading="lazy" decoding="async"></figure>
  <div class="contact-links">
    <p class="contact-q">¿Hablamos?</p>
    <a class="ulink" href="{wa(p['wa'])}" target="_blank" rel="noopener">WhatsApp 2926 41-2120</a>
    <a class="ulink" href="tel:+542926422292">Fijo (02926) 42-2292</a>
    <p class="contact-small">Sarmiento 449, Coronel Suárez. Horario: Lorem ipsum.</p>
  </div>
</section>
</main>
<!--FOOTER--><!--/FOOTER-->
<!--SCRIPTS--><!--/SCRIPTS-->
</body>
</html>
'''
    return html


def fill(html, px, extra=()):
    html = re.sub(r'<!--HEADER-->.*?<!--/HEADER-->', lambda m: '<!--HEADER-->' + header(px) + '<!--/HEADER-->', html, flags=re.S)
    html = re.sub(r'<!--FOOTER-->.*?<!--/FOOTER-->', lambda m: '<!--FOOTER-->' + footer(px) + '<!--/FOOTER-->', html, flags=re.S)
    html = re.sub(r'<!--SCRIPTS-->.*?<!--/SCRIPTS-->', lambda m: '<!--SCRIPTS-->' + scripts(px, extra) + '<!--/SCRIPTS-->', html, flags=re.S)
    return html


def main():
    for p in PAGES:
        d = ROOT / p['slug']; d.mkdir(exist_ok=True)
        (d / 'index.html').write_text(fill(page(p), '../', ('tools.js',)), encoding='utf-8')
        print('ok', p['slug'])
    home = ROOT / 'index.html'
    h = home.read_text(encoding='utf-8')
    h = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={V}', h)
    home.write_text(fill(h, '', ('tools.js',)), encoding='utf-8')
    urls = [SITE] + [f"{SITE}{p['slug']}/" for p in PAGES]
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                                      ''.join(f'  <url><loc>{u}</loc><lastmod>2026-11-16</lastmod></url>\n' for u in urls) + '</urlset>\n', encoding='utf-8')
    print('ok home + sitemap')


if __name__ == '__main__':
    main()
