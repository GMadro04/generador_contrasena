import random 

# Creo unas primeras listas con caracteres para el generador 
mayúsculas = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
minúsculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
symbols = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')']
numero = ['1','2','3','4','5']

# Uno las listas para hacer una sola donde van a ser seleccionadas
fusion = mayúsculas+minúsculas+symbols+numero
# Creo una lista vacía para llenar la contraseña
contraseña = []
# Aquí va el ciclo con el que se arma la contraseña 
for i in range(10):
    select = random.choice(fusion)
    contraseña.append(select)
    contraseña = "".join(contraseña)

print("La contraseña es: ", contraseña)