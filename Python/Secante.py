from sympy import sympify

"""
Funcion que implementa el metodo de la secante
:param f: string con la funcion que se debe evaluar
:param xkAnterior2: valor de xk de la iteracion inicial
:param xkAnterior1: valor de xk de la segunda iteracion
:param tol: tolerancia al fallo que debe cumplir el resultado
"""
def secante(f, xkAnterior2, xkAnterior1, tol):
    funcion = sympify(f); #Se obtiene la funcion ingresada por el usuario
    iter = 0; #Se inicializa el contador del numero de iteraciones

    #While infinito que se rompe al cumplir la condicion de parada
    while True:
        #Se calcula el xk de la iteracion actual
        xk = float(xkAnterior1 - (funcion.subs({'x':xkAnterior1})*(xkAnterior1 - xkAnterior2))/(funcion.subs({'x':xkAnterior1}) - funcion.subs({'x':xkAnterior2})));

        #Se evalua la funcion en el valor de xk
        fxk = float(funcion.subs({'x':xk}));

        # Se verifica si se cumple la condicion de parada
        if (abs(fxk) <= tol):
            break;

        #Si no se cumple la condicion de parada, se ajustan las variables para la siguiente iteracion
        xkAnterior2 = xkAnterior1;
        xkAnterior1 = xk;
        iter += 1;

    return [xk, iter]

#funcion = 'exp(2*x) - 10 - log(x/2)'
#print(secante(funcion, 1, 1.2, 10**-2));