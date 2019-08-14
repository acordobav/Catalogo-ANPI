from sympy import Derivative, sympify
from matplotlib import pyplot as plt

"""
Metodo de Newton-Raphson para encontrar el cero de una funcion
:param f: string con la funcion que se debe evaluar
:param xk: valor de x inicial con el cual aplicar el metodo
:param tol: tolerancia al fallo de debe tener el resultado final
:returns: lista con dos elementos, xk calculado y numero iteraciones
"""


def newton_raphson(f, xk, tol):
    funcion = sympify(f)  # Se obtiene la funcion a partir del string
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
:param x: lista con todos los valores que deben graficarse en el eje x
:param y: lista con todos los valores que deben graficarse en el eje y
"""


def graficar_error(x, y):
    plt.plot(x, y)  # Se asignan los valores a los ejes de coordenadas
    plt.xlabel('Iteracion')  # Se le coloca un nombre al eje x
    plt.ylabel('| f(xk) |')  # Se le coloca un nombre al eje y
    plt.show()  # Se despliega el grafico


# function1 = 'cos(2*x)^2 - x^2'
# function2 = 'exp(x) - x^3 - x'
# newton_raphson(function1, 3/4, 0.0001)
