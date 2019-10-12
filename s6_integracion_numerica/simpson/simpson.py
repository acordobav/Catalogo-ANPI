from sympy import sympify


def simpson(funcion, a, b):
    """
    Regla del Simpson para calcular la integral de una funcion
    :param funcion: Funcion a integrar
    :param a: Limite inferior
    :param b: Limite superior
    :return: Resultado obtenido
    """
    f = sympify(funcion)  # Se crea una funcion
    h = (b - a) / 2  # Se calcula el h
    fx0 = float(f.subs({'x': a}))  # Se calcula f(a)
    fx1 = float(f.subs({'x': (a + b) / 2}))
    fx2 = float(f.subs({'x': b}))  # Se calcula f(b)
    return (h / 3) * (fx0 + 4 * fx1 + fx2)


# f1 = "ln(x)"
# resultado = simpson(f1, 2, 5)
# print(resultado)

# f1 = "13 / (5 * x + 4)"
# resultado = simpson(f1, 1, 2)
# print(resultado)
