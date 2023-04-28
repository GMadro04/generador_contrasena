import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = []  # creo una lista vacia para guradar minusculas
    symbol = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
              '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lim = len(mayusculas)
    # aqui convierto la lista mayuscula en minusculas y las guardo en una nueva lista
    for i in range(lim):
        minus = mayusculas[i].lower()
        minusculas.append(minus)
    # print(minusculas) # aqui estaba mirando si funcionaba jajajaja y si

    caracteres = mayusculas + minusculas + symbol + nums

    contrasena = []

    for i in range(15):  # el 15 es el numero de caracteres que llevará la contraseña puede ser cualquiera 8-7 etc
        carcter_random = random.choice(caracteres)
        contrasena.append(carcter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()
