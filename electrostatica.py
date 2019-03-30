# CATEDRA DE FISICA - VIDEOJUEGOS
# UNIVERSIDAD DE LA CUENCA DEL PLATA
# PROF. GUSTAVO MANUEL DELUCA
#
# PROYECTO: SIMULACION DE ELECTROSTATICA Y MOVIMIENTO DE CARGAS
# VERSION: 1.0
# ACTUALIZACION: 21-03-2019

# ----------------------------------
# IMPORTACION DE LIBRERIAS NECESARIAS
# ----------------------------------

import tkinter as tk
import time

# ----------------------------------
# DEFINICION DE CONSTANTES Y PARAMETROS
# ----------------------------------

ke = 8.98755E9  # Constante de Coulomb, necesaria para el calculo de fuerzas. Usaremos su valor en el vacío. Sus unidades son [N * m^2 / C^2]
Xmm_max = 10 # ancho en x del area de simulación en [mm]
Ymm_max = 10 # largo en y del area de simulación en [mm]
Xpix_max = 200 # ancho en x del area de simulación en pantalla [pixeles]
Ypix_max = 200 # largo en y del area de simulación en pantalla [pixeles]
X_Escala = Xpix_max / Xmm_max # Escala que sirve para transformar mm en pixeles y viceversa en el eje x [pixeles/mm]
Y_Escala = Ypix_max / Ymm_max # Escala que sirve para transformar mm en pixeles y viceversa en el eje x [pixeles/mm]
delta_tiempo = 1 # Es el cambio en tiempo desde un frame al siguiente. [ms]
tiempo = 0 # Valor del tiempo inicial. [ms]

# ----------------------------------
# DEFINICIÓN DE CLASES
# ----------------------------------

# Clase Particula
# ---------------
#  posición --> pos_x, pos_y   [m]
#  velocidad --> vel_x, vel_y   [m/s]
#  aceleración --> acel_x, acel_y   [m/s^2]
#  carga de la particula --> carga [C]
#  masa de la particula --> masa [g]
#  radio de dibujo de la particula --> radio (depende de la carga de la particula) [pixeles]
#  color de dibujo de la particula --> color --> 'blue' para carga negativa y 'red' para carga positiva

class Particula:
    def __init__(self,
                a_pos_x,  
                a_pos_y,  
                a_vel_X,
                a_vel_y,
                a_acel_x,
                a_acel_y,
                a_carga,
                a_masa,
                a_radio,
                a_color):
        self.pos_x = a_pos_x # [mm = 10^-3 m]
        self.pos_y = a_pos_y # [mm = 10^-3 m]
        self.vel_x = a_vel_X # [mm/us = 10^-3/10^-9 m/s]
        self.vel_y = a_vel_y # [mm/us = 10^-3/10^-9 m/s]
        self.acel_x = a_acel_x # [mm/us^2 =  m/s]
        self.acel_y = a_acel_y # [mm/us^2 =  m/s]
        self.carga = a_carga 
        self.masa = a_masa
        self.radio = a_radio
        self.color = a_color
        
        self.circulo = canvas.create_oval(
            self.pos_x - self.radio, self.pos_y - self.radio, self.pos_x + self.radio, self.pos_y + self.radio, fill=self.color
        )
    def FuerzaX (self, a_q, a_x):
        FuerzaX = ke * a_q * self.carga / (a_x - self.pos_x)^2  # la Fuerza en el eje x se expresa en [N]

    def FuerzaY (self, a_q, a_y):
        FuerzaY = ke * a_q * self.carga / (a_y - self.pos_y)^2 # la Fuerza en el eje y se expresa en [N]

        
# ----------------------------------
# INICIALIZACION
# ----------------------------------


if __name__ == '__main__':
    root = tk.Tk()

    # create canvas
    canvas = tk.Canvas(root, width=Xpix_max, height=Ypix_max)
    canvas.pack()

    # create objects
    p1 = Particula(50, 50, 0, 0, 0, 0, 5, 10, 5, 'red')
    p2 = Particula(100, 50, 0, 0, 0, 0, -10, 5, 10, 'blue')

# ----------------------------------
# BUCLE PRINCIPAL
# ----------------------------------
    while True:

# ACCIONES DEL MOTOR DE FISICA
# --------------------------------
 
        p1.acel_x = p2.FuerzaX / p1.masa
        p1.vel_x = p1.vel_x + p1.acel_x * delta_tiempo
        p1.pos_x = p1.pos_x + p1.vel_x * delta_tiempo + p1.acel_x * delta_tiempo^2 / 2
        


# ACTUALIZACIONES DE ESTADO
# ---------------------------------
        p1.pos_x = p1.pos_x - 1
        p1.pos_y = p1.pos_y + 0
               
        
# ANALISIS DE COLISIONES
# ---------------------------------

        # Colisiones en el eje x
        if (p1.pos_x + p1.radio) >= Xpix_max :
            p1.pos_x = Xpix_max - p1.radio
        if (p1.pos_x - p1.radio) <= 1 :
            p1.pos_x = 1 + p1.radio
            
        # Colisiones en el eje y
        if (p1.pos_y + p1.radio) >= Ypix_max :
            p1.pos_y = Ypix_max - p1.radio
        if (p1.pos_y - p1.radio) <= 1 :
            p1.pos_y = 1 + p1.radio
            


# RENDERIZACION
# ---------------------------------
        canvas.coords(p1.circulo, p1.pos_x - p1.radio, p1.pos_y - p1.radio, p1.pos_x + p1.radio, p1.pos_y + p1.radio)
        canvas.update()
        
        
# CONTROL DE TEMPORIZACION / BUCLE
# ---------------------------------
        
        time.sleep(0.025)
