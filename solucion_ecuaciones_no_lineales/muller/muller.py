import numpy as np
from sympy import sympify


"""
Metodo de Muller para encontrar el cero de una funcion
:param str_funcion: string con la funcion que se debe evaluar
:param x0: primer aproximacion inicial
:param x1: segunda aproximacion inicial
:param x2: tercera aproximacion inicial
:param tol: tolerancia al fallo que debe tener el resultado final
:returns: lista con dos elementos, x_aprox calculado y numero de iteraciones
"""


def muller(str_funcion, x0, x1, x2, tol):
    funcion = sympify(str_funcion)  # Se obtiene la funcion a partir del string
    itr = 1  # Se inicializa el contador de iteraciones

    while 1:
        # Se evalua la funcion en cada uno de los puntos ingresados
        f_x0 = float(funcion.subs({'x': x0}))
        f_x1 = float(funcion.subs({'x': x1}))
        f_x2 = float(funcion.subs({'x': x2}))

        # Se crean las matrices para representar el sistema de ecuaciones
        matrix_a = np.array([[x0 ** 2, x0, 1], [x1 ** 2, x1, 1], [x2 ** 2, x2, 1]])
        matrix_b = np.array([[f_x0], [f_x1], [f_x2]])

        if np.linalg.det(matrix_a) == 0:
            print('El determinante es cero, no se puede resolver')
            break

        # Se calculan la solucion del sistema de ecuaciones
        matrix_x = np.linalg.solve(matrix_a, matrix_b)

        # Se calcula el discriminante de la funcion cuadratica
        discr = (matrix_x[1][0] ** 2) - 4 * matrix_x[0][0] * matrix_x[2][0]

        # Se calculan los ceros de la funcion
        cero1 = (-matrix_x[1][0] + discr ** (1 / 2)) / (2 * matrix_x[0][0])
        cero2 = (-matrix_x[1][0] - discr ** (1 / 2)) / (2 * matrix_x[0][0])

        # Se calcula el promedio de los ceros a cada punto
        prom_cero1 = (abs(cero1 - x0) + abs(cero1 - x1) + abs(cero1 - x2)) / 3
        prom_cero2 = (abs(cero2 - x0) + abs(cero2 - x1) + abs(cero2 - x2)) / 3

        # Se selecciona el que tenga menor promedio
        x_aprox = cero1
        if prom_cero2 < prom_cero1:
            x_aprox = cero2

        # Se determinan los dos puntos mas cercanos al cero
        distancias = {abs(x_aprox - x0): x0, abs(x_aprox - x1): x1, abs(x_aprox - x2): x2}
        dist_ordenada = sorted(distancias)  # Se ordena la lista ascendentemente

        # Se verifica la condicion de parada
        f_x_aprox = float(funcion.subs({'x': x_aprox}))
        if abs(f_x_aprox) < tol:
            break

        # Se actualizan las variables para la nueva iteracion
        x0 = x_aprox
        x1 = distancias[dist_ordenada[0]]
        x2 = distancias[dist_ordenada[1]]
        itr += 1

    return [x_aprox, itr]


# funcion1 = 'sin(x) - x / 2'
# print("funcion = ", funcion1)
# print(muller(funcion1, 2, 2.2, 1.8, 10 ** -5))

# funcion2 = '(1 + x) * sin(x) - 1'
# print("funcion = ", funcion2)
# print(muller(funcion2, 2.9, 3, 2.8, 10 ** -5))
