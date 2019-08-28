pkg load symbolic

%{
Metodo de Newton-Raphson para encontrar el cero de una funcion
:param str_funcion: string con la funcion que se debe evaluar
:param xk: valor de x inicial con el cual aplicar el metodo
:param tol: tolerancia al fallo de debe tener el resultado final
:returns: lista con dos elementos, xk calculado y numero iteraciones
%}
function [x_aprox, iter] = newton_raphson(str_funcion, xk, tol)
    f = matlabFunction(sym(str_funcion));  % Se obtiene la funcion

    % Se calcula la derivada de la funcion ingresada
    df = matlabFunction(diff(sym(f)));

    % Listas donde se guardaran los valores para la grafica de error
    lista_xk = [];
    lista_iter = [];

    itr = 0;  % Se inicializa el contador de iteraciones

    while 1
        % Calcular el valor de la funcion en el xk anterior
        fxk = f(xk);

        % Se guardan los valores para la grafica
        lista_xk = [lista_xk abs(fxk)]
        lista_iter = [lista_iter (itr)]

        if abs(f(xk)) <= tol % Se verifica si se cumple la condicion de parada
            break;

        else
            %Se calcula el proximo valor de xk a partir del valor anterior
            xk = xk - (f(xk) / df(xk));
            itr = itr + 1;
        end % End if abs(fxk) <= tol;

    end % while 1

    %Se grafica el error
    graficarError(lista_iter, lista_xk)

    x_aprox = xk;
    iter = itr;

end % End newton_raphsonAux

%{
Funcion para realizar la grafica del error en el metodo Newton-Raphson
:param lista_iter: lista con todos los valores que deben graficarse en el eje x
:param lista_xk: lista con todos los valores que deben graficarse en el eje y
%}
function graficarError(lista_iter, lista_xk)
    plot(lista_iter, lista_xk);   %Se realiza la grafica
    grid on;                      %Se activa la malla
    xlabel("iteracion")           %Se nombra el eje x
    ylabel("| f(xk) | ")          %Se nombra el eje y
end % End graficar_error


%{
funcion1 = 'cos(2*x)^2 - x^2';
disp(funcion1);
[x_aprox1, iter1] = newton_raphson(funcion1, 3/4, 10^-5);
pause(2);
disp(x_aprox1);
disp(iter1);
%}

%{
funcion2 = 'exp(x) - x^3 - x';
disp(funcion2);
[x_aprox2, iter2] = newton_raphson(funcion2, 3/4, 10^-5);
pause(2);
disp(x_aprox2);
disp(iter2);
%}
