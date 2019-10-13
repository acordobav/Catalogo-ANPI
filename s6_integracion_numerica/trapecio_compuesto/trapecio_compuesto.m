pkg load symbolic


function resultado = trapecio_compuesto(funcion, a, b, m)
    % Regla compuesta del trapecio para calcular la integral de una funcion
    % :param funcion: Funcion a integrar
    % :param a: Limite inferior
    % :param b: Limite superior
    % :param m: Cantidad de puntos a utilizar
    % :return: Resultado obtenido
    f = matlabFunction(sym(funcion));  % Se crea la funcion
    h = (b - a) / (m - 1);  % Se calcula el h
    x = a;
    sumatoria = 0;
    for i = 0: m - 1
        sumatoria = sumatoria +  (h / 2) * (f(x) + f(x + h));
        x = x + h;
    end
    resultado = sumatoria;
end

%f1 = "ln(x)";
%resultado = trapecio_compuesto(f1, 2, 5, 50);
%disp(resultado);

%f1 = "exp(-x ** 2)";
%resultado = trapecio_compuesto(f1, 0, 4, 6);
%disp(resultado);
