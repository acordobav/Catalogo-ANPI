from numpy import transpose, linalg, array
from s3_sol_sist_ecuaciones_lineales.metodos_directos.sustitucion import sustitucion_adelante
from s3_sol_sist_ecuaciones_lineales.metodos_directos.sustitucion import sustitucion_atras


def factorizacion_cholesky(matriz_a, matriz_b):
    """
    Metodo Factorizacion de Cholesky para resolver un sistema A x = B
    :param matriz_a: matriz cuadrada de nxn
    :param matriz_b: matriz columna de nx1
    :return: matriz x que resuelve el sistema A x = b
    """
    # Se verifica que la matriz A tenga simetria
    ma_transpuesta = transpose(matriz_a)
    norma_a = linalg.norm(array(matriz_a, dtype='float'))
    norma_a_t = linalg.norm(array(ma_transpuesta, dtype='float'))
    if norma_a - norma_a_t != 0:
        return "Error: La matriz_a debe ser simetrica"

    # Se calcula la factorizacion de Cholesky para la matriz_a
    matriz_l = linalg.cholesky(matriz_a)
    matriz_l_t = transpose(matriz_l)

    # Se resuelve el sistema L y = b utilizando una sustitucion hacia adelante
    matriz_y = sustitucion_adelante(matriz_l, matriz_b)

    # Se resuelve el sistema Lt x = y utilizando una sustitucion hacia adelante
    matriz_x = sustitucion_atras(matriz_l_t, matriz_y)

    return matriz_x


# a = [[25, 15, -5, -10], [15, 10, 1, -7], [-5, 1, 21, 4], [-10, -7, 4, 18]]
# b = [[-25], [-19], [-21], [-5]]
# print(factorizacion_cholesky(a, b))
