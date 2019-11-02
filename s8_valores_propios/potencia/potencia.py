from numpy import matrix, linalg, inf


def potencia(A, x, tol):
    """
    Metodo de la potencia para obtener el autovalor dominante de una matriz A
    :param A: Matriz A
    :param x: x0 inicial
    :param tol: Tolerancia al fallo que debe tener el resultado
    :return: Autovalor dominante
    """
    A = matrix(A)  # Matriz A
    x = matrix(x)  # Matrix x
    norma_inf_ant = 0  # Resultado de la norma de la iteracion anterior
    while 1:
        y = A * x  # Calculo de y

        # Calculo de la norma infinita
        norma_inf = linalg.norm(y, inf)
        y = y / norma_inf

        c = abs(norma_inf_ant - norma_inf)
        v = linalg.norm(x - y)
        error = max(c, v)

        # Verificacion de la condicion de parada error < tol
        if error < tol:
            break
        norma_inf_ant = norma_inf
        x = y

    return norma_inf


# resultado = potencia([[1.5, 0.5], [0.5, 1.5]], [[0], [1]], 10 ** -5)
# print(resultado)
