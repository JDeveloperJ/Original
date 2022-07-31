print("Bienvenido")
print("En este programa podras calcular el tu promedio final de curso")

practica1 = int(input("Ingresa la nota de tu primera practica"))
practica2 = int(input("Ingresa la nota de tu segunda practica"))
practica3 = int(input("Ingresa la nota de tu tercera practica"))
parcial1 = int(input("Ingresa la nota de tu primer parcial"))
parcial2 = int(input("Ingresa la nota de tu segundo parcial"))
np = int(input("Ingresa tu nota permanente"))

if(practica1 > practica2 and practica2 > practica3):
    promedioppc = (practica1 + practica2)/2
elif(practica2 > practica1 and practica3 > practica1):
    promedioppc =(practica2 + practica3)
else:
    promedioppc =(practica1 + practica3)/2

promedioppa = (parcial1 + parcial2)/2

promediofinal = (promedioppa * 0.5) + (promedioppc * 0.4) + (np * 0.1)

if promediofinal > 11:
    print("Has aprobado el curso con una nota de " , promediofinal)
else:
    print("Has desaprobado el curso con una nota de ", promediofinal)
    print("Pa la prox vez estudia un poco mas xd")