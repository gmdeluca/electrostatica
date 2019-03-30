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
Xmm_max = 10E-3 # ancho en x del area de simulación en 10 [mm] = 10E-3 [m]
Ymm_max = 10E-3 # largo en y del area de simulación en 10 [mm] = 10E-3 [m]
Xpix_max = 500 # ancho en x del area de simulación en pantalla [pixeles]
Ypix_max = 500 # largo en y del area de simulación en pantalla [pixeles]
X_Escala = Xpix_max / Xmm_max # Escala que sirve para transformar mm en pixeles y viceversa en el eje x [pixeles/mm]
Y_Escala = Ypix_max / Ymm_max # Escala que sirve para transformar mm en pixeles y viceversa en el eje x [pixeles/mm]
delta_tiempo = 1E-6 # Es el cambio en tiempo desde un instante de simulación al siguiente, consideremos que es 1 [us] = 1E-6 [s]
tiempo = 0 # Valor del tiempo inicial. [s]

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
        self.pos_x = a_pos_x # en el orden de los [um]= 10^-6 [m]
        self.pos_y = a_pos_y # en el orden de los [um]= 10^-6 [m]
        self.vel_x = a_vel_X # [mm/us = 10^-3/10^-9 m/s]
        self.vel_y = a_vel_y # [mm/us = 10^-3/10^-9 m/s]
        self.acel_x = a_acel_x # [mm/us^2 =  m/s]
        self.acel_y = a_acel_y # [mm/us^2 =  m/s]
        self.carga = a_carga # en el orden de los [nC]=1E-9 [C]
        self.masa = a_masa # en el orden de los [ug]=1E-6 [g]
        self.radio = a_radio
        self.color = a_color
        
        self.circulo = canvas.create_oval(
            round(self.pos_x * X_Escala, 0) - self.radio, round(self.pos_y * Y_Escala, 0) - self.radio,
            round(self.pos_x * X_Escala, 0) + self.radio, round(self.pos_y * Y_Escala + self.radio, 0), fill=self.color
        )
    def FuerzaX (self, a_q, a_x):
        FuerzaX = ke * a_q * self.carga / ((a_x - self.pos_x) ** 2) # la Fuerza en el eje x se expresa en [N]
        return FuerzaX

    def FuerzaY (self, a_q, a_y):
        FuerzaY = ke * a_q * self.carga / ((a_y - self.pos_y) ** 2) # la Fuerza en el eje y se expresa en [N]
        return FuerzaY

        
# ----------------------------------
# INICIALIZACION
# ----------------------------------


if __name__ == '__main__':
    root = tk.Tk()

    # create canvas
    canvas = tk.Canvas(root, width=Xpix_max, height=Ypix_max)
    canvas.pack()

    # create objects
    p1 = Particula(6E-3, 5E-3, 0, 0, 0, 0, 5E-9, 1E-6, 5, 'red')
    p2 = Particula(5E-3, 5E-3, 0, 0, 0, 0, 10E-9, 5E-6, 10, 'red')

# ----------------------------------
# BUCLE PRINCIPAL
# ----------------------------------
    while True:

# ACCIONES DEL MOTOR DE FISICA
# --------------------------------
 
        p1.acel_x = p2.FuerzaX(p1.carga, p1.pos_x) / p1.masa
        p1.vel_x = p1.vel_x + p1.acel_x * delta_tiempo
        p1.pos_x = p1.pos_x + p1.vel_x * delta_tiempo + (p1.acel_x * delta_tiempo**2) / 2
        
        p2.acel_x = p1.FuerzaX(p2.carga, p2.pos_x) / p2.masa
        p2.vel_x = p2.vel_x + p2.acel_x * delta_tiempo
        p2.pos_x = p2.pos_x - p2.vel_x * delta_tiempo - (p2.acel_x * delta_tiempo**2) / 2



# ACTUALIZACIONES DE ESTADO
# ---------------------------------
#        p1.pos_x = p1.pos_x - 1E-5
        p1.pos_y = p1.pos_y + 0
               
        
# ANALISIS DE COLISIONES
# ---------------------------------

        # Colisiones en el eje x
        if (round(p1.pos_x * X_Escala, 0) + p1.radio) >= Xpix_max :
            p1.pos_x = (Xpix_max - p1.radio) / X_Escala
        if (round(p1.pos_x * X_Escala, 0) - p1.radio) <= 1 :
            p1.pos_x = (1 + p1.radio) / X_Escala
            
        # Colisiones en el eje y
        if (round(p1.pos_y * Y_Escala, 0) + p1.radio) >= Ypix_max :
            p1.pos_y = (Ypix_max - p1.radio) / Y_Escala
        if (round(p1.pos_y * Y_Escala, 0) - p1.radio) <= 1 :
            p1.pos_y = (1 + p1.radio) / Y_Escala
            


# RENDERIZACION
# ---------------------------------
        canvas.coords(p1.circulo, round(p1.pos_x * X_Escala, 0) - p1.radio, round(p1.pos_y * Y_Escala, 0) - p1.radio,
        round(p1.pos_x * X_Escala, 0) + p1.radio, round(p1.pos_y * Y_Escala, 0) + p1.radio)
        canvas.coords(p2.circulo, round(p2.pos_x * X_Escala, 0) - p2.radio, round(p2.pos_y * Y_Escala, 0) - p2.radio,
        round(p2.pos_x * X_Escala, 0) + p2.radio, round(p2.pos_y * Y_Escala, 0) + p2.radio)
       
        canvas.update()
        
        
# CONTROL DE TEMPORIZACION / BUCLE
# ---------------------------------
        
        time.sleep(0.025)
