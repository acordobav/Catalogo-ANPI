pkg load symbolic


function resultado = simpson(funcion, a, b)
    % Regla del Simpson para calcular la integral de una funcion
    % :param funcion: Funcion a integrar
    % :param a: Limite inferior
    % :param b: Limite superior
    % :return: Resultado obtenido
    f = matlabFunction(sym(funcion));  % Se crea una funcion
    h = (b - a) / 2;  % Se calcula el h
    resultado =  (h / 3) * (f(a) + 4 * f((a + b) / 2) + f(b));
end


%f1 = "ln(x)";
%resultado = simpson(f1, 2, 5);
%disp(resultado);

%f1 = "13 / (5 * x + 4)";
%resultado = simpson(f1, 1, 2);
%disp(resultado);
