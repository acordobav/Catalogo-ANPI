pkg load symbolic

%{
Metodo de la biseccion para encontrar el cero de una funcion matematica
:param a: limite izquierdo del intervalo
:param b: limite derecho de la funcion
:param tol: tolerancia al fallo que debe tener el resultado final
:param f: funcion que se desea biseccionar
:returns: lista con dos elementos, x_aprox obtenido y numero de iteraciones
%}
function [Xaprox, iter] = biseccion(a, b, tol, f)
    xk = (a + b) / 2;  % Calculo del x_aprox inicial
    [Xaprox, iter] = biseccion_aux(a, b, tol, f, xk, 0);
end

%{
Metodo auxiliar del metodo de la biseccion
:param a: limite izquierdo del intervalo en el eje x
:param b: limite derecho de la funcion en el eje x
:param tol: tolerancia al fallo que debe tener el resultado final
:param funcion: funcion que se desea biseccionar
:param x_anterior: xk calculado en iteraciones anteriores de la funcion
:param itr: numero total de iteraciones
:returns: lista con dos elementos, x_aprox obtenido y numero de iteraciones
%}
function [x_aprox, iter] = biseccion_aux(a, b, tol, f, x_anterior, itr)
    % Se obtiene la funcion a partir del string
    funcion = matlabFunction(sym(f));

    % Se verifica la condicion de parada del algoritmo
    if abs(funcion(x_anterior)) <= tol
        x_aprox = x_anterior;
        iter = itr;

    else
        % Se verifica si se cumple el Teorema de Bolzano
        multi = funcion(a) * funcion(b);
        if multi <= 0
            % Se calcula xk, para dividir el intervalo en dos
            xk = (a + b) / 2;

            % Se verifica la condicion en el intervalo de [a, xk]
            multiIntervalo1 = funcion(a) * funcion(xk);
            if multiIntervalo1 <= 0
                [x_aprox, iter] = biseccion_aux(a, xk, tol, f, xk, itr+1);
            end

            % Intervalo1 no cumple, se verifica si el intervalo2 lo cumple
            multiIntervalo2 = funcion(xk) * funcion(b);
            if multiIntervalo2 <= 0
                [x_aprox, iter] = biseccion_aux(xk, b, tol, f, xk, itr+1);
            end

        else
            % Funcion no cumple el Teorema de Bolzano en el intervalo ingresado
            x_aprox = 'La funcion no cumple con el Teorema de Bolzano.';
            iter = 0;
        end % End multi <= 0

    end % if abs(funcion(x_anterior)) <= tol
end % End biseccion_aux


%{
str = 'exp(x) - x - 2';
[a, b] = biseccion(0, 2, 0.24034295746184142, str)
%}
