from sympy import Derivative, sympify
from matplotlib import pyplot as plt

"""
Metodo de Newton-Raphson para encontrar el cero de una funcion
:param str_funcion: string con la funcion que se debe evaluar
:param xk: valor de x inicial con el cual aplicar el metodo
:param tol: tolerancia al fallo de debe tener el resultado final
:returns: lista con dos elementos, xk calculado y numero iteraciones
"""


def newton_raphson(str_funcion, xk, tol):
    funcion = sympify(str_funcion)  # Se obtiene la funcion a partir del string
    df = Derivative(funcion, 'x')  # Se deriva la funcion
    itr = 0  # Se inicializa el contador de iteraciones

    # Listas donde se guardaran los valores para la grafica de error
    lista_xk = []
    lista_iter = []

    while 1:
        fxk = float(funcion.subs({'x': xk}))

        # Se guardan los valores para la grafica
        lista_xk += [abs(fxk)]
        lista_iter += [itr]

        if abs(fxk) <= tol:  # Se verifica si se cumple la condicion de parada
            break

        else:
            # Se calcula el xk de la siguiente iteracion
            xk = float(xk - fxk / (df.doit().subs({'x': xk})))
            itr += 1  # Se aumenta el numero de iteraciones

    graficar_error(lista_iter, lista_xk)

    return [xk, itr]


"""
Funcion para realizar la grafica del error en el metodo Newton-Raphson
:param eje_x: lista con todos los valores que deben graficarse en el eje x
:param eje_y: lista con todos los valores que deben graficarse en el eje y
"""


def graficar_error(eje_x, eje_y):
    plt.plot(eje_x, eje_y)  # Se asignan los valores a los ejes de coordenadas
    plt.xlabel('Iteracion')  # Se le coloca un nombre al eje x
    plt.ylabel('| f(xk) |')  # Se le coloca un nombre al eje y
    plt.show()  # Se despliega el grafico


# funcion1 = 'cos(2*x)^2 - x^2'
# print(funcion1)
# print(newton_raphson(funcion1, 3 / 4, 10 ** -5))
# print()
#
# funcion2 = 'exp(x) - x^3 - x'
# print(funcion2)
# print(newton_raphson(funcion2, 3 / 4, 10 ** -5))
# print()
