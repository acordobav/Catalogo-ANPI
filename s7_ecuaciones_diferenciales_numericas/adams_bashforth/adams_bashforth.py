from sympy import Symbol, lambdify


def adams_bashforth(str_funcion, a, b, n, x0, y0, y1):
    """
    Metodo de Adams-Bashforth de paso dos para aproximar la solucion de un problema de valor inicial
    :param str_funcion: string con la funcion que se debe evaluar
    :param a: Extremo inferior del intervalo
    :param b: Extremo superior del intervalo
    :param n: Cantidad de puntos
    :param x0: Valor inicial de x
    :param y0: Valor de y para el x inicial
    :param y1: Valor de y1 para el x1
    :return: Valor de la ecuacion en b
    """
    # Se contruye la funcion a evaluar
    funcion = lambdify([Symbol('x'), Symbol('y')], str_funcion)
    h = (b - a) / (n - 1)
    x = x0 + h  # Variable para el x de la iteracion actual
    y = y1  # Variable para el y de la iteracion actual
    x_ant = x0  # Variable para el x de la iteracion anterior
    y_ant = y0  # Variable para el y de la iteracion anterior

    while x <= b - h:
        y_temp = y  # Variable temporal para guardar el valor de y
        y = y + h * (3 * funcion(x, y) - funcion(x_ant, y_ant)) / 2

        # Se actualizan las varaibles
        y_ant = y_temp
        x_ant = x
        x += h

    return y


# resultado = adams_bashforth('1 + (x - y) ** 2', 2, 4, 11, 2, 1, 1.191)
# print(resultado)
