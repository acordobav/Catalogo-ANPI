from scipy import linalg
from s3_sol_sist_ecuaciones_lineales_directos.sustitucion import sustitucion_adelante
from s3_sol_sist_ecuaciones_lineales_directos.sustitucion import sustitucion_atras


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

    # Se calculan las matrices L y U del sistema
    matriz_i, matriz_l, matriz_u = linalg.lu(matriz_a)

    # Se resuelve el sistema L y = b utilizando una sustitucion hacia adelante
    matriz_y = sustitucion_adelante(matriz_l, matriz_b)

    # Se resuelve el sistema U x = y utilizando una sustitucion hacia atras
    matriz_x = sustitucion_atras(matriz_u, matriz_y)

    return matriz_x


# a = [[4, -2, 1], [20, -7, 12], [-8, 13, 17]]
# b = [[11], [70], [17]]
# print(factorizacion_lu(a, b))
# 
# a1 = [[2, 3, 4], [4, 5, 10], [4, 8, 2]]
# b1 = [[6], [16], [2]]
# print(factorizacion_lu(a1, b1))
