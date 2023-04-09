from punto import Punto #Clase Punto()
import funciones as func #Módulo propio
import numpy as np #Para la intersección a través de array

class Linea:

    #Método constructor, se define la recta a través de dos puntos
    def __init__(self, punto1 = Punto(), punto2 = Punto(1,1)):
        self.__punto1 = punto1
        self.__punto2 = punto2

    def get_punto1(self):
        return self.__punto1
    
    def get_punto2(self):
        return self.__punto2
    
    #Ecuación de la recta
    def eqc(self):
        #y-y1 = m(x-x1)
        # -m*x + y + (m*x1 - y1) = 0
        m = self.pendiente()

        # m es racional
        if type(m) is str:
            p,q = m.split("/")
            #Convertimos el numerador y denominador de m en enteros
            p = int(p)
            q = int(q)
            
            #Calcular la constante m*x1 - y1, donde m es de la forma p/q
            #Reducimos la expresión m*x1 - y1
            p1,q1 = func.reducir(p*self.__punto1.get_x()- q*self.__punto1.get_y(),q)
            
            #Para dejar la ecuación sin racionales
            if q != q1:
                b = int(q*p1/q1)
            else:
                b = p1
                
            #Para imprimir el signo +
            if b >= 0:
                b = "+ " + str(b)

            #Para no imprimir -1x o 1x 
            if -p == 1:
                return "x + " + str(q)+ "y " + str(b) + " = 0"
            elif -p == -1:
                return "-x + " + str(q)+ "y " + str(b) + " = 0"
            else:
                return str(-p) + "x + " + str(q)+ "y " + str(b) + " = 0"

        #Recta con x constante
        elif type(m) is bool:
            x = -self.__punto1.get_x()

            if x > 0:
                return "x + " + str(x) + " = 0"
            else:
                return "x " + str(x) + " = 0"
            
        # m es entero
        else:
            b = m*self.__punto1.get_x() - self.__punto1.get_y()
            
            if b >= 0:
                    b = "+ " + str(b)
                    
            if m == 0:
                return "y " + str(b) + " = 0"
            
            else:                
                #Calcular la constante m*x1 - y1
                    
                #Para no imprimir -1x o 1x 
                if -m == 1:
                    return "x + y " + str(b) + " = 0"
                elif -m == -1:
                    return "-x + y " + str(b) + " = 0"
                else:
                    return str(-m) + "x + y " + str(b) + " = 0"


    #Pendiente de la recta
    def pendiente(self):
        #y2-y1
        p = self.__punto2.get_y()-self.__punto1.get_y()
        #x2-x1
        q = self.__punto2.get_x()-self.__punto1.get_x()

        #denominador distinto de 0
        if q != 0:
            if p%q == 0:
                m = int(p/q)
            #Reducir la expresión p/q
            else:
                p, q = func.reducir(p,q)
                m = str(p) + "/" + str(q)
            return m
        else:
            return False


    #Ordenada al origen
    def ord_origen(self):
        #y-y1 = m(-x1)
        #y = -m*x1 + y1 
        m = self.pendiente()
        # m es racional
        if type(m) is str:
            p,q = m.split("/")
            #Convertimos el numerador y denominador de m en enteros
            p = int(p)
            q = int(q)

            #Calcular la constante -m*x1 + y1, donde m es de la forma p/q
            #Reducimos la expresión -m*x1 + y1
            p1,q1 = func.reducir(-p*self.__punto1.get_x()+ q*self.__punto1.get_y(),q)
            if p1%q1 == 0:
                return p1
            else:
                return str(p1) + "/" + str(q1)

        #Recta con x constante
        elif type(m) is bool:
            return False
        
        # m es entero
        else:
            #Calcular la constante -m*x1 + y1
            return -m*self.__punto1.get_x() + self.__punto1.get_y()


    #Punto pertenece a la recta
    def punto_linea(self,punto):
        if isinstance(punto, Punto):
            x = punto.get_x()
            y = punto.get_y()
            
            #Se separan los coeficientes de la ecuación para poder evaluar
            a,b,c = func.coef(self.eqc())

            #Se evalúa el punto en la ecuación
            if a*x+b*y-c==0:
                return True
            else:
                return False
        else:
            return False


    #Rectas paralelas
    def paralelas(self,linea):
        m1 = self.pendiente()
        m2 = linea.pendiente()
        
        """
        En python 0 = False  probrar: bool(0)
        Hay que evitar que una recta horizontal (m = 0 = False)
        sea paralela (m1 = m2) a una recta vertical m = False
        """
        if type(m1) == bool: #La pendiente es bool (False) cuando no está definida (vertical)
            m1 = True #Cambiamos el valor a True
        if type(m2) == bool:
            m2 = True
            
        if m1 == m2:
            return True
        else:
            return False


    #Rectas perpendiculares
    def perpendiculares(self,linea):

        m1 = self.pendiente()
        m2 = linea.pendiente()

        if type(m1) is bool and type(m2) is bool:
            return False
        
        #Rectas con x = conts,  y = const
        elif type(m1) is bool and m2 == 0 or type(m2) is bool and m1 == 0:
            return True

        #Ambas pendientes de la forma p/q
        elif type(m1) is str and type(m2) is str:
            p1,q1 = m1.split("/")
            p2,q2 = m2.split("/")
            p1 = int(p1)
            q1 = int(q1)
            p2 = int(p2)
            q2 = int(q2)

            if p1*p2/(q1*q2) == -1:
                return True
            else:
                return False
            
        #Una pendiente de la forma p/q
        elif type(m1) is str:
            p1,q1 = m1.split("/")
            p1 = int(p1)
            q1 = int(q1)
            if p1*m2/q1 == -1:
                return True
            else:
                return False

        #La otra pendiente de la forma p/q
        else:
            p2,q2 = m2.split("/")
            p2 = int(p2)
            q2 = int(q2)
            if p2*m1/q2 == -1:
                return True
            else:
                return False


    #Intersección entre dos recta
    def interseccion(self,linea):

        if isinstance(linea,Linea):

            if not self.__eq__(linea) and not self.paralelas(linea):
                a1,b1,c1 = func.coef(self.eqc())
                a2,b2,c2 = func.coef(linea.eqc())

                #Creamos un sistema de ecuaciones con arreglos uni y bidimensionales
                A = np.array([[a1,b1],[a2,b2]])
                B = np.array([c1,c2])

                #Función de numpy para resolver el sistema
                x,y = np.linalg.solve(A,B)

                #Creamos el objeto de la clase punto
                punto = Punto(x,y)
                
                return(punto)
            
            elif self.__eq__(linea):
                return "Todos sus puntos son iguales"
            
            else:
                return "No se intersectan"
        else:
            return False


    """
    #Rectas iguales a través de su ecuación
    def __eq__(self,linea):
        if isinstance(linea, Linea):
                return self.eqc() == linea.eqc()
        else:
            return False
    """
    
    #Rectas iguales a través de su pendiente y ordenada
    def __eq__(self,linea):
        
        m1 = self.pendiente()
        m2 = linea.pendiente()
        b1 = self.ord_origen()
        b2 = linea.ord_origen()

        if isinstance(linea, Linea):
            "Hay que considerar que para rectas verticales pendiente y ordenada = False"
            if m1 == m2 == False and b1 == b2 == False:
                #Si tienen son verticales entonces vemos que un punto esté en la otra recta
                return self.punto_linea(linea.get_punto1())
            else:
                return  m1 == m2 and  b1 == b2
        else:
            return False


    #Imprimir los dos puntos que definieron a la recta
    def __str__(self):
        return "Los puntos de la recta: " + self.__punto1.__str__() + ", " + self.__punto2.__str__() + "\n" +\
               "La ecuación de la recta: " + self.eqc() + "\n" + \
               "La pendiente de la recta: m = " + str(self.pendiente()) + "\n" + \
               "La ordena al origen: b = " + str(self.ord_origen())
               

