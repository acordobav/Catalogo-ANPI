from sympy import Symbol, lambdify


def runge_kutta(str_funcion, a, b, n, x, y, orden):
    """
    Metodo de Runge-Kutta para aproximar la solucion de un problema de valor inicial
    :param str_funcion: string con la funcion que se debe evaluar
    :param a: Extremo inferior del intervalo
    :param b: Extremo superior del intervalo
    :param n: Cantidad de puntos
    :param x: Valor inicial de x
    :param y: Valor de y para el x inicial
    :param orden: Entero que indica el orden del metodo, debe ser 2, 3 o 4 unicamente
    :return: Valor de la ecuacion diferencial en xn
    """
    if orden != 2 and orden != 3 and orden != 4:
        return "El parametro orden debe ser 2, 3 o 4"

    # Se contruye la funcion a evaluar
    funcion = lambdify([Symbol('x'), Symbol('y')], str_funcion)
    h = (b - a) / (n - 1)

    # Caso en el que el orden es 2
    if orden == 2:
        while x <= b - h:
            k1 = calcular_k1(funcion, x, y)  # Calculo del k1
            k2 = calcular_k2(funcion, x, y, h, k1)  # Calculo del k2
            y = y + h * k2
            x += h

    # Caso en el que el orden es 3
    if orden == 3:
        while x <= b - h:
            k1 = calcular_k1(funcion, x, y)  # Calculo del k1
            k2 = calcular_k2(funcion, x, y, h, k1)  # Calculo del k2
            k3 = funcion(x + h, y + h * (2 * k2 - k1))  # Calculo del k3
            y = y + h * (k1 + 4 * k2 + k3) / 6
            x += h

    # Caso en el que el orden es 4
    if orden == 4:
        while x <= b - h:
            k1 = calcular_k1(funcion, x, y)  # Calculo del k1
            k2 = calcular_k2(funcion, x, y, h, k1)  # Calculo del k2
            k3 = funcion(x + h / 2, y + h * k2 / 2)  # Calculo del k3
            k4 = calcular_k4(funcion, x, y, h, k3)  # Calculo dek k4
            y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x += h

    return y


def calcular_k1(funcion, x, y):
    """
    Funcion para calcular el k1 del metodo de Runge-Kutta
    :param funcion: Lambdify con la funcion a evaluar
    :param x: Numero con el valor de x
    :param y: Numero con el valor de y
    :return: Numero con el valor de k1
    """
    return funcion(x, y)


def calcular_k2(funcion, x, y, h, k1):
    """
    Funcion para calcular el k2 del metodo de Runge-Kutta
    :param funcion: Lambdify con la funcion a evaluar
    :param x: Numero con el valor de x
    :param y: Numero con el valor de y
    :param h: Numero con el h del metodo de Runge-Kutta
    :param k1: Numero con el k1 del metodo de Runge-Kutta
    :return: Numero con el valor de k2
    """
    return funcion(x + h / 2, y + h * k1 / 2)


def calcular_k4(funcion, x, y, h, k3):
    """
    Funcion para calcular el k4 del metodo de Runge-Kutta
    :param funcion: Lambdify con la funcion a evaluar
    :param x: Numero con el valor de x
    :param y: Numero con el valor de y
    :param h: Numero con el h del metodo de Runge-Kutta
    :param k3: Numero con el k3 del metodo de Runge-Kutta
    :return: Numero con el valor de k4
    """
    return funcion(x + h, y + h * k3)


# resultado = runge_kutta('-x * y + 4 * x / y', 0, 1, 11, 0, 1, 2)
# print(resultado)

# resultado = runge_kutta('-x * y + 4 * x / y', 0, 1, 11, 0, 1, 3)
# print(resultado)

# resultado = runge_kutta('-x * y + 4 * x / y', 0, 1, 11, 0, 1, 4)
# print(resultado)
