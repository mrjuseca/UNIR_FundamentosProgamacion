# !/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
Juan Sebastian Castrillon Pulido
Universidad de la Rioja
Fundamentos de programacion
Oct 15, 2020
"""
print('     EJERCICIOS DE PROGRAMACION BÁSICOS\n')
print(' 1. (A+B)^2/3')
print(' 2. Orden inverso')
print(' 3. Mayor número')
print('23. Función por trozos')

ejercicio = int(input('\nSeleccione el número del ejercicio '))

if ejercicio == 1:
    exec(open('Potencia.py').read())
elif ejercicio == 2:
    exec(open('Inversion.py').read())
elif ejercicio == 3:
    exec(open('MayorQue.py').read())
elif ejercicio == 23:
    exec(open('FuncionTrozos.py').read())
else:
    print('Número no valido')
