from linea import Linea #Clase Linea
from punto import Punto #Calse Punto
from crearLineaPunto import crearLinea #Función propia para crear un objeto Linea
from crearLineaPunto import crearPunto #Función propia para crear un objeto Punto

"""
Menú para interactuar con la clase Linea
"""

linea = crearLinea()
    
while True:
    
    print("","[0]SALIR",sep="\n")
    print("[1]Mostrar ecuación de la recta")
    print("[2]Calcular la pendiente de la recta")
    print("[3]Calcular la ordenada al origen de la recta")
    print("[4]Determinar si un punto está en la recta")
    print("[5]Dererminar si dos rectas son paralelas")
    print("[6]Determinar si dos rectas son perpendiculares")
    print("[7]Intersección entre dos rectas")
    print("[8]Determinar si dos rectas son iguales")
    print("[9]Probar con otros puntos",end="\n\n")
    opcion = int(input("Elige una opción: "))
    print()

    match opcion:
        case 0:
            print("Fin del programa")
            break
        
        case 1:
            print("La ecuación de la linea que pasa por",linea, "es:")
            print(linea.eqc())
            
        case 2:
            print("La pendiente de la linea que pasa por",linea, "es:")
            print("m =",linea.pendiente())
            
        case 3:
            print("La ordena al origen de la linea que pasa por", linea, "es:")
            print("b =", linea.ord_origen())
            
        case 4:
            punto = crearPunto()
            print(punto,"pertenece a la recta:",linea.punto_linea(punto))
            
        case 5:
            linea2 = crearLinea()
            print("Paralelas:",linea.paralelas(linea2))
            
        case 6:
            linea2 = crearLinea()
            print("Perpendiculares:",linea.perpendiculares(linea2))
            
        case 7:
            linea2 = crearLinea()
            print(linea.interseccion(linea2))
            
        case 8:
            linea2 = crearLinea()
            if linea == linea2:
                print("Son iguales")
            else:
                print("No son iguales")
        case 9:
            linea = crearLinea()

        
    
