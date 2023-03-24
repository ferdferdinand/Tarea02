texto = input("Ingresa un texto sin formato: ")

print("!Vamos a darle formato a tu texto!",end = '\n\n')

#Cambio de etiqueta html
texto = texto.replace('<br>', '\n')
texto = texto.replace('<hr>','\n' + '-' * 80 + '\n')

#Lista separada por cada salto de línea
texto = texto.splitlines()

for line in texto: #Para el texto entre cada salto
    if len(line) > 80: #Para líneas mayores a 80 carácteres
        start = 0 #inicio del rango que vamos a verificar
        salto = line[start:start + 80].rfind(' ')#Posición para saltar de línea
        print(line[start:start + salto])
        start += salto + 1
        print(line[start:])#Última línea 
    else:
        print(line)


