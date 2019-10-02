from sympy import Symbol, solve
from numpy import linalg, matrix


def iteracion_jacobi(matriz_a, matriz_b, tol):
    """
    Funcion que implementa el metodo iterativo de Jacobi para resolver el
    sistema A x = b
    :param matriz_a: Matriz cuadrada
    :param matriz_b: Vector columna
    :param tol: Tolerancia al fallo que debe tener el vector resultado
    :return: Vector resultado
    """
    n = len(matriz_a)       # Numero de filas
    m = len(matriz_a[0])    # Numero de columnas

    if n != m:
        return "matriz_a debe ser cuadrada"

    x = Symbol('x')  # Variable simbolica para aplicar el metodo
    vec_x = [0] * m  # Vector x que resuelve el sistema A x = b

    while 1:
        vec_x_ant = vec_x.copy()  # Vector de la iteracion anterior
        for i in range(0, n):
            ecuacion = matriz_b[i][0]
            for j in range(0, m):
                if i == j:
                    # Elemento en la diagonal, se multiplica por la variable
                    ecuacion -= matriz_a[i][j] * x
                else:
                    # Se multiplica por el valor respectivo en el vector anterior
                    ecuacion -= matriz_a[i][j] * vec_x_ant[i]

            # Se actualiza el vector con la solucion obtenida
            vec_x[i] = float(solve(ecuacion)[0])

        # Condicion de parada
        vec_parada = [x1 - x2 for (x1, x2) in zip(vec_x, vec_x_ant)]
        norma_2 = linalg.norm(vec_parada, 2)

        if norma_2 < tol:
            break

    # Se construye un vector columna a partir del vector obtenido
    vec_x = [[x1] for x1 in vec_x]

    return vec_x


# A = [[5, 1, 1], [1, 5, 1], [1, 1, 5]]
# b = [[7], [7], [7]]
# resultado = iteracion_jacobi(A, b, 10 ** -5)
# print(resultado)

# A = [[3, 1, 1], [1, 3, 1], [1, 1, 3]]
# b = [[5], [5], [5]]
# resultado = iteracion_jacobi(A, b, 10 ** -5)
# print(resultado)
