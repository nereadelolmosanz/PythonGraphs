#          PyGal
#     www.soyteleco.net
#  joan.bono@soyteleco.net

import pygal

barra_horizontal=pygal.HorizontalBar()
barra_horizontal.title='Temperatura Raspberry Pi'
barra_horizontal.add('Junio',41.6)
barra_horizontal.add('Julio',51.7)
barra_horizontal.add('Agosto',59.4)
barra_horizontal.add('Septiembre',47.2)
barra_horizontal.add('Octubre',48.6)

barra_horizontal.render_to_file('barra_horizontal.svg')
