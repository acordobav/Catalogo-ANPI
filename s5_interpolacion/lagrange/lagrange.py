from sympy import Symbol, expand


def lagrange(lista_puntos):
    """
    Metodo de interpolacion de Lagrange
    :param lista_puntos: Los puntos deben ser ingresados en una lista, donde cada punto
    es una lista, donde la primera posicion es el x, y la segunda posicion es el y. [x, y]
    :return: Polinomio de interpolacion obtenido
    """
    n = len(lista_puntos)  # Cantidad de puntos
    x = Symbol('x')        # Variable simbolica
    polinomio = 0          # Polinomio de interpolacion

    # Se recorre cada punto en la lista ingresada
    for i in range(0, n):
        punto = lista_puntos[i]  # Punto actual
        lk = 1
        # Calculo de Lk(x)
        for j in range(0, n):
            if i != j:
                # Se obtiene el xj
                xj = lista_puntos[j][0]
                # Se calcula el producto actual
                lk *= (x - xj) / (punto[0] - xj)

        # Calculo de Pn(x)
        polinomio += punto[1] * lk

    return expand(polinomio)


# lista_p = [[-2, 0], [0, 1], [1, -1]]
# resultado = lagrange(lista_p)
# print(resultado)

# lista_p = [[1, 2 / 3], [3, 1], [5, -1], [6, 0]]
# resultado = lagrange(lista_p)
# print(resultado)
