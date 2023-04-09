"""
Funciones creadas para MenuLinea, para una fácil creación de un punto o recta
"""

from linea import Linea
from punto import Punto

def crearLinea():
    puntos = input("Ingresa dos puntos (x1,y1),(x2,y2): ")
    puntos = puntos.replace(" ", "")
    ind = puntos.find(")")
        
    if puntos[ind+1] != ",":
        puntos = puntos.replace(")", ",",1)
            
    puntos = puntos.replace("(","")
    puntos = puntos.replace(")","")
    puntos = puntos.split(",")

    x1 = int(puntos[0])
    y1 = int(puntos[1])
    x2 = int(puntos[2])
    y2 = int(puntos[3])

    #Creación del objeto
    return Linea(Punto(x1,y1),Punto(x2,y2))

def crearPunto():
    punto = input("Ingresa un punto (x,y): ")
    punto = punto.replace(" ", "")
    punto = punto.replace("(","")
    punto = punto.replace(")","")
    punto = punto.split(",")

    x = int(punto[0])
    y = int(punto[1])
    
    #Creación del objeto
    return Punto(x,y)

        
    
        
    
