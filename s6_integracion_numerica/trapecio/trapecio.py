from sympy import sympify


def trapecio(funcion, a, b):
    """
    Regla del trapecio para calcular la integral de una funcion
    :param funcion: Funcion a integrar
    :param a: Limite inferior
    :param b: Limite superior
    :return: Resultado obtenido
    """
    f = sympify(funcion)  # Se crea una funcion
    h = b - a  # Se calcula el h
    fa = float(f.subs({'x': a}).doit())  # Se calcula f(a)
    fb = float(f.subs({'x': b}).doit())  # Se calcula f(b)
    return (h / 2) * (fa + fb)


# f1 = "ln(x)"
# resultado = trapecio(f1, 2, 5)
# print(resultado)

# f1 = "13 / (5 * x + 4)"
# resultado = trapecio(f1, 1, 2)
# print(resultado)
