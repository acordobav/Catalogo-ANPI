%{
Funcion principal que hace un llamado a la funcion auxiliar que implementa el metodo de la biseccion
para encontrar el cero de una funcion matematica.
:param a: limite izquierdo del intervalo en el eje x
:param b: limite derecho del intervalo en el eje x
:param tol: tolerancia al fallo que debe tener el resultado final
:param f: funcion que se debe evaluar
:returns: Xaprox que corresponda al valor aproximado en x donde se encuentra un cero, iter que corresponde
          al numero de iteraciones que necesito el algoritmo para encontrar el resultado
%}
function [Xaprox, iter] = biseccion(a, b, tol, f)
    xa = (a + b) / 2;
    [Xaprox, iter] = biseccionAux(a, b, tol, f, xa, 0);
end

%{
Funcion auxiliar que implementa el metodo de la biseccion para encontrar el cero de una funcion matematica.
:param a: limite izquierdo del intervalo en el eje x
:param b: limite derecho del intervalo en el eje x
:param tol: tolerancia al fallo que debe tener el resultado final
:param f: funcion que se debe evaluar
:param xa: xk calculado en la iteracion anterior
:returns: Xaprox que corresponda al valor aproximado en x donde se encuentra un cero, iter que corresponde
          al numero de iteraciones que necesito el algoritmo para encontrar el resultado
%}
function [Xaprox, iter] = biseccionAux(a, b, tol, f, xa, itr)
    %Se obtiene la funcion a partir del string ingresado
    funcion = str2func(f)

    %Se verifica la condicion de parada del algoritmo
    if abs(funcion(xa)) <= tol
        Xaprox = xa;
        iter = itr;

    else
        %Se verifica si se cumple el Teorema de Bolzano
        multi = funcion(a) * funcion(b);
        if multi <= 0
            %Se calcula xk, variable que se utiliza para dividir el intervalo en dos
            xk = (a + b) / 2;

            %Se verifica si el intervalo [a, xk] cumple con el Teorema de Bolzano
            multiIntervalo1 = funcion(a) * funcion(xk);
            if multiIntervalo1 <= 0
                [Xaprox, iter] = biseccionAux(a, xk, tol, f, xk, itr+1);
            end

            %Se verifica si el intervalo [xk, b] cumple con el Teorema de Bolzano
            multiIntervalo2 = funcion(xk) * funcion(b);
            if multiIntervalo2 <= 0
                [Xaprox, iter] = biseccionAux(xk, b, tol, f, xk, itr+1);
            end

        else
            %Si la funcion no cumple con el Teorema de Bolzano se le indica al usuario
            Xaprox = 'La funcion no cumple con el Teorema de Bolzano.';
            iter = 0;
        end %End multi <= 0

    end %End condicion de parada
end %End biseccionAux

%{
str = '@(x)exp(x) - x - 2';
[a, b] = biseccion(0, 2, 0.24034295746184142, str)
%}
