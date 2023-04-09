from linea import Linea
from punto import Punto

"""
10 líneas específicas para probar los métodos de la clase línea
"""

linea1 = Linea(Punto(-2,19),Punto(-1,-5))
linea2 = Linea(Punto(6,9),Punto(30,10))
linea3 = Linea(Punto(10,19),Punto(8,16))
linea4 = Linea(Punto(-2,2),Punto(2,8))
linea5 = Linea(Punto(-2,1),Punto(4,10))
linea6 = Linea(Punto(26,6),Punto(12,7))
linea7 = Linea(Punto(26,6),Punto(12,5))
linea8 = Linea(Punto(2,8),Punto(2,19))
linea9 = Linea(Punto(2,8),Punto(13,8))
linea10 = Linea(Punto(7,19),Punto(7,27))

print("Linea 1:",linea1,sep = "\n")
p = Punto(0,-29)
print(p,"está en la recta:", linea1.punto_linea(p),end = "\n\n")

print("Linea 2:",linea2, sep = "\n")

print("linea 2 y 1 Paralelas:",linea2.paralelas(linea1))
print("linea 2 y 1 Perpendiculares:",linea2.perpendiculares(linea1))
print("linea 2 y 1 Intersección:", linea2.interseccion(linea1),end="\n\n\n")


print("Linea 3:",linea3,sep = "\n")
p = Punto(-2,1)
print(p,"está en la recta:", linea3.punto_linea(p),end = "\n\n")

print("Linea 4:",linea4,sep = "\n")

print("linea 3 y 4 Paralelas:",linea4.paralelas(linea3))
print("linea 3 y 4 Perpendiculares:",linea4.perpendiculares(linea3))
print(linea4.interseccion(linea3),end="\n\n\n")

print("Linea 5:",linea5,sep = "\n")
print("Iguales 3 y 5:",linea5 == linea3)
print("Intersección 3 y 5:",linea5.interseccion(linea3),end="\n\n\n")

print("Linea 6:",linea6,sep = "\n")
print("linea 1 y 6 Intersección:", linea6.interseccion(linea1),end="\n\n\n")

print("Linea 7:",linea7,sep = "\n")
print("linea 6 y 7 Intersección:", linea7.interseccion(linea6),end="\n\n\n")

print("Linea 8:",linea8, sep = "\n")
p = Punto(2,-29)
print(p,"está en la recta:", linea8.punto_linea(p))
print("linea 1 y 8 Intersección:", linea8.interseccion(linea1),end="\n\n\n")


print("Linea 9:",linea9, sep = "\n")
p = Punto(19,8)
print(p,"está en la recta:", linea9.punto_linea(p))
print("Iguales 8 y 9:",linea8 == linea9)
print("linea 8 y 9 Paralelas:",linea9.paralelas(linea8))
print("linea 8 y 9 Perpendiculares:",linea9.perpendiculares(linea8))
print("linea 8 y 9 Intersección:", linea9.interseccion(linea8))
print("linea 5 y 9 Intersección:", linea9.interseccion(linea5),end="\n\n\n")


print("Linea 10:",linea10, sep = "\n")
p = Punto(7,-29)
print(p,"está en la recta:", linea10.punto_linea(p))
print("Iguales 8 y 10:",linea10 == linea8)
print("linea 8 y 10 Paralelas:",linea10.paralelas(linea8))
print("linea 8 y 10 Perpendiculares:",linea10.perpendiculares(linea8))
print("linea 8 y 10 Intersección:", linea10.interseccion(linea8),end="\n\n\n")

print("Iguales 9 y 10:",linea10 == linea9)
print("linea 9 y 10 Paralelas:",linea10.paralelas(linea9))
print("linea 9 y 10 Perpendiculares:",linea10.perpendiculares(linea9))
print("linea 9 y 10 Intersección:", linea10.interseccion(linea9),end="\n\n\n")







