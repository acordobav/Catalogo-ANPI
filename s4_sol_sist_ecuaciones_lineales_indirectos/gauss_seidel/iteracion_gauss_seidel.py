from sympy import Symbol, solve
from numpy import linalg


def iteracion_gauss_seidel(matriz_a, matriz_b, tol):
    """
    Funcion que implementa el metodo iterativo de Gauss-Seidel para resolver el
    sistema A x = b
    :param matriz_a: Matriz cuadrada diagonalmente dominante
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
                    # Se multiplica por el valor respectivo en el vector
                    ecuacion -= matriz_a[i][j] * vec_x[j]

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


# A = [[10, 3, 1], [2, -10, 3], [0, -1, 2]]
# b = [[-5], [14], [14]]
# resultado = iteracion_gauss_seidel(A, b, 10 ** -5)
# print(resultado)

# A = [[5, 3, 0], [3, -6, 2], [0, 2, -3]]
# b = [[3], [-2], [-4]]
# resultado = iteracion_gauss_seidel(A, b, 10 ** -5)
# print(resultado)
