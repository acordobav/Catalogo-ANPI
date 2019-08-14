from sympy import sympify
import math

"""
Funcion que se encarga de calcular el xk+1 utilizando el metodo de la secante
:param funcion: funcion que se debe evaluar
:param xk: xk de la iteracion anterior
:param ck: limite izquierdo del intervalo si se seleeciona [ak, xk],
           limite derecho del intervalo si se selecciona [xk, ck]
"""
def xkSecante(funcion, xk, ck):
    # Se calcula el xk+1 utilizando el metodo de la secante
    xk1 = float(xk - (funcion.subs({'x': xk}) * (xk - ck)) / (
                funcion.subs({'x': xk}) - funcion.subs({'x': ck})));
    return xk1

"""
Funcion que implementa el metodo de la falsa posicion para encontrar el cero de una funcion
:param f: funcion que se debe evaluar
:param a: limite izquierdo del intervalo
:param b: limite derecho del intervalo
:param tol: tolerancia al fallo que debe tener el resultado, debe ser un numero que se encuentre entre cero y uno
"""
def falsa_posicion(f, a, b, tol):
    funcion = sympify(f); #Se obtiene la funcion ingresada por el usuario
    iter = 0; #Se inicializa el contador del numero de iteraciones
    xk = xkSecante(funcion, b, a); #Se calcula el valor inicial de xk

    #Se verifica si en el intervalo ingresado existe un cero
    intervalo0 = float(funcion.subs({'x':a}) * funcion.subs({'x':b}));
    if not (intervalo0 < 0):
        return ["La funcion no cumple con el criterio para aplicar este metodo", 0];

    while True:
        #Se evalua la funcion en el valor de xk
        fxk = float(funcion.subs({'x':xk}));

        #Se verifica la condicion de parada
        if abs(fxk) <= tol:
            break; #Se termina el ciclo infinito

        #Se verifica si en el primer intervalo garantiza la existencia de un cero
        intervalo1 = funcion.subs({'x':a}) * funcion.subs({'x':xk});
        if intervalo1 < 0:
            b = xk; #Se define el nuevo limite derecho
            iter += 1; #Se aumenta el contador
            xk = xkSecante(funcion, xk, a);

        else:
            # Se verifica si en el segundo intervalo garantiza la existencia de un cero
            intervalo2 = funcion.subs({'x':xk}) * funcion.subs({'x':b});
            if intervalo2 < 0:
                a = xk; #Se define el nuevo limite izquierdo
                iter += 1; #Se aumenta el contador
                xk = xkSecante(funcion, xk, b);

    return [xk, iter];

# funcion = 'cos(x)-x'
# print(falsa_posicion(funcion, 1/2, math.pi/4, 10**(-5)));