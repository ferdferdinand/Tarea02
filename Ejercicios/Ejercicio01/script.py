#Importamos math y nuestra función para comparar los valores
import math
from sinTay import sinTay 

print(sinTay(19000))
print("Con la función de math: ",math.sin(math.radians(19000)),end="\n\n")

print(sinTay(39))
print("Con la función de math: ",math.sin(math.radians(39)),end="\n\n")

print(sinTay(-789))
print("Con la función de math: ",math.sin(math.radians(-789)),end="\n\n")
