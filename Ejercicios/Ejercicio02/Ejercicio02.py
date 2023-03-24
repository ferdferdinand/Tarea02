texto = input("Ingresa un texto sin formato: ")

print("!Vamos a darle formato a tu texto!",end = '\n\n')

#Cambio de etiquetas html

##Cuantas veces se tiene que hacer el cambio a upper
rep = texto.count("<h1>")

for i in range(rep):
    inicio = texto.find("<h1>")
    texto = texto.replace("<h1>", "",1) #Hace el remplazo una vez para evitar borrar las siguientes
    final = texto.find("</h1>") 
    mayus = texto[inicio:final] #Toma la parte que será cambiada a upper
    texto = texto.replace(mayus,mayus.upper(),1) #Hace el cambio una vez para evitar cambiar palabras iguales
    texto = texto.replace("</h1>", "",1) #Borra una vez el final de la etiqueta

#Reemplaza todas las etiquetas restantes
texto = texto.replace('<br>', '\n')
texto = texto.replace('<hr>','\n' + '-' * 80 + '\n')


#Lista separada por cada línea entre los saltos de línea
texto = texto.splitlines()

for line in texto: #Para cada línea
    if len(line) > 80: #Para líneas mayores a 80 carácteres
        start = 0
        for j in range(len(line) // 80): #Partir en tantas líneas como sea necesario
            salto = line[start:start + 80].rfind(' ')#Posición para saltar de línea
            print(line[start:start + salto])
            start += salto + 1
        print(line[start:])#Última línea
        
    else: #Líneas menores a 80 caracteres
        print(line) 
