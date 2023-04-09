import math
class Punto:
    def __init__(self,x=0, y=0):
        ##Variables de instancia
        self.__x = x
        self.__y = y

    def set_x(self, x):
        self.__x = x
        
    def set_y(self, y):
        self.__y = y
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def suma(self,otro_punto):
        #print(otro_punto.get_x())
        coord_x = self.__x + otro_punto.get_x()
        coord_y = self.__y + otro_punto.get_y()
        punto_suma = Punto(coord_x, coord_y)
        return punto_suma
        ## return Punto(self.__x + otro_punto.get_x(), self.__y + otro_punto.get_y())

    def resta(self,otro_punto):
        #print(otro_punto.get_x())
        coord_x = self.__x - otro_punto.get_x()
        coord_y = self.__y - otro_punto.get_y()
        punto_resta = Punto(coord_x, coord_y)
        return punto_resta
    
    def desplazamiento(self, aumento_x, aumento_y):
        self.__x += aumento_x
        self.__y += aumento_y   
            

    def distancia(self, otro_punto):
        val1= (otro_punto.get_x() - self.__x)*(otro_punto.get_x() - self.__x)
        val2 = math.pow((otro_punto.get_y() - self.__y),2)
        sum_val =  val1+val2
        return math.sqrt(sum_val)
        

    def __str__(self):
        return "("+ str(self.__x) + "," + str(self.__y) + ")"

    def __eq__(self, otro_punto):
        if isinstance(otro_punto, Punto):
            return self.__x == otro_punto.get_x() and self.__y == otro_punto.get_y()
        else:
            return False
            
            

        



