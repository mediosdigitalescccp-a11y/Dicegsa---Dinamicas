# Genera datos.js con los bloques de la hoja "Data fármacos dinámicas 2026" (pestaña Data_FB_Ads, desde la columna CU).
# Uso: python3 datos/build_data.py
import json, os
D0 = os.path.dirname(os.path.abspath(__file__))
REG = {'Región Autónoma del Atlántico Norte': 'RACCN', 'Región Autónoma del Atlántico Sur': 'RACCS', 'Unknown': 'Desconocido'}
reg = lambda x: REG.get(x, x.replace(' Department', ''))
GEN = {'female': 'Mujer', 'male': 'Hombre', 'unknown': 'Desconocido'}
# diario: fecha alcance impresiones interacciones me_gusta_pagina comentarios cpm
# cre: fecha anuncio alcance impresiones
# resumen (Frec Nuevo, CPM Nuevo, Reach Nuevo) tal cual la hoja
M = [
 dict(marca='Neurobion', campana='FARMACO_NEUROBION_ENG_NOV_2026', alcance=7960, frecuencia=1.78, cpm=1.28,
  diario="""2026-11-07 1347 1626 254 0 14 1.46
2026-11-08 2474 3130 415 1 22 1.44
2026-11-09 1751 2213 283 0 7 1.55
2026-11-10 2367 2945 280 2 6 1.19
2026-11-11 2778 3296 253 0 6 1.00
2026-11-12 881 950 69 0 2 1.07""",
  cre="""2026-11-12 FB 415 434
2026-11-12 IG 484 516
2026-11-11 FB 1875 2143
2026-11-11 IG 979 1153
2026-11-10 FB 1716 2010
2026-11-10 IG 829 935
2026-11-09 FB 1078 1235
2026-11-09 IG 788 978
2026-11-08 FB 1303 1526
2026-11-08 IG 1386 1604
2026-11-07 FB 596 710
2026-11-07 IG 814 916""",
  gen=[('female', 4639), ('male', 3316), ('unknown', 27)],
  edad=[('18-24', 2423), ('25-34', 2311), ('35-44', 1380), ('45-54', 785), ('55-64', 609), ('65+', 585)],
  reg=[('Managua Department', 3125), ('Región Autónoma del Atlántico Norte', 706), ('Masaya Department', 656), ('Matagalpa Department', 478), ('León Department', 469), ('Chinandega Department', 414)]),
 dict(marca='Cebión', campana='FARMACO_CEBION_ENG_NOV_2026', alcance=14651, frecuencia=1.53, cpm=1.05,
  diario="""2026-11-16 2057 2530 384 - 28 1.65
2026-11-17 4100 4910 477 - 33 1.32
2026-11-18 6606 7496 512 - 75 0.90
2026-11-19 6713 7427 384 - 58 0.80""",
  cre="""2026-11-19 FB 2980 3197
2026-11-19 IG 3999 4230
2026-11-18 FB 2807 2999
2026-11-18 IG 4251 4497
2026-11-17 FB 2530 2927
2026-11-17 IG 1813 1983
2026-11-16 FB 1191 1394
2026-11-16 IG 961 1136""",
  gen=[('female', 10730), ('male', 3745), ('unknown', 55)],
  edad=[('18-24', 2898), ('25-34', 3771), ('35-44', 2474), ('45-54', 1670), ('55-64', 2007), ('65+', 1867)],
  reg=[('Managua Department', 6383), ('Masaya Department', 1292), ('León Department', 983), ('Chinandega Department', 786), ('Región Autónoma del Atlántico Norte', 763), ('Matagalpa Department', 683)]),
 dict(marca='Lubriderm', campana='FARMACO_LUBRIDERM_ENG_NOV_2026', alcance=14304, frecuencia=1.2, cpm=0.86,
  diario="""2026-11-20 5 5 2 - 0 0
2026-11-21 2775 2943 2271 - 8 0.97
2026-11-22 3646 3929 2947 - 7 1.02
2026-11-23 4867 5127 3444 - 14 0.73
2026-11-24 3818 4003 2892 - 9 0.82
2026-11-25 1036 1116 674 - 2 0.77""",
  cre="""2026-11-25 FB 174 184
2026-11-25 IG 881 932
2026-11-24 FB 826 857
2026-11-24 IG 3047 3146
2026-11-23 FB 434 451
2026-11-23 IG 4492 4676
2026-11-22 FB 450 482
2026-11-22 IG 3177 3447
2026-11-21 FB 975 1049
2026-11-21 IG 1789 1894
2026-11-20 FB 5 5""",
  gen=[('female', 9769), ('male', 4080), ('unknown', 60)],
  edad=[('18-24', 1811), ('25-34', 2479), ('35-44', 2344), ('45-54', 2206), ('55-64', 2715), ('65+', 2428)],
  reg=[('Managua Department', 5472), ('León Department', 1095), ('Masaya Department', 909), ('Chinandega Department', 893), ('Matagalpa Department', 806), ('Estelí Department', 692)]),
]
out = []
for m in M:
    dia = []
    for l in m['diario'].split('\n'):
        f, a, i, e, lk, c, cpm = l.split()
        dia.append(dict(fecha=f, alcance=int(a), impresiones=int(i), interacciones=int(e), likes=None if lk == '-' else int(lk), comentarios=int(c), cpm=float(cpm)))
    cre = [dict(fecha=f, red=r, alcance=int(a), impresiones=int(i)) for f, r, a, i in (l.split() for l in m['cre'].split('\n'))]
    assert sum(d['impresiones'] for d in dia) == sum(c['impresiones'] for c in cre), m['marca']
    out.append(dict(marca=m['marca'], campana=m['campana'], alcance=m['alcance'], frecuencia=m['frecuencia'], cpm=m['cpm'], diario=dia, creativos=cre,
        genero=[dict(seg=GEN[k], v=v) for k, v in m['gen']], edad=[dict(seg=k, v=v) for k, v in m['edad']], region=[dict(seg=reg(k), v=v) for k, v in m['reg']]))
data = dict(dinamicas=out, actualizado=max(d['fecha'] for m in out for d in m['diario']))
open(os.path.join(D0, '..', 'datos.js'), 'w', encoding='utf-8').write('window.DN_DATA = ' + json.dumps(data, ensure_ascii=False) + ';\n')
print({m['marca']: sum(d['impresiones'] for d in m['diario']) for m in out})
