from sympy import Symbol, lambdify


def simpson_compuesto(str_funcion, a, b, m):
    """
    Regla compuesta de Simpson para calcular la integral de una funcion
    :param str_funcion: String con la funcion a integrar, debe ser en funcion de x
    :param a: Limite inferior
    :param b: Limite superior
    :param m: Cantidad de puntos a utilizar
    :return: Resultado obtenido
    """
    # Se contruye la funcion a evaluar
    funcion = lambdify(Symbol('x'), str_funcion)
    h = (b - a) / (m - 1)  # Se calcula el h
    x = a
    soporte = []

    # Construccion del conjunto soporte
    while x <= b:
        soporte.append(x)
        x += h

    par = 0  # Variable que contiene la sumatoria de todas las posiciones par
    impar = 0  # Variable que contiene la sumatoria de todas las posiciones impar

    n = len(soporte)
    for i in range(1, n - 1):
        # Se verifica si el indice de la lista es par o impar
        if i % 2 == 0:
            par += funcion(soporte[i])
        else:
            impar += funcion(soporte[i])

    return h * (funcion(soporte[0]) + 2 * par + 4 * impar + funcion(soporte[-1])) / 3


# resultado = simpson_compuesto('log(x)', 2, 5, 7)
# print(resultado)

# resultado = simpson_compuesto("exp(-x ** 2)", 0, 4, 6)
# print(resultado)
