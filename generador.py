import random 

# Creo unas primeras listas con caracteres para el generador 
mayúsculas = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
minúsculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
symbols = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')']
numero = ['1','2','3','4','5']

# Uno las listas para hacer una sola donde van a ser seleccionadas
caracteres = mayúsculas + minúsculas + symbols + numero
# Creo una lista vacía para llenar la contraseña
contrasena = []

for i in range(15):  # el 15 es el numero de caracteres que llevará la contraseña puede ser cualquiera 8-7 etc
    carcter_random = random.choice(caracteres)
    contrasena.append(carcter_random)

contrasena = "".join(contrasena)

print("La contraseña es:", contrasena)