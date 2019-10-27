pkg load symbolic


function resultado = euler(str_funcion, a, b, n, x, y)
    % Metodo de Euler para aproximar la solucion de un problema de valor inicial
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
        y = y + h * funcion(x, y);
        x = x + h;
    end

    resultado = y;
end

%resultado = euler('y - x ^ 2 + 1', 0, 2, 11, 0, 0.5);
%disp(resultado);
