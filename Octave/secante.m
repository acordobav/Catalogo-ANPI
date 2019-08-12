pkg load symbolic

%{
Funcion que implementa el metodo de la secante para encontrar el cero de una funcion
:param f: string con la funcion que se debe evaluar
:param xKAnterior2: valor de xk de la iteracion inicial
:param xkAnterior1: valor de xk de la segunda iteracion
:param tol: tolerancia al fallo que debe cumplir el resultado
%}
function [xAprox, iter] = secante(f, xkAnterior2, xkAnterior1, tol)
    funcion = matlabFunction(sym(f)); %Se obtiene la funcion ingresada por el usuario
    itr = 0 %Se inicializa el contador de iteraciones

    %Bucle infinito que se rompe al encontrar la condicion de parada
    while 1
        %Se calcula el xk de la iteracion actual
        xk = xkAnterior1 - ((funcion(xkAnterior1)*(xkAnterior1-xkAnterior2))/(funcion(xkAnterior1)-funcion(xkAnterior2)));

        %Se evalua la funcion en el valor de xk
        fxk = funcion(xk);

        %Se verifica la condicion de parada
        if(abs(fxk) <= tol)
            break; %Se rompe el bucle infinito

        end % End if(abs(fxk) <= 0)

        %Se ajustan las variables para la siguiente iteracion
        xkAnterior2 = xkAnterior1;
        xkAnterior1 = xk;
        itr = itr + 1;

    end % End While

    xAprox = xk;
    iter = itr;

end %secante(f, xkAnterior2, xkAnterior1, tol)

%[xAprox, iter] = secante('exp(2*x) - 10 - log(x/2)', 1, 1.2, 10^-2)