#import math

#Importamos las funciones de ayuda que creamos (si existen en math pero, en este momento del curso es buena práctica crearlas nosotros)
import funciones as func

def sinTay(x): #función para aproximar la función sin(x), recibe los grados
    """
    Función para aproximar el sin(x)

    Params:
        x(int): Valor x al que se quiere aproximar el sin(x)
    Returns:
        S_k(float): Valor aproximado del sin(x)
    """
    E = 1 #iniciamos un error en 1
    k = 0 #iniciamos el k-ésimo termino en 0
    S_k = 0 
    S_k1 = 0
    a = 0 #variable de ayuda
    if abs(x) > 360: #si los grados de x son mayores a 360 o menores a -360
        a = x % 360
        if 360 - a < a: #se calcula por el más cercano a 0
            x = -(360-a)
        else:
            x = a
    #Este print es sólo por el ejercicio, en otro caso no es necesario ponerlo
    print(f"El sin de {x}° es:", end=" ")
    #x = math.radians(x) #convertimos los grados a radianes con math
    x = func.radians(x) #convertimos los grados a radianes con nuestra función
    while E > 0.000001 and x != 0: #se repite mientras el error sea mayor que 0.000001 y si los grados no son 0
        S_k1 = S_k #definimos S_(k-1)
        #S_k += (((-1)**k)/math.factorial(2*k+1))*x**(2*k+1) #calculamos S_k con math
        S_k += (((-1)**k)/func.factorial(2*k+1))*x**(2*k+1) #calculamos S_k
        k += 1
        if S_k1 != 0:
            E = abs((S_k-S_k1)/S_k1) #calculamos el error por medio de S_(k-1) y S_k
    return S_k #regresa un dato float

        
