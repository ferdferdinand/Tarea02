import math

#Funciones de ayuda para la función principal del ejercicio 

def factorial(n):
    """
    Función para calcular el factorial de un número

    Params:
        n(int): Valor a calcular su factorial

    Returns:
        fac(int): Factorial de n
    """
    fac = 1
    for i in range(n,1,-1):
        fac *= i
    return fac

def radians(x):
    """
    Convierte de grados a radianes

    Params:
        x(int): Valor en grados
    Returns:
        (float): Valor en radianes de x
    """
    return x*math.pi/180
