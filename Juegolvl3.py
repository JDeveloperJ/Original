print("Bienvenido")
print("Ingresa un caracter para ver si es una vocal")
caracter = input()

vocales = ["a", "e", "i", "o", "u"]

if caracter.lower in vocales:
    print("El caracter ingresado es una cocal")
else:
    print("El caracter ingresado no es una cocal")
