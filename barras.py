#          PyGal
#     www.soyteleco.net
#  joan.bono@soyteleco.net

import pygal

grafica_barras=pygal.Bar()
grafica_barras.title='Evolucion de Notas por anyos'
grafica_barras.x_labels=map(str,range(7,20))
grafica_barras.add('Matematicas',[10,9,8,7,7,7,8,7.5,9,10,10,9,5,3])
grafica_barras.add('Programacion',[None,None,None,None,None,None,None,None,None,None,None,7,6])
grafica_barras.add('Ingles',[10,9,5,7,3,5,8,4,6,8,8,6,4,0,8,6,3,1,10])
grafica_barras.add('Otras',[2.6,5,5,8,2,5.5,7,2,2,4,3,6])

grafica_barras.render_to_file('barras.svg')
