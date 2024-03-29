from sympy import sympify

"""
Funcion que se encarga de calcular el xk+1 utilizando el metodo de la secante
:param funcion: funcion que se debe evaluar
:param xk: xk de la iteracion anterior
:param ck: limite izquierdo del intervalo si se seleeciona [ak, xk],
           limite derecho del intervalo si se selecciona [xk, ck]
:returns: se retorna el xk+1 calculado
"""


def xk_secante(funcion, xk, ck):
    # Se calcula el xk+1 utilizando el metodo de la secante
    xk1 = float(xk - (funcion.subs({'x': xk}) * (xk - ck)) / (
            funcion.subs({'x': xk}) - funcion.subs({'x': ck})))
    return xk1


"""
Metodo de  falsa posicion para encontrar el cero de una funcion
:param str_funcion: string con la funcion que se debe evaluar
:param a: limite izquierdo del intervalo
:param b: limite derecho del intervalo
:param tol: tolerancia al fallo del resultado, numero entre cero y uno
:returns: lista con dos elementos, x_aprox obtenido y numero de iteraciones
"""


def falsa_posicion(str_funcion, a, b, tol):
    funcion = sympify(str_funcion)  # Se obtiene la funcion ingresada por el usuario
    itr = 0  # Se inicializa el contador del numero de iteraciones
    xk = xk_secante(funcion, b, a)  # Se calcula el valor inicial de xk

    # Se verifica si en el intervalo ingresado existe un cero
    intervalo0 = float(funcion.subs({'x': a}) * funcion.subs({'x': b}))
    if not (intervalo0 < 0):
        return ["Funcion no cumple con el criterio para este metodo", 0]

    while True:
        # Se evalua la funcion en el valor de xk
        fxk = float(funcion.subs({'x': xk}))

        # Se verifica la condicion de parada
        if abs(fxk) <= tol:
            break  # Se termina el ciclo infinito

        # Verifica si primer intervalo garantiza la existencia de un cero
        intervalo1 = funcion.subs({'x': a}) * funcion.subs({'x': xk})
        if intervalo1 < 0:
            b = xk  # Se define el nuevo limite derecho
            itr += 1  # Se aumenta el contador
            xk = xk_secante(funcion, xk, a)

        else:
            # Verifica si segundo intervalo garantiza la existencia de un cero
            intervalo2 = funcion.subs({'x': xk}) * funcion.subs({'x': b})
            if intervalo2 < 0:
                a = xk  # Se define el nuevo limite izquierdo
                itr += 1  # Se aumenta el contador
                xk = xk_secante(funcion, xk, b)

    return [xk, itr]


# funcion1 = 'cos(x)-x'
# print(funcion1)
# print(falsa_posicion(funcion1, 1 / 2, 3.14159 / 4, 10 ** -5))
# print()
#
# funcion2 = 'exp(x) - x - 2'
# print(funcion2)
# print(falsa_posicion(funcion2, 0, 2, 10**-5))
# print()
