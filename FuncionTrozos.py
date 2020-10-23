# !/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
Juan Sebastian Castrillon Pulido
Universidad de la Rioja
Fundamentos de programacion
Oct 22, 2020
"""
print('\nFuncion definida por tramos\n')
print('y = 100x si	x<0')
print('y = 2x+5	si  0<=x<3')
print('y = 100/x si 3<=x<=6')
print('y = 0 En otro caso')
x = float(input('\nIngrese el valor de referencia x = '))
if x<0:
    y = 100*x
elif 0<=x and x<3:
    y = 2*x+5
elif 3<=x and x<=6:
    y = 100/x
else:
    y = 0
print('y =',y)
