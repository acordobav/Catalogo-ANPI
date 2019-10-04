from numpy import linalg, transpose, matrix, eye


def solv_sist_pinv(matriz_a, matriz_b, tol):
    """
    Solucion de sistemas de ecuaciones con el uso de pseudoinversa
    :param matriz_a: Matriz A
    :param matriz_b: Matriz b
    :param tol: Tolerancia que debe cumplir el resultado
    :return: Solucion del sistema A x = b
    """
    if tol < 0:
        return "La tolerancia debe ser mayor a cero"

    matriz_b = matrix(matriz_b)

    # Calculo de la pseudoinversa de matriz_a
    a_t = pseudoinversa_sbi(matriz_a, tol)

    # Calculo de la solucion del sistema
    x = a_t * matriz_b

    return x


def pseudoinversa_sbi(matriz_a, tol):
    """
    Metodo iterativo para encontrar la pseudoinversa de una matriz
    :param matriz_a: Matriz a la que calcularle la pseudoinversa
    :param tol: Tolerancia al fallo que debe cumplir el resultado
    :return: Matriz pseudoinversa aproximada
    """
    n = len(matriz_a)       # Numero de filas
    m = len(matriz_a[0])    # Numero de columnas
    matriz_a = matrix(matriz_a)

    a_t = transpose(matriz_a)  # Matriz transpuesta de matriz_a
    norma_2 = linalg.norm(matriz_a)
    xk = (1 / (norma_2 ** 2)) * a_t  # x inicial
    m_identidad = eye(n, n)  # matriz identidad de n x n

    while 1:
        # Calculo del nuevo valor de xk
        xk = xk * (2 * m_identidad - matriz_a * xk)

        # Condicion de parada
        m_cparada = matriz_a * xk * matriz_a - matriz_a
        norma_2 = linalg.norm(m_cparada)
        if norma_2 < tol:
            break

    return xk


# A = [[1, 3, 9], [8, 9, 7]]
# resultado = pseudoinversa_sbi(A, 10 ** -5)
# print(resultado)

# A = [[1, 3, 9], [8, 9, 7]]
# b = [[8], [24]]
# resultado = solv_sist_pinv(A, b, 10 ** -5)
# print(resultado)
