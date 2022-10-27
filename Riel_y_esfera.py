from cProfile import label
from logging import exception
import tkinter
from tkinter.ttk import LabeledScale,Frame
from tkinter import Button, Label, ttk
from turtle import color
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json

try: 
    h1 = float(input("Ingresar altura inicial del riel: "))
    h2 = float(input("Ingrese valor de la altura "))
except(exception):
    print(exception)
    print("No se puede calcular los datos solicitados, y generar la gráfica")
