# !/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
Juan Sebastian Castrillon Pulido
juansebastian.castrillon772@comunidadunir.net
Universidad de la Rioja
Fundamentos de programacion
Oct 15, 2020
"""
codigoalumno = input("Cuál es el código del alumno ")
nota1 = float(input("Ingrese la nota 1 "))
nota2 = float(input("Ingrese la nota 2 "))
nota3 = float(input("Ingrese la nota 3 "))
nota4 = float(input("Ingrese la nota 4 "))
nota5 = float(input("Ingrese la nota 5 "))
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print("La nota del estudiante ", codigoalumno, "\nEs: ", promedio)
