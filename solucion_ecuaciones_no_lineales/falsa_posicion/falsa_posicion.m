pkg load symbolic

%{
Funcion que se encarga de calcular el xk+1 utilizando el metodo de la secante
:param funcion: funcion que se debe evaluar
:param xk: xk de la iteracion anterior
:param ck: limite izquierdo del intervalo si se seleeciona [ak, xk],
           limite derecho del intervalo si se selecciona [xk, ck]
:returns: se retorna el xk+1 calculado
%}
function [xk1] = xk_secante(funcion, xk, ck)
    % Se calcula el xk+1 utilizando el metodo de la secante
    xk1 = xk - (funcion(xk) * (xk - ck)) / (funcion(xk) - funcion(ck));
end % xk_secante(funcion, xk, ck)

%{
Metodo de  falsa posicion para encontrar el cero de una funcion
:param str_funcion: funcion que se debe evaluar
:param a: limite izquierdo del intervalo
:param b: limite derecho del intervalo
:param tol: tolerancia al fallo del resultado, numero entre cero y uno
:returns: lista con dos elementos, x_aprox obtenido y numero de iteraciones
%}
function [x_aprox, iter] = falsa_posicion(str_funcion, a, b, tol)
    funcion = matlabFunction(sym(str_funcion)); % Se obtiene la funcion ingresada por el usuario
    itr = 0; % Se inicializa el contador de iteraciones
    xk = xk_secante(funcion, b, a); % Se calcula el xk inicial

    intervalo0 = funcion(a) * funcion(b); % Se verifica si en el intervalo existe un cero
    if ~(intervalo0 < 0)
        x_aprox = "La funcion no garantiza la existencia de un cero en el intervalo ingresado";
        iter = 0;
    end % ~(intervalo0 < 0)

    while 1
        % Se verifica la condicion de parada
        if abs(funcion(xk)) <= tol
            break;
        end % abs(funcion(xk)) <= tol

        % Verifica si primer intervalo garantiza la existencia de un cero
        intervalo1 = funcion(a) * funcion(xk);
        if intervalo1 < 0
            b = xk; %Se define el nuevo limite derecho
            itr = itr + 1; %Se aumenta el contador de iteraciones
            xk = xk_secante(funcion, xk, a); %Se calcula el nuevo xk

        else
            a = xk; %Se define el nuevo limite izquierdo
            itr = itr + 1; %Se aumenta el contador de iteraciones
            xk = xk_secante(funcion, xk, b); %Se calcula el nuevo xk
        end % intervalo1 < 0
    end % while 1

        %Se retornan los valores obtenidos
        x_aprox = xk;
        iter = itr;

end %falsa_posicion(f, a, b, tol)


%{
funcion1 = 'cos(x)-x';
disp(funcion1);
[x_aprox1, iter1] = falsa_posicion(funcion1, 1/2, pi, 10^-5)
disp(x_aprox1);
disp(iter1);

funcion2 = 'exp(x) - x - 2'
disp(funcion2);
[x_aprox2, iter2] = falsa_posicion(funcion2, 0, 2, 10^-5)
disp(x_aprox2);
disp(iter2);
%}
