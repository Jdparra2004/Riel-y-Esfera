from cmath import sqrt
import tkinter
import numpy as np
import matplotlib.pyplot as plt 
from math import sin, sqrt, pi
from math import *

'''
Inicio de programa.
Programa de calculo de variables fisicas, para el tiro parabolico de una esfera, después del recorrido de un proyectil,
en este caso una esfera.

Revisar documento de apoyo, y fundamentación de ecuaciones para el simulador.
https://drive.google.com/file/d/1wfrTL5agLeBVtpcMo1uygvN5063D9SE-/view?usp=sharing
tengasé en cuenta el paso a paso que se presenta en el documento
'''

#Bienvenida, y explicación programa al usuario
Bienvenida = "Bienvenido estudiante, con este simulador, podrás calcular el alcance máximo de una esfera"
Grafica = "La gráfica anterior es una guía del recorrido y datos que serán pedidos al usuario"
Funcionamiento ="Primero se tomará la velocidad de salida en B, mediante el dato dado, o el calculo, por conservación de energía,"
Tiro_parabolico = "con la velocidad en B y alturas, se calcular el recorrido de la esfera y su alcance máximo"
angulo_salida = "El angulo solicitado en el programa es el angulo que se forma en la salida de la curva  y el suelo, antes del punto B: "

#advertencias y aclaraciones
Datos_no_dados = "De no poseer algún dato, ingresar 0, el programa esta diseñado para calcularlos"
aclaracion = "Lo ideal es tener los datos basicos, como las alturas, y angulo, de no poseerlos, usar el programa como método experimental"
recordar = "El programa se diseña con fines de calculo y graficación base, auqnue se puede usar con fines academicos experimentales"

#Copyright
copy = "Este software es desarrollado con fines academicos, no  lucrativos, revisar nota README en fichero de GitHub"
link = "Copiar enlace: https://github.com/Jdparra2004/Riel-y-Esfera"

#Prints
print(Bienvenida)
print(Grafica, Funcionamiento, Tiro_parabolico, angulo_salida)
print(Datos_no_dados, aclaracion, recordar)
print(copy, link)
print("todos los datos deberán ser ingresados en metros, el uso decimales será con el punto")

#Datos pedidos al usuario y dados
hA = float(input("Ingresa el valor de la altura al punto A: "))
hB = float(input("Ingrese el valor de la altura al punto B: "))
h3 = float(input("Ingrese el valor de la altura del suelo a la base del riel: "))
g = float(input("Valor de la gravedad a usar: "))
v = float(input("Ingrese valor de la velocidad que se obtiene en el tramo AB(de no tenerlo, poner 0): "))
angulo = float(input("Ingrese el valor del angulo de salida en el punto B: "))
tmax = float(input("Ingrese el valor del tiempo de caida del proyectil desde el punto B(de no tenerlo, poner 0): "))
Xmax = float(input("Ingrese alcance max de la caida del proyectil,(valor a calcular, poner 0): "))
hf = float(input("Ingrese altura final del proyectil: "))
#Xi corresponderá a 0, dado que es el punto en el cuál sale la esfera del punto B
Xi = 0

#Funciones y operaciones mátematicas.
'''
Declarar funciones, y operaciones, tengasé en cuenta que pueden existir valores experimentales o no, dados en 0, revisar ejes de 
coordenadas, prioridad, que no den imaginarios con respecto al eje, y ejecutar "except".
el punto C será interpretado como el punto final de caida del tiro parabolico, pero tambíen el limite del eje Y hacía los negativos.
'''
try:
    #Tener en cuenta las condicionales de ciclo, y las ecuaciones afectadas por raiz y negativos
    #Revisar ecuaciones de documento de fundamentación en Drive
    #https://drive.google.com/file/d/1wfrTL5agLeBVtpcMo1uygvN5063D9SE-/view?usp=sharing
    '''
    Lo primero son las condicionales de valores para los datos solicitados al usuario
    Luego hallar la velocidad entre el tramo AB, mediante conservación de energía.
    '''
    #Condicionales de datos y demás, para hallar el alcance máximo.
    if hA == None: 
        hA = 0
    
    if hB == None: 
        hB = 0
    
    #si A es < que B en altura, la raiz de velocidad dará negativo, y no será posible calcular la velocidad
    if hA < hB:
        print("\nNo se puede ejecutar el software, dado que la velocidad no será la necesaria, para salir del riel en el punto B")
    
    #h3 es la altura del suelo, a la base del riel, la cual puede ser 0, pero se el limite de caida, para el eje Y
    if h3 == None:
        h3 = 0
        
    if hf == None:
        hf = 0
    
    #El angulo de salida puede ser cero, pero se ha de tener en cuenta la logica mátematica, y se define alpha, para la parte
    #operacional
    if angulo == None:
        angulo = 0
        
    alpha = ((angulo*pi)/180)
    
    if tmax == None:
        tmax = 0
    
    if g < 0:
        print("\nNO se puede desarrollar el simulador, dado que la gravedad es negativa")
    
    #Despejando velocidad mediante conservación se llega a la Velocidad.
    if v == None:
        v= sqrt((10/7) * g * (hA - hB)) 
    
    '''
    Ahora con la velocidad encontrada, por dinámica, hallar el Xmax, pero para esto, se requiere del tiempo de vuelo y otras variables.
    '''
    #Primero hallar el tiempo, teniendo en cuenta la ecuación cuadrática, teniendo en cuenta la raiz.
    #Y la altura a usar, va a ser hB + h3
    
    h = hB + h3
   
    
    #Este tiempo a calcular, es el tiempo de caida, del proyectil desde el punto B.
    #Else: desarrolla tiro parabolico.
    raiz_t = sqrt((v**2 * sin(alpha) + 2 * g *h))
    
    if raiz_t < 0:
        print("\nNo se puede calcular el tiempo de vuelo, dado que es una raiz negativa")
    #Tiempo de vuelo y gráficación
    else:
        #Hallar tiempo
        tmax2 = ((v * sin(alpha) + raiz_t)/180)
        #rango de tiempo
        t = np.arange(0, tmax2+tmax/50, tmax2/50)
        
        
        #Velocidad y alcance en X
        Vx = v*cos(alpha)
        X = (Xi + (Vx*t))
        Xmax = (((v**2)*(2*cos(alpha)*sin(alpha))) / g)
        
        #Velocidad y alcance en Y
        Vy = (v*sin(alpha) - (g*t))
        Y = (((v*sin(alpha)*t) - (0.5*g*t**2)) + h)
        Ymax = ((((v**2)*(sin(alpha)**2)) / (2*g)) + h)
        
        #tiempo de altura maxima  en X, Y
        tHmax =((v*sin(alpha))/g)
        xHmax = Xi + (Vx*tHmax)
        
        #tiempo de alcance en X
        tXmax = tmax2
        xXmax = v*cos(alpha)*tmax2
        
        #Desarrollo grafica y correspondiente de funciones
        fig, ax = plt.subplots(1,1, figsize = (15,5))
        ax.plt.scatter(X, Y, 'K--', lw=3)
        #indicador trayectoria
        ax.set_xlabel("Trayectoria (x,y)", fontsize = 25)
        ax.set_xlabel('x [m]', fontsize = 16)
        ax.set_ylabel('y [m]', fontsize = 16)
        ax.grid(True, which = 'both')
        #indicador de datos para altura, distancia, velocidad, y posición      
        ax.plot(xHmax, Ymax, 's', lw = 4, label = (f'Altura Max: ({np.arround(xHmax, 2)}, {np.arround(Ymax, 2)})') )
        ax.plot(xXmax, hf, 'o', lw = 4, label = f'Distancia Max: ({np.arround(xXmax, 2)}, {hf}')
        ax.plot(Xi, h, 'v', lw = 4, label = f'Posición inicial: ({Xi}, {h})')
        ax.plot(lw = 4, label = f'Velocidad Generada: ({np.round(v, 2)})')
        ax.legend()
        
        #mostrar figura
        fig.show       
except Exception as exc:
    print(exc)
    print("No es posible calcular el alcance máximo de la esfera")
    
#ventana de apertura, para terminal.

ventana = tkinter.Tk()
ventana.mainloop()
