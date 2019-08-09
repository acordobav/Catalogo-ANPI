from sympy import Derivative, sympify

'''
Funcion que implementa el metodo de Newton-Raphson para encontrar el cero de una funcion
:param f: string con la funcion que se debe evaluar
:param x0: valor de x inicial con el cual aplicar el metodo
:param tol: tolerancia al fallo de debe tener el resultado final
:returns: lista con dos elementos, donde el primero corresponde al valor de x obtenido con el metodo,
          y el segundo elemento es el numero de iteraciones que realizo el algoritmo para encontrar
          el resultado final.
'''
def newton_raphson(f, x0, tol):
    #Se obtiene la funcion a partir del string ingresado por el usuario
    funcion = sympify(f)

    # Se hace un llamado a la funcion auxiliar
    return newton_raphsonAux(funcion, x0, tol, 0)


'''
Funcion auxiliar que implementa el metodo de Newton-Raphson para encontrar el cero de una funcion
:param funcion: funcion que se debe evaluar
:param x0: valor de x inicial con el cual aplicar el metodo
:param tol: tolerancia al fallo de debe tener el resultado final
:param itr: contador con el numero de iteraciones que ha realizado el algoritmo
:returns: lista con dos elementos, donde el primero corresponde al valor de x obtenido con el metodo,
          y el segundo elemento es el numero de iteraciones que realizo el algoritmo para encontrar
          el resultado final.
'''
def newton_raphsonAux(funcion, xk, tol, itr):
    #Se evalua la funcion en el valor de xk
    fxk = funcion.subs({'x':xk})

    #Se verifica si se cumple la condicion de parada
    if (abs(fxk) <= tol):
        return [xk, itr]

    else:
        #Se deriva la funcion ingresada por el usuario
        df = Derivative(funcion, 'x');

        #Se calcula el xk de la siguiente iteracion
        xkSiguiente = xk - fxk/(df.doit().subs({'x':xk}))

        return newton_raphsonAux(funcion, xkSiguiente, tol, itr + 1)


# function1 = 'cos(2*x)^2 - x^2'
# function2 = 'exp(x) - x^3 - x'
# newton_raphson(function, 3/4, 0.0001)
