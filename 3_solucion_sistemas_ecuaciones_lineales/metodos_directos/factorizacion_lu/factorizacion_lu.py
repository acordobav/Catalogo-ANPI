from sympy import Symbol, solve
from scipy import linalg


def factorizacion_lu(matriz_a, matriz_b):
    """
    Metodo de Factorizacion LU para resolver un sistema A x = B
    :param matriz_a: matriz cuadrada de nxn
    :param matriz_b: matriz columna de nx1
    :return: matriz x que resuelve el sistema A x = b
    """
    n = len(matriz_a)
    m = len(matriz_a[0])
    lista_simb = []

    if n != m:
        return "matriz_a debe ser cuadrada"

    # Se crea una lista con las variables simbolicas de la ecuacion
    for i in range(0, n):
        lista_simb.append(Symbol('x' + str(i)))

    # Se calculan las matrices L y U del sistema
    matriz_i, matriz_l, matriz_u = linalg.lu(matriz_a)

    # Se resuelve el sistema L y = b utilizando una sustitucion hacia adelante
    lista_y = lista_simb.copy()
    for i in range(0, n):
        sub_lista1 = matriz_l[i]
        ecuacion1 = '- ' + str(matriz_b[i][0])

        # Se forma la ecuacion
        for x in range(0, m):
            ecuacion1 += ' + ' + str(sub_lista1[x]) + ' * ' + str(lista_y[x])

        # Se resuelve la ecuacion
        resultado1 = solve(ecuacion1)
        lista_y[i] = resultado1[0]

    # Se resuelve el sistema U x = y utilizando una sustitucion hacia atras
    lista_x = lista_simb.copy()
    for i in range(1, n + 1):
        sub_lista2 = matriz_u[-i]
        ecuacion2 = '- ' + str(lista_y[-i])

        # Se forma la ecuacion
        for x in range(0, m):
            ecuacion2 += ' + ' + str(sub_lista2[x]) + ' * ' + str(lista_x[x])

        # Se despeja la ecuacin
        resultado2 = solve(ecuacion2)
        lista_x[-i] = resultado2[0]

    return lista_x


# a = [[4, -2, 1], [20, -7, 12], [-8, 13, 17]]
# b = [[11], [70], [17]]
# print(factorizacion_lu(a, b))

# a1 = [[2, 3, 4], [4, 5, 10], [4, 8, 2]]
# b1 = [[6], [16], [2]]
# print(factorizacion_lu(a1, b1))
