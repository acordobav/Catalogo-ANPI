pkg load symbolic


function resultado = predictor_corrector(str_funcion, a, b, n, x, y)
    % Metodo Predictor-Corrector para aproximar la solucion de un problema de valor inicial
    % :param str_funcion: string con la funcion que se debe evaluar
    % :param a: Extremo inferior del intervalo
    % :param b: Extremo superior del intervalo
    % :param n: Cantidad de puntos
    % :param x: Valor inicial de x
    % :param y: Valor de y para el x inicial
    % :return: Valor de la ecuacion diferencial en xn
    funcion = matlabFunction(sym(str_funcion));
    h = (b - a) / (n - 1);

    while x <= b - h
        % Calculo del valor predictor utilizando Euler
        predictor = y + h * funcion(x, y);

        % Calculo del valor corrector
        y = y + h * (funcion(x, y) + funcion(x + h, predictor)) / 2;

        x = x + h;
    end

    resultado = y;
end


%resultado = predictor_corrector('y - x ** 2 + 1', 0, 2, 11, 0, 0.5);
%disp(resultado);
