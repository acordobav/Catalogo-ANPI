pkg load symbolic

function [xAprox, iter] = newton_raphson(f, x0, tol)
    [xAprox, iter] = newton_raphsonAux(f, x0, tol, 0, [], []);
end % End newton_raphson


function [xAprox, iter] = newton_raphsonAux(strFuncion, xkAnterior, tol, itr, listaError, listaIter)
    f = matlabFunction(sym(strFuncion));

    fxk = f(xkAnterior);
    if abs(f(xkAnterior)) <= tol
        xAprox = xkAnterior;
        iter = itr;


    else
        df = matlabFunction(diff(sym(strFuncion)));
        xkSiguiente = xkAnterior - (f(xkAnterior)/df(xkAnterior));

        [xAprox, iter] = newton_raphsonAux(f, xkSiguiente, tol, itr + 1, listaIter, listaError);

    end % End if abs(fxk) <= tol;

end % End newton_raphsonAux

%{
f = 'cos(2*x)^2 - x^2'
[xAprox, iter] = newton_raphson(f, 3/4, 0.0001)
%}
