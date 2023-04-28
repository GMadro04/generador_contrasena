import random 

# Creo unas primeras listas con caracteres para el generador 
mayúsculas = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Se automatiza los cambios de mayusculas a minusculas 
for i in range(len(mayúsculas)):
    minúsculas = mayúsculas[i].lower
symbols = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')']
numero = ['1','2','3','4','5']

# Uno las listas para hacer una sola donde van a ser seleccionadas
fusion = mayúsculas+minúsculas+symbols+numero
# Creo una lista vacía para llenar la contraseña
contraseña = []
# Aquí va el ciclo con el que se arma la contraseña 
for i in range(10):
    select = random.choice(contraseña)
    contraseña.append(select)
contraseña = "".join(contraseña)

print(contraseña)
    