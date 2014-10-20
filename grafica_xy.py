#          PyGal
#     www.soyteleco.net
#  joan.bono@soyteleco.net

import pygal
from math import *

grafica_xy=pygal.XY()
grafica_xy.title='tan(a) & cos(b)'
grafica_xy.add('x = cos(y)', [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)])
grafica_xy.add('y = tan(x)', [(x / 10., tan(x / 10.)) for x in range(-50, 50, 5)])

grafica_xy.render_to_file('grafica_xy.svg')
