pkg load symbolic

%{
Metodo de Newton-Raphson para encontrar el cero de una funcion
:param f: string con la funcion que se debe evaluar
:param xk: valor de x inicial con el cual aplicar el metodo
:param tol: tolerancia al fallo de debe tener el resultado final
:returns: lista con dos elementos, xk calculado y numero iteraciones
%}
function [xAprox, iter] = newton_raphson(f, xk, tol)
    f = matlabFunction(sym(f));  % Se obtiene la funcion

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

    xAprox = xk;
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
function1 = 'cos(2*x)^2 - x^2'
function2 = 'exp(x) - x^3 - x'
[xAprox, iter] = newton_raphson(function1, 3/4, 0.0001)
pause(10)
%}
