#función para reducir fracciones

"""
Funciones propias para ayudarnos a una mejor implementación de métodos en Linea
"""

#Reducir fracciones p/q, devuelve p y q 
def reducir(p,q):
    #Para regresar el número positivo
    if p < 0 and q < 0:
        p = abs(p)
        q = abs(q)
    #Para que el negativo aparezca en el numerador
    elif q < 0:
        p = -p
        q = abs(q)
        
    for i in range(abs(min(p,q)),1,-1):
        if abs(min(p,q))%i == 0:
            if abs(max(p,q))%i == 0:
                p /= i
                q /= i
            
    return int(p),int(q)


#Tomar los coeficientes de una ecuación (str)
def coef(eqc):
    #Quitamos " = 0"
    eqc = eqc[:-4]
    #Quitamos todos los espacios
    eqc = eqc.replace(" ","")

    if 'x' in eqc and 'y' in eqc:
        #Cambiamos la x por un espacio
        eqc = eqc.replace("x", " ")
        #Cambiamos y por un espacio
        eqc = eqc.replace("y", " ")
        #Separamos en tres partes, la primera contiene el coeficiente de x
        #la segunda contiene el coeficiente de y
        #la última contiene la constante
        eqc = eqc.split(" ")

        #Escalar de x
        if eqc[0] == "-":
            a = -1
        elif eqc[0] == "":
            a = 1
        else:
            a = int(eqc[0])

        #Escalar de y
        if eqc[1] == "+":
            b = 1
        else:
            b = int(eqc[1])

        #Independiente
        c = -int(eqc[2])
        
    elif 'x' not in eqc:
        #Cambiamos y por un espacio
        eqc = eqc.replace("y", " ")
        eqc = eqc.split(" ")

        #Escalar de x
        a = 0
        #Escalar de y
        if eqc[0] == "":
            b = 1
        else:
            b = int(eqc[0])
        #Independiente
        c = -int(eqc[1])

    elif 'y' not in eqc:
        #Cambiamos la x por un espacio
        eqc = eqc.replace("x", " ")
        eqc = eqc.split(" ")

        #Escalar de x
        if eqc[0] == "":
            a = 1
        else:
            a = int(eqc[0])
        #Escalar de y
        b = 0
        #Independiente
        c = -int(eqc[1])

    return a,b,c

