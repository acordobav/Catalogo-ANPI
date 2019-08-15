from sympy import sympify

"""
Metodo de la biseccion para encontrar el cero de una funcion matematica
:param a: limite izquierdo del intervalo
:param b: limite derecho de la funcion
:param tol: tolerancia al fallo que debe tener el resultado final
:param f: funcion que se desea biseccionar
:returns: lista con dos elementos, x_aprox obtenido y numero de iteraciones
"""


def biseccion(a, b, tol, f):
    funcion = sympify(f)  # Se obtiene la funcion a partir del string

    # Se verifica si el intervalo cumple el TB
    multi0 = float(funcion.subs({'x': a}) * funcion.subs({'x': b}))
    if not multi0 <= 0:
        return ["La funcion no cumple con el Teorema de Bolzano", 0]

    itr = 1

    while True:
        x_aprox = (a + b) / 2  # Calculo del x_aprox

        # Se verifica si el x_aprox cumple la condicion de parada
        if abs(funcion.subs({'x': x_aprox})) <= tol:
            break

        # Se almacena el resultado de la multiplicacion en una variable
        multi = funcion.subs({'x': a}) * funcion.subs({'x': b})

        # Se verifica si se cumple el Teorema de Bolzano
        if multi <= 0:
            itr += 1  # Se aumenta el contador de iteraciones

            # Se verifica la condicion en el intervalo de [a, xk]
            multi_intervalo1 = funcion.subs({'x': a}) * funcion.subs({'x': x_aprox})
            if multi_intervalo1 <= 0:
                b = x_aprox

            else:
                # Intervalo1 no cumple, se verifica si el intervalo2 lo cumple
                multi_intervalo2 = funcion.subs({'x': x_aprox}) * funcion.subs({'x': b})
                if multi_intervalo2 <= 0:
                    a = x_aprox

    return [x_aprox, itr]

# f = 'exp(x) - x - 2'
# biseccion(0, 2, 10**-5, f)
