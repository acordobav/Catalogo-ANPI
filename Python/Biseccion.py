import math

#Declaracion de la funcion que se desea evaluar
g = lambda x : math.exp(x) - x - 2;

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
    return biseccionAux(a, b, tol, f, Xaprox, 0)


"""
Funcion auxiliar que implementa el metodo de la biseccion para encontrar el cero de una funcion matematica
:param a: limite izquierdo del intervalo en el eje x
:param b: limite derecho de la funcion en el eje x
:param tol: tolerancia al fallo que debe tener el resultado final
:param f: funcion que se desea biseccionar
:param Xaprox: xk calculado en iteraciones anteriores de la funcion
:param itr: numero total de iteraciones
:returns: lista con dos elementos, el primero corresponde a el Xaprox obtenido, y el segundo al numero de iteraciones
"""
def biseccionAux(a, b, tol, f, Xaprox, itr):    
    #Se verifica si el Xaprox cumple la condicion de parada
    if(abs(f(Xaprox)) <= tol):
        return [Xaprox, itr];

    #Se almacena el resultado de la multiplicacion f(a) * f(b) en una variable
    multi = f(a) * f(b);
    
    #Se verifica si se cumple el Teorema de Bolzano
    if(multi <= 0):
        #Se calcula xk, variable que se utiliza para dividir el intervalo en dos
        xk = (a + b) / 2;

        #Se verifica si el intervalo de [a, xk] cumple con el Teorema de Bolzano;
        multiIntervalo1 = f(a) * f(xk);
        if(multiIntervalo1 <= 0):
            #Si se cumple la condicion se hace un llamado recursivo utilizando xk como
            #nuevo limite derecho del intervalo
            return biseccionAux(a, xk, tol, f, xk, itr + 1);

        #En caso de que el intervalo1 no cumpla con el TB, se verifica si el intervalo2 lo cumple
        multiIntervalo2 = f(xk) * f(b); 
        if(multiIntervalo2 <= 0):
            #Si se cumple la condicion se hace un llamado recursivo utilizando xk como
            #nuevo limite izquierdo del intervalo
            return biseccionAux(xk, b, tol, f, xk, itr + 1);
        

    #Si la funcion no cumple el Teorema de Bolzano en el intervalo ingresado entonces
    #se le indica al usuario
    return "La funcion no cumple con el Teorema de Bolzano. Iteraciones: 0";
