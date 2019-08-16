from sympy import sympify

"""
Funcion que implementa el metodo de la secante
:param str_funcion: string con la funcion que se debe evaluar
:param xk_anterior2: valor de xk de la iteracion inicial
:param xk_anterior1: valor de xk de la segunda iteracion
:param tol: tolerancia al fallo que debe cumplir el resultado
:returns: lista con dos elementos, xk calculado y numero iteraciones
"""


def secante(str_funcion, xk_anterior2, xk_anterior1, tol):
    funcion = sympify(str_funcion)  # Se obtiene la funcion ingresada por el usuario
    itr = 0  # Se inicializa el contador del numero de iteraciones

    # While infinito que se rompe al cumplir la condicion de parada
    while True:
        # Se calcula el xk de la iteracion actual
        xk = float(xk_anterior1 - (funcion.subs({'x': xk_anterior1}) * (xk_anterior1 - xk_anterior2)) /
                   (funcion.subs({'x': xk_anterior1}) - funcion.subs({'x': xk_anterior2})))

        # Se evalua la funcion en el valor de xk
        fxk = float(funcion.subs({'x': xk}))

        # Se verifica si se cumple la condicion de parada
        if abs(fxk) <= tol:
            break

        # No cumple condicion de parada, ajuste de variables para sig iteracion
        xk_anterior2 = xk_anterior1
        xk_anterior1 = xk
        itr += 1

    return [xk, itr]


# funcion1 = 'exp(2*x) - 10 - log(x/2)'
# print(funcion1)
# print(secante(funcion1, 1, 1.2, 10 ** -2))
# print()
#
# funcion2 = 'cos(2*x)^2 - x^2'
# print(funcion2)
# print(secante(funcion2, 2 / 4, 3 / 4, 10 ** -5))
# print()
