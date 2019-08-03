pkg load symbolic


%{
Funcion que se encarga de encontrar el cero de una funcion utilizando el metodo de Newton-Raphson
:param f: funcion a la que se le desea encontrar el cero
:param x0: valor inicial de x en el cual se empieza a buscar el cero
:param tol: tolerancia al fallo que debe tener el resultado final
:returns: xAprox corresponde al valor en el eje x donde se encuentra el cero
          iter corresponde a las iteraciones que realizo el algoritmo para encontrar el resultado
%}
function [xAprox, iter] = newton_raphson(f, x0, tol)
    %Se hace un llamado a la funcion auxiliar, estableciendo los valores iniciales de los argumentos
    [xAprox, iter] = newton_raphsonAux(f, x0, tol, 0, [], []);
end % End newton_raphson

%{
Funcion auxiliar que implementa el metodo de Newton-Raphson para encontrar el cero de una funcion
:param f: funcion a la que se le desea encontrar el cero
:param x0: valor inicial de x en el cual se empieza a buscar el cero
:param tol: tolerancia al fallo que debe tener el resultado final
:returns: xAprox corresponde al valor en el eje x donde se encuentra el cero
          iter corresponde a las iteraciones que realizo el algoritmo para encontrar el resultado
%}
function [xAprox, iter] = newton_raphsonAux(strFuncion, xkAnterior, tol, itr, listaError, listaIter)
    %Se obtiene la funcion ingresada por el usuario
    f = matlabFunction(sym(strFuncion));

    %Se calcula el valor de la funcion en el xk calculado anteriormente
    fxk = f(xkAnterior);

    %Se verifica si la tolerancia al fallo ha sido alcanzada
    if abs(f(xkAnterior)) <= tol
        xAprox = xkAnterior;
        iter = itr;


    else
        %Se calcula la derivada de la funcion ingresada
        df = matlabFunction(diff(sym(strFuncion)));
        %Se calcula el proximo valor de xk a partir del valor anterior
        xkSiguiente = xkAnterior - (f(xkAnterior)/df(xkAnterior));

        [xAprox, iter] = newton_raphsonAux(f, xkSiguiente, tol, itr + 1, listaIter, listaError);

    end % End if abs(fxk) <= tol;

end % End newton_raphsonAux

%{
f = 'cos(2*x)^2 - x^2'
[xAprox, iter] = newton_raphson(f, 3/4, 0.0001)
%}
