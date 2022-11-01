#import
from cProfile import label
from cmath import sqrt
from ipaddress import v6_int_to_packed
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
import matplotlib.pyplot as plt 
import numpy as np 

#Introducción
print("Simulador Riel y esfera, el programa mostrará el valor del alcance max que va a obtener la esfera")
print("El simulador, pide los datos de Altura 1 (h1), Altura 2 (h2), Altura 3 (h3) la cual corresponde a el punto de salida de la esfera.")
print("Los valores de la gravedad, y ángulo de inclinación de salida.")
print("por ultimo solicita el tiempo, si no se tiene, poner 0")
print("y por ultimo se solicita el valor de la Volocidad inicial, si no se tiene, poner 0 ")
print("para cualquier valor no poseido, poner 0 en la variable")

# Datos
try: 
    h1 = float(input("Ingresa valor de la altura en el punto A, en cm: "))
    h2 = float(input("Ingresa valor de la altura en el punto B, en cm: "))
    h3 = float(input("Ingresa valor de la altura del suelo a donde está la base del riel, en cm: "))    
    g = float(input("Ingresa el valor de la gravedad a usar, en m/s^2: "))
    t = float(input("Ingresa el valor del tiempo,en segundos: "))
    vi = float(input("Ingrese valor de la velocidad inicial, en m/s, en el punto B:  "))
    xi = float(input("ingresa el valor de la posicón inicial desde el punto B(cm en eje x): "))
    xf = float(input("Ingresa el valor de la posicón final(metros en eje x ): "))
    angulo = float(input("ingrese el angulo de salida en B: "))
    
    Hi = h2
    Hf = float(input("Ingrese el valor de la altura final de la caida(metros): "))
    
    if g == None:
        g = 9.87
    
    if Hi == None:
        Hi = 0
    
    if xi == None:
        xi = 0
    
    if Hf == None:
        Hf = 0
    
    if angulo == None:
        angulo = 45   
  
    # se requiere el tiempo de caída de la esfera entonces
    
    if t == None:
        t = 0
        
    alpha = ((angulo* np.pi)/180)
    
    #Primero calcular velocidad de salida, de no poseerla
    # V = vi = sqrt((10/7)*(g)*(h1 - h2))
    V = vi    
    if V == 0 or V == None:
        V = (g*t)/2*np.sin(alpha)
    
    #Ahora con la velocidad en el riel, determinar el alcance maximo de la esfera
    #por tiro parabolico
        
    raiz = (((vi**2)*(np.sin(alpha)**2)) - (2*g*Hf) + (2*g*Hi))
    
    if raiz < 0:
        print("\n NO ES POSIBLE CALCULAR UNA PARABOLA CON LOS DATOS INGRESADOS. \n INTENTA CON OTROS VALORES")
    
    else:
        
        t2 = (((V*np.sin(alpha)) + (np.sqrt(((V**2)*(np.sin(alpha)**2)) - (2*g*Hf) + (2*g*Hi)))) / g)
        t = np.arange(0, t2+t2/50, t2/50)
        
        Vx = V*np.cos(alpha)
        X =(xi + (Vx*t))
        Xmax = (((V**2)*(2*np.cos(alpha)*np.sin(alpha))) / g)
        
        Vy = ((V*np.sin(alpha)) - (g*t))
        Y = h1+h3
        Ymax = ((((V**2)*(np.sin(alpha)**2)) / (2*g)) + Hi)
        
        tHmax = ((V*np.sin(alpha))/g)
        xHmax = V*np.cos(alpha)*t
        
        tXmax = t2
        xXmax = V*np.cos(alpha)*t
        
        fig, ax = plt.subplots(1,1, figsize = (15,5))
        ax.plot(X, Y,'k--',lw=3)
        ax.set_title("Trayectoria (x,y)", fontsize=25)
        ax.set_xlabel('x [cm]', fontsize=16)
        ax.set_ylabel('y [cm]', fontsize=16)
        ax.grid(True, which='both')
        ax.plot(xHmax,Ymax,'s',lw=4, label = (f'Altura Max: ({np.round(xHmax,2)}, {np.round(Ymax,2)})'))
        ax.plot(xXmax,Hf,'o',lw=4, label=f'Distancia Max: ({np.round(xXmax,2)}, {Hf})')
        ax.plot(xi,Hi,'v',lw=4,label=f'Posicion Inicial: ({xi}, {Hi})')
        ax.plot(lw=4,label=f'Velocidad Generada: ({np.round(V, 2)})')
        ax.legend()
        
        fig.show()  
except(exception):
    print(exception)    
    print("No se puede calcular el alcance del proyectil")
    
    

#Interfaz
ventana = tkinter.Tk()
ventana.mainloop()

    