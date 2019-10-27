pkg load symbolic


function resultado = simpson_compuesto(str_funcion, a, b, m)
    % Regla compuesta de Simpson para calcular la integral de una funcion
    % :param str_funcion: String con la funcion a integrar, debe ser en funcion de x
    % :param a: Limite inferior
    % :param b: Limite superior
    % :param m: Cantidad de puntos a utilizar
    % :return: Resultado obtenido
    funcion = matlabFunction(sym(str_funcion));  % Se crea la funcion
    h = (b - a) / (m - 1);  % Se calcula el h
    x = a;
    soporte = [];

    % Construccion del conjunto soporte
    while x <= b
        soporte = [soporte x];
        x = x + h;
    end

    par = 0;  % Variable que contiene la sumatoria de todas las posiciones par
    impar = 0;  % Variable que contiene la sumatoria de todas las posiciones impar

    n = length(soporte);
    for i = 2: n - 1
        % Se verifica si el indice de la lista es par o impar
        if ~mod(i,2) == 0
            par = par + funcion(soporte(i));
        else
            impar = impar + funcion(soporte(i));
        end
    end

    resultado = (funcion(soporte(1)) + 2 * par + 4 * impar + funcion(soporte(n))) * h / 3;
end


%resultado = simpson_compuesto('log(x)', 2, 5, 7);
%disp(resultado);

%resultado = simpson_compuesto("exp(-x ** 2)", 0, 4, 6);
%disp(resultado);
