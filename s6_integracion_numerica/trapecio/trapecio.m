pkg load symbolic


function resultado = trapecio(funcion, a, b)
    % Regla del trapecio para calcular la integral de una funcion
    % :param funcion: Funcion a integrar
    % :param a: Limite inferior
    % :param b: Limite superior
    % :return: Resultado obtenido
    f = matlabFunction(sym(funcion));  % Se crea una funcion
    resultado = ((b - a) / 2) * (f(a) + f(b));
end


%f1 = "ln(x)";
%resultado = trapecio(f1, 2, 5);
%disp(resultado);

%f1 = "13 / (5 * x + 4)";
%resultado = trapecio(f1, 1, 2);
%disp(resultado);
