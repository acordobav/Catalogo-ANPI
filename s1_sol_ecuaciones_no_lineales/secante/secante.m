pkg load symbolic

%{
Funcion que implementa el metodo de la secante
:param str_funcion: string con la funcion que se debe evaluar
:param xk_ante2: valor de xk de la iteracion inicial
:param xk_ante1: valor de xk de la segunda iteracion
:param tol: tolerancia al fallo que debe cumplir el resultado
:returns: lista con dos elementos, xk calculado y numero iteraciones
%}
function [x_aprox, iter] = secante(str_funcion, xk_ante2, xk_ante1, tol)
    funcion = matlabFunction(sym(str_funcion)); % Se obtiene la funcion ingresada por el usuario
    itr = 0 % Se inicializa el contador del numero de iteraciones

    % While infinito que se rompe al cumplir la condicion de parada
    while 1
        % Se calcula el xk de la iteracion actual
        xk = xk_ante1 - ((funcion(xk_ante1)*(xk_ante1-xk_ante2))/(funcion(xk_ante1)-funcion(xk_ante2)));

        % Se evalua la funcion en el valor de xk
        fxk = funcion(xk);

        % Se verifica la condicion de parada
        if(abs(fxk) <= tol)
            break; % Se rompe el bucle infinito

        end % End if(abs(fxk) <= 0)

        % No cumple condicion de parada, ajuste de variables para sig iteracion
        xk_ante2 = xk_ante1;
        xk_ante1 = xk;
        itr = itr + 1;

    end % End While

    x_aprox = xk;
    iter = itr;

end % secante(f, xk_ante2, xk_ante1, tol)



%{
funcion1 = 'exp(2*x) - 10 - log(x/2)';
disp(funcion1);
[x_aprox1, iter1] = secante(funcion1, 1, 1.2, 10^-2)
disp(x_aprox1);
disp(iter1);


funcion2 = 'cos(2*x)^2 - x^2';
disp(funcion2);
[x_aprox2, iter2] = secante(funcion2, 2 / 4, 3 / 4, 10^-5);
disp(x_aprox2);
disp(iter2);
%}
