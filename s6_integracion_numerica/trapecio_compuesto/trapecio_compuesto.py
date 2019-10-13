from sympy import sympify


def trapecio_compuesto(funcion, a, b, m):
    """
    Regla compuesta del trapecio para calcular la integral de una funcion
    :param funcion: Funcion a integrar
    :param a: Limite inferior
    :param b: Limite superior
    :param m: Cantidad de puntos a utilizar
    :return: Resultado obtenido
    """
    f = sympify(funcion)  # Se crea una funcion
    h = (b - a) / (m - 1)  # Se calcula el h
    x = a
    resultado = 0
    for i in range(0, m - 1):
        fxi = float(f.subs({'x': x}))  # Se calcula f(xi)
        x += h
        fxi1 = float(f.subs({'x': x}))  # Se calcula f(xi+1)
        resultado += (h / 2) * (fxi + fxi1)

    return resultado


# f1 = "ln(x)"
# resultado1 = trapecio_compuesto(f1, 2, 5, 20)
# print(resultado1)

# f1 = "exp(-x ** 2)"
# resultado = trapecio_compuesto(f1, 0, 4, 6)
# print(resultado)
