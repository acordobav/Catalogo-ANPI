from sympy import sympify

"""
Funcion principal que implementa el metodo de la biseccion para encontrar el cero de una funcion matematica
:param a: limite izquierdo del intervalo
:param b: limite derecho de la funcion
:param tol: tolerancia al fallo que debe tener el resultado final
:param f: funcion que se desea biseccionar
:returns: lista con dos elementos, el primero corresponde a el Xaprox obtenido, y el segundo al numero de iteraciones
"""
def biseccion(a, b, tol, f):
    #Se hace un llamado a una funcion auxiliar que lleva la cuenta del numero de iteraciones totales
    Xaprox = (a + b) / 2;

    # Se obtiene la funcion a partir del string ingresado por el usuario
    funcion = sympify(f)
    return biseccionAux(a, b, tol, funcion, Xaprox, 0)


"""
Funcion auxiliar que implementa el metodo de la biseccion para encontrar el cero de una funcion matematica
:param a: limite izquierdo del intervalo en el eje x
:param b: limite derecho de la funcion en el eje x
:param tol: tolerancia al fallo que debe tener el resultado final
:param funcion: funcion que se desea biseccionar
:param Xaprox: xk calculado en iteraciones anteriores de la funcion
:param itr: numero total de iteraciones
:returns: lista con dos elementos, el primero corresponde a el Xaprox obtenido, y el segundo al numero de iteraciones
"""
def biseccionAux(a, b, tol, funcion, Xaprox, itr):
    #Se verifica si el Xaprox cumple la condicion de parada
    if(abs(funcion.subs({'x':Xaprox})) <= tol):
        return [Xaprox, itr];

    #Se almacena el resultado de la multiplicacion funcion(a) * funcion(b) en una variable
    multi = funcion.subs({'x':a}) * funcion.subs({'x':b});
    
    #Se verifica si se cumple el Teorema de Bolzano
    if(multi <= 0):
        #Se calcula xk, variable que se utiliza para dividir el intervalo en dos
        xk = (a + b) / 2;

        #Se verifica si el intervalo de [a, xk] cumple con el Teorema de Bolzano;
        multiIntervalo1 = funcion.subs({'x':a}) * funcion.subs({'x':xk});
        if(multiIntervalo1 <= 0):
            #Si se cumple la condicion se hace un llamado recursivo utilizando xk como
            #nuevo limite derecho del intervalo
            return biseccionAux(a, xk, tol, funcion, xk, itr + 1);

        #En caso de que el intervalo1 no cumpla con el TB, se verifica si el intervalo2 lo cumple
        multiIntervalo2 = funcion.subs({'x':xk}) * funcion.subs({'x':b});
        if(multiIntervalo2 <= 0):
            #Si se cumple la condicion se hace un llamado recursivo utilizando xk como
            #nuevo limite izquierdo del intervalo
            return biseccionAux(xk, b, tol, funcion, xk, itr + 1);
        

    #Si la funcion no cumple el Teorema de Bolzano en el intervalo ingresado entonces
    #se le indica al usuario
    return "La funcion no cumple con el Teorema de Bolzano. Iteraciones: 0";

#f = 'exp(x) - x - 2'
#biseccion(0, 2, 10**-5, f)