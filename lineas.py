#          PyGal
#     www.soyteleco.net
#  joan.bono@soyteleco.net

import pygal

grafica_lineas=pygal.Line()
grafica_lineas.title='Evolucion de Notas por anyos'
grafica_lineas.x_labels=map(str,range(7,20))
grafica_lineas.add('Matematicas',[10,9,8,7,7,7,8,7.5,9,10,10,9,5,3])
grafica_lineas.add('Programacion',[None,None,None,None,None,None,None,None,None,None,None,7,6])
grafica_lineas.add('Ingles',[10,9,5,7,3,5,8,4,6,8,8,6,4,0,8,6,3,1,10])
grafica_lineas.add('Otras',[2.6,5,5,8,2,5.5,7,2,2,4,3,6])

grafica_lineas.render_to_file('lineas.svg')
