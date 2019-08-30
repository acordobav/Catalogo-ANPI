from sympy import diff, sympify, solve


def punto_fijo(str_funcion, xk, a, b, tol):
    """
    Funcion que implementa el metodo de punto fijo
    :param str_funcion: string con la funcion a evaluar
    :param xk: valor inicial del punto fijo
    :param a: extremo inferior del intervalo
    :param b: extremo superior del intervalo
    :param tol: tolerancia al fallo que debe tener el resultado
    :return: lista: [xk calculado, numero de iteraciones]
    """
    funcion = sympify(str_funcion)  # Se obtiene la funcion a partir del string
    df = diff(funcion, 'x')         # Se deriva la funcion
    itr = 0                         # Contador de iteraciones

    # Se verifica la existencia del punto fijo
    if verificar_existencia(funcion, df, a, b) != 0:
        return "No se cumple el criterio de existencia"

    # Se verifica la unicidad del punto fijo
    if verificar_unicidad(df) != 0:
        return "No se cumple el criterio de unicidad"

    xk_ant = xk

    while 1:
        # Se actualiza el valor de xk
        xk = float(funcion.subs({'x': xk}))
        itr += 1

        # Se verifica la condicion de parada
        if abs(xk - xk_ant) < tol:
            break

        xk_ant = xk

    return [xk, itr]


def verificar_existencia(funcion, derivada, a, b):
    """
    Funcion para verificar la existencia de un punto fijo dentro de [a, b]
    :param funcion: funcion simbolica (sympify)
    :param derivada: derivada de la funcion simbolica
    :param a: extremo inferior del intervalo
    :param b: extremo superior del intervalo
    :return: 0 si existe, un 1 en caso de que no exista
    """
    # Se obtienen los puntos criticos de la funcion
    puntos_criticos = solve(derivada)

    # Puntos criticos deben estar dentro del intervalo [a, b]
    n = len(puntos_criticos)
    for i in range(0, n):
        # Se calcula el valor de f en el punto critico
        valor = float(funcion.subs({'x': puntos_criticos[i]}))

        # Se verifica que este valor este dentro del intervalo [a, b]
        if not a < valor < b:
            return 1

    # Se evaluan los extremos en la funcion
    valor_a = float(funcion.subs({'x': a}))
    valor_b = float(funcion.subs({'x': b}))

    # Funcion en los extremos debe estar dentro del intervalo [a, b]
    if not a < valor_a < b or not a < valor_b < b:
        1

    return 0


def verificar_unicidad(derivada):
    """
    Funcion para verificar la unicidad del punto fijo
    :param derivada: derivada de la funcion
    :return: 0 si el punto es unico, un 1 en caso contrario
    """
    # Se obtienen los puntos criticos de la funcion
    puntos_criticos = solve(derivada)

    # Puntos criticos deben estar dentro del intervalo [-1, 1]
    n = len(puntos_criticos)
    for i in range(0, n):
        # Se verifica que el punto critico este dentro de [-1, 1]
        if not -1 < puntos_criticos[i] < 1:
            return 1

    return 0


# print(punto_fijo('(x ** 2 - 1) / 3', 0, -1, 1, 10 ** -5))

# print(punto_fijo('1 / (1 + x ** 2)', 0, -3, 3, 10 ** -5))

# print(punto_fijo('log(2 * x + 1)', 0, 1, 2, 10 ** -5))
