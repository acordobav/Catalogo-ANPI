from sympy import Symbol, solve
from scipy import linalg


def eliminacion_gaussiana(matriz_a, matriz_b):
    """
    Funcion que implementa el metodo de Eliminacion Gaussiana
    :param matriz_a: matriz cuadrada e invertible
    :param matriz_b: matriz columna
    :return: matriz x del sistema A x = b
    """
    n = len(matriz_a)
    m = len(matriz_a[0])
    lista_simb = []

    if n != m:
        return "matriz_a debe ser cuadrada"

    # Se construye la matriz aumentada del sistema
    m_aumentada = []
    for i in range(0, n):
        m_aumentada.append(matriz_a[i] + matriz_b[i])
        lista_simb.append(Symbol('x' + str(i)))

    # Se obtiene la matriz trianguar superior del sistema
    matriz_i, matriz_l, matriz_u = linalg.lu(m_aumentada)

    # Se realiza una sustitucion hacia atras
    for i in range(1, n + 1):
        sub_lista = matriz_u[-i]
        ecuacion = '- ' + str(sub_lista[m])

        for x in range(0, m):
            ecuacion += ' + ' + str(sub_lista[x]) + ' * ' + str(lista_simb[x])

        resultado = solve(ecuacion)
        lista_simb[-i] = resultado[0]

    return lista_simb


# a = [[2, -6, 12, 16], [1, -2, 6, 6], [-1, 3, -3, -7], [0, 4, 3, 6]]
# b = [[70], [26], [-30], [-26]]
# eliminacion_gaussiana(a, b)
# print(eliminacion_gaussiana(a, b))
