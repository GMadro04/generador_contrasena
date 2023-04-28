import random 

# Creo unas primeras listas con caracteres para el generador 
mayusculas = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
minusculas = []  # creo una lista vacia para guradar minusculas
symbol = ['*', '+', '-', '/', '@', '_', '?', '!', '[','{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
lim = len(mayusculas)
# aqui convierto la lista mayuscula en minusculas y las guardo en una nueva lista
for i in range(lim):
    minus = mayusculas[i].lower()
    minusculas.append(minus)
# print(minusculas) # aqui estaba mirando si funcionaba jajajaja y si

# Uno las listas para hacer una sola donde van a ser seleccionadas
caracteres = mayusculas + minusculas + symbol + nums

contrasena = [] # lista para llenar contraseña 


# Aquí va el ciclo con el que se arma la contraseña 
for i in range(10):
    select = random.choice(caracteres)
    contrasena.append(select)
    
contrasena = "".join(contrasena)

print(contrasena)
    
