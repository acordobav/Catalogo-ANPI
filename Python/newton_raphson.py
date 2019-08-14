from sympy import Derivative, sympify
from matplotlib import pyplot as plt

'''
Funcion que implementa el metodo de Newton-Raphson para encontrar el cero de una funcion
:param f: string con la funcion que se debe evaluar
:param xk: valor de x inicial con el cual aplicar el metodo
:param tol: tolerancia al fallo de debe tener el resultado final
:returns: lista con dos elementos, donde el primero corresponde al valor de x obtenido con el metodo,
          y el segundo elemento es el numero de iteraciones que realizo el algoritmo para encontrar
          el resultado final.
'''
def newton_raphson(f, xk, tol):
    funcion = sympify(f)  # Se obtiene la funcion a partir del string ingresado por el usuario
    df = Derivative(funcion, 'x')  # Se deriva la funcion ingresada por el usuario
    itr = 0  # Se inicializa el contador de iteraciones

    # Se inicializan las lista donde se guardaran los valores para la grafica de error
    listaXk = []
    listaIter = []

    while 1:
        fxk = float(funcion.subs({'x': xk}))

        # Se guardan los valores para la grafica
        listaXk += [abs(fxk)]
        listaIter += [itr]

        if abs(fxk) <= tol:  # Se verifica si se cumple la condicion de parada
            break;

        else:
            xk = float(xk - fxk / (df.doit().subs({'x': xk})))  # Se calcula el xk de la siguiente iteracion
            itr += 1  # Se aumenta el numero de iteraciones

    graficarError(listaIter, listaXk)

    return [xk, itr]

"""
Funcion para realizar la grafica del error en el metodo Newton-Raphson
:param x: lista con todos los valores que deben graficarse en el eje x
:param y: lista con todos los valores que deben graficarse en el eje y
"""
def graficarError(x, y):
    plt.plot(x, y)  # Se asignan los valores a los ejes de coordenadas
    plt.xlabel('Iteracion')  # Se le coloca un nombre al eje x
    plt.ylabel('| f(xk) |')  # Se le coloca un nombre al eje y
    plt.show()  # Se despliega el grafico

# function1 = 'cos(2*x)^2 - x^2'
# function2 = 'exp(x) - x^3 - x'
# newton_raphson(function1, 3/4, 0.0001)
