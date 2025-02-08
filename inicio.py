# age = int(input("Ingrese su edad:"))
# name = "Mario"
# cover = int(input("Ingrese su dinero:"))

# if age < 18:
#  print("no se permite el ingreso")
# elif cover < 50000:
#  print("no se permite el ingreso, no tiene el dinero suficiente")
# elif cover > 50000:
#  cover1=cover-50000
#  print("Bienvenido",name,"su devuelta es de:", cover1)
# else:
#  print("Bienvenido:", name) 


temp = []
temperatura = 0
for n in range (0,5):
    temp.append (int(input("digite las temperaturas:")))
    temperatura=sum(temp)
    print("Las temperaturas son:", temp)
   
promedio = temperatura / len(temp)
if promedio <= 20:
    print("El promedio de temperaturas de es de:",promedio, "la temperatura es baja")
elif promedio >= 37:
     print("El promedio de temperaturas de es de:",promedio, "la temperatura es muy alta revise la ventilacion")
else:
    print("El promedio de temperaturas de es de:",promedio, "la temperatura es normal")