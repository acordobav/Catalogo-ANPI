from sympy import Symbol, expand


def newton(lista_puntos):
    """
    Diferencias Divididas de Newton para resolver un problema de interpolacion
    :param lista_puntos: Los puntos deben ser ingresados en una lista, donde cada punto
    es una lista, donde la primera posicion es el x, y la segunda posicion es el y. [x, y]
    :return: Polinomio de interpolacion obtenido
    """
    n = len(lista_puntos)  # Cantidad de puntos
    polinomio = lista_puntos[0][1]  # Polinomio de interpolacion
    resul_previos = []     # Lista para los resultados previos
    x = Symbol('x')        # Variable simbolica
    m = n - 1
    multi = 1  # Variable que almacena la multiplicacion (x-x0) * ... * (x-xn)

    for i in range(0, n):
        # Se agregan los "y" en la lista de resultados previos
        resul_previos += [lista_puntos[i][1]]

    for i in range(1, n):
        multi *= x - lista_puntos[i - 1][0]  # Se multiplica por (x - xi)
        resul_nuevos = []  # Lista para los resultados nuevos
        for j in range(0, m):
            # Se realiza el calculo de cada elemento del polinomio
            numerador = resul_previos[j] - resul_previos[j + 1]
            denominador = lista_puntos[j][0] - lista_puntos[j + i][0]
            resul_nuevos += [numerador / denominador]
        m -= 1
        # Se actualiza el polinomio
        polinomio += resul_nuevos[0] * multi
        # Se actualiza la lista de resultados previos
        resul_previos = resul_nuevos.copy()

    return expand(polinomio)


# lista_p = [[-2, 0], [0, 1], [1, -1]]
# resultado = newton(lista_p)
# print(resultado)

# lista_p = [[1, 2 / 3], [3, 1], [5, -1], [6, 0]]
# resultado = newton(lista_p)
# print(resultado)
