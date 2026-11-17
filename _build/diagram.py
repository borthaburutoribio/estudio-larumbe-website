# Genera los dos SVG del diagrama "papeles sueltos -> carpeta -> presentado".
import random
random.seed(449)
N=48; S=12
def wide():
    out=[]
    for i in range(N):  # dispersos
        x=random.uniform(10,360); y=random.uniform(12,250); r=random.uniform(-35,35)
        c='var(--sq-a)' if i%2 else 'var(--sq-b)'
        out.append(f'<rect class="sq s1" x="{x:.0f}" y="{y:.0f}" width="{S}" height="{S}" fill="{c}" transform="rotate({r:.0f} {x+6:.0f} {y+6:.0f})"/>')
    for i in range(N):  # cinta de 3 filas
        col=i//3; row=i%3
        x=420+col*22.5; y=117+row*14
        out.append(f'<rect class="sq s2" x="{x:.0f}" y="{y:.0f}" width="{S}" height="{S}" fill="var(--sq-c)"/>')
    for i in range(N):  # filas ordenadas
        col=i%8; row=i//8
        x=830+col*46; y=24+row*40
        out.append(f'<rect class="sq s3" x="{x:.0f}" y="{y:.0f}" width="{S}" height="{S}" fill="var(--sq-d)"/>')
    return '<svg class="diagram diagram-wide" viewBox="0 0 1200 270" role="img" aria-label="Papeles sueltos a la izquierda, juntos en una carpeta en el medio y ordenados en filas a la derecha">'+''.join(out)+'</svg>'
def tall():
    random.seed(449); out=[]
    for i in range(N):
        x=random.uniform(8,250); y=random.uniform(8,140); r=random.uniform(-35,35)
        c='var(--sq-a)' if i%2 else 'var(--sq-b)'
        out.append(f'<rect class="sq s1" x="{x:.0f}" y="{y:.0f}" width="{S}" height="{S}" fill="{c}" transform="rotate({r:.0f} {x+6:.0f} {y+6:.0f})"/>')
    for i in range(N):
        row=i//3; col=i%3
        x=112+col*14; y=168+row*9.5
        out.append(f'<rect class="sq s2" x="{x:.0f}" y="{y:.0f}" width="{S}" height="{S}" fill="var(--sq-c)"/>')
    for i in range(N):
        col=i%6; row=i//6
        x=14+col*44; y=350+row*20
        out.append(f'<rect class="sq s3" x="{x:.0f}" y="{y:.0f}" width="{S}" height="{S}" fill="var(--sq-d)"/>')
    return '<svg class="diagram diagram-tall" viewBox="0 0 270 520" role="img" aria-label="Papeles sueltos arriba, juntos en una carpeta en el medio y ordenados en filas abajo">'+''.join(out)+'</svg>'
html=open('index.html',encoding='utf-8').read()
import re
html=re.sub(r'<!--DIAGRAMA-->.*?<!--/DIAGRAMA-->','<!--DIAGRAMA-->'+wide()+tall()+'<!--/DIAGRAMA-->',html,flags=re.S)
open('index.html','w',encoding='utf-8').write(html)
print('ok')
