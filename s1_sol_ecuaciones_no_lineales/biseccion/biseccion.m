pkg load symbolic

%{
Metodo de la biseccion para encontrar el cero de una funcion matematica
:param a: limite izquierdo del intervalo
:param b: limite derecho de la funcion
:param tol: tolerancia al fallo que debe tener el resultado final
:param str_funcion: string con la funcion que se desea evaluar
:returns: lista con dos elementos, x_aprox obtenido y numero de iteraciones
%}
function [x_aprox, iter] = biseccion(a, b, tol, str_funcion)
    % Se obtiene la funcion a partir del string
    funcion = matlabFunction(sym(str_funcion));

    if ~(funcion(a) * funcion(b) <= 0)
        x_aprox = 'La funcion no cumple con el Teorema de Bolzano.';
        iter = 0;
    end % ~(funcion(a) * funcion(b) <= 0)

    itr = 1;

    while 1
        xk = (a + b) / 2; % Calculo del x_aprox

        % Se verifica la condicion de parada del algoritmo
        if abs(funcion(xk)) <= tol
            break;
        end

        % Se verifica si se cumple el Teorema de Bolzano
        if funcion(a) * funcion(b) <= 0
            itr = itr + 1;

            % Se verifica la condicion en el intervalo de [a, xk]
            if funcion(a) * funcion(xk) <= 0
                b = xk;

            else
                % Intervalo1 no cumple, se verifica si el intervalo2 lo cumple
                if funcion(xk) * funcion(b) <= 0
                    a = xk;
                end % funcion(xk) * funcion(b) <= 0

            end % funcion(a) * funcion(xk) <= 0

        end % funcion(a) * funcion(b) <= 0

    end % while 1

    x_aprox = xk;
    iter = itr;

end % End biseccion(a, b, tol, f)


%{
funcion1 = 'cos(x)-x';
disp(funcion1)
[x_aprox1, iter1] = biseccion(1 / 2, 3.14159 / 4, 10^-5, funcion1)
disp(x_aprox1);
disp(iter1);

funcion2 = 'exp(x) - x - 2';
disp(funcion2)
[x_aprox2, iter2] = biseccion(0, 2, 10^-5 , funcion2)
disp(x_aprox2);
disp(iter2);
%}
