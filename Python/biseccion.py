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
    x_aprox = (a + b) / 2  # Calculo del x_aprox inicial
    funcion = sympify(f)  # Se obtiene la funcion a partir del string
    return biseccion_aux(a, b, tol, funcion, x_aprox, 0)


"""
Metodo auxiliar del metodo de la biseccion
:param a: limite izquierdo del intervalo en el eje x
:param b: limite derecho de la funcion en el eje x
:param tol: tolerancia al fallo que debe tener el resultado final
:param funcion: funcion que se desea biseccionar
:param x_aprox: xk calculado en iteraciones anteriores de la funcion
:param itr: numero total de iteraciones
:returns: lista con dos elementos, x_aprox obtenido y numero de iteraciones
"""


def biseccion_aux(a, b, tol, funcion, x_aprox, itr):
    # Se verifica si el x_aprox cumple la condicion de parada
    if abs(funcion.subs({'x': x_aprox})) <= tol:
        return [x_aprox, itr]

    # Se almacena el resultado de la multiplicacion en una variable
    multi = funcion.subs({'x': a}) * funcion.subs({'x': b})

    # Se verifica si se cumple el Teorema de Bolzano
    if multi <= 0:
        # Se calcula xk, para dividir el intervalo en dos
        xk = (a + b) / 2

        # Se verifica la condicion en el intervalo de [a, xk]
        multi_intervalo1 = funcion.subs({'x': a}) * funcion.subs({'x': xk})
        if multi_intervalo1 <= 0:
            # Llamado recursivo utilizando xk como limite derecho del intervalo
            return biseccion_aux(a, xk, tol, funcion, xk, itr + 1)

        # Intervalo1 no cumple, se verifica si el intervalo2 lo cumple
        multi_intervalo2 = funcion.subs({'x': xk}) * funcion.subs({'x': b})
        if multi_intervalo2 <= 0:
            # Llamado recursivo, se usa xk como limite izquierdo del intervalo
            return biseccion_aux(xk, b, tol, funcion, xk, itr + 1)

    # Funcion no cumple el Teorema de Bolzano en el intervalo ingresado
    return "La funcion no cumple con el Teorema de Bolzano. Iteraciones: 0"

# f = 'exp(x) - x - 2'
# biseccion(0, 2, 10**-5, f)
