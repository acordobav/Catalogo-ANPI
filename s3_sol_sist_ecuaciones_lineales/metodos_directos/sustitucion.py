from sympy import Symbol, solve


def sustitucion_adelante(matriz_a, matriz_b):
    """
    Funcion para realizar una sustitucion hacia adelante
    :param matriz_a: matriz triangular inferior
    :param matriz_b: matriz columna
    :return: matriz con el resultado de realizar la sustitucion
    """
    n = len(matriz_a)
    m = len(matriz_a[0])

    lista_simb = []
    # Se crea una lista con las variables simbolicas de la ecuacion
    for i in range(0, n):
        lista_simb.append([Symbol('x' + str(i))])

    # Se resuelve el sistema A x = B utilizando una sustitucion hacia adelante
    for i in range(0, n):
        sub_lista = matriz_a[i]
        ecuacion = '- ' + str(matriz_b[i][0])

        # Se forma la ecuacion
        for x in range(0, m):
            ecuacion += ' + ' + str(sub_lista[x]) + ' * ' + str(lista_simb[x][0])

        # Se resuelve la ecuacion
        resultado = solve(ecuacion)
        lista_simb[i] = resultado

    return lista_simb


def sustitucion_atras(matriz_a, matriz_b):
    """
    Funcion para realizar una sustitucion hacia adelante
    :param matriz_a: matriz triangular superior
    :param matriz_b: matriz columna
    :return: matriz con el resultado de realizar la sustitucion
    """
    n = len(matriz_a)
    m = len(matriz_a[0])

    lista_simb = []
    # Se crea una lista con las variables simbolicas de la ecuacion
    for i in range(0, n):
        lista_simb.append([Symbol('x' + str(i))])

    # Se realiza una sustitucion hacia atras
    for i in range(1, n + 1):
        sub_lista = matriz_a[-i]
        ecuacion = '- ' + str(matriz_b[-i][0])

        for x in range(0, m):
            ecuacion += ' + ' + str(sub_lista[x]) + ' * ' + str(lista_simb[x][0])

        resultado = solve(ecuacion)
        lista_simb[-i] = resultado

    return lista_simb
