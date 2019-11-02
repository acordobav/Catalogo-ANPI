pkg load symbolic


function resultado = adams_bashforth_p2(str_funcion, a, b, n, x0, y0, y1)
    % Metodo de Adams-Bashforth de paso dos para aproximar la solucion de un problema de valor inicial
    % :param str_funcion: string con la funcion que se debe evaluar
    % :param a: Extremo inferior del intervalo
    % :param b: Extremo superior del intervalo
    % :param n: Cantidad de puntos
    % :param x0: Valor inicial de x
    % :param y0: Valor de y para el x inicial
    % :param y1: Valor de y1 para el x1
    % :return: Valor de la ecuacion en b
    funcion = matlabFunction(sym(str_funcion));
    h = (b - a) / (n - 1);
    x = x0 + h;  % Variable para el x de la iteracion actual
    y = y1;  % Variable para el y de la iteracion actual
    x_ant = x0;  % Variable para el x de la iteracion anterior
    y_ant = y0;  % Variable para el y de la iteracion anterior

    while x <= b - h
        y_temp = y;  % Variable temporal para guardar el valor de y
        y = y + h * (3 * funcion(x, y) - funcion(x_ant, y_ant)) / 2;

        % Se actualizan las varaibles
        y_ant = y_temp;
        x_ant = x;
        x = x + h;
    end

    resultado = y;
end


function resultado = adams_bashforth_p3(str_funcion, a, b, n, y0, y1, y2)
    % Metodo de Adams-Bashforth de paso tres para aproximar la solucion de un problema de valor inicial
    % :param str_funcion: string con la funcion que se debe evaluar
    % :param a: Extremo inferior del intervalo
    % :param b: Extremo superior del intervalo
    % :param n: Cantidad de puntos
    % :param y0: Valor de y para el x inicial
    % :param y1: Valor de y1 para el x1
    % :param y2: Valor de y2 para el x2
    % :return: Valor de la ecuacion en b
    %  Se contruye la funcion a evaluar
    funcion = matlabFunction(sym(str_funcion));
    h = (b - a) / (n - 1);
    x = a + 2 * h;  % Variable para el x de la iteracion actual
    y = y2;  % Variable para el y de la iteracion actual
    x_ant = a + h;  % Variable para el x de la iteracion anterior
    y_ant = y1;  % Variable para el y de la iteracion anterior
    y_ant_1 = y0;  % Variable para el "y" de dos iteraciones anterior
    x_ant_1 = a;  % Variable para el "x" de dos iteraciones anterior

    while x <= b - h
        y_temp = y;  % Variable temporal para guardar el valor de y
        y = y + h * (23 * funcion(x, y) - 16 * funcion(x_ant, y_ant) + 5 * funcion(x_ant_1, y_ant_1)) / 12;

        % Se actualizan las varaibles
        x_ant_1 = x_ant;
        y_ant_1 = y_ant;
        y_ant = y_temp;
        x_ant = x;
        x = x + h;

    end
    resultado =  y;
end


function resultado = adams_bashforth_p4(str_funcion, a, b, n, y0, y1, y2, y3)
    % Metodo de Adams-Bashforth de paso cuatro para aproximar la solucion de un problema de valor inicial
    % :param str_funcion: string con la funcion que se debe evaluar
    % :param a: Extremo inferior del intervalo
    % :param b: Extremo superior del intervalo
    % :param n: Cantidad de puntos
    % :param y0: Valor de y para el x inicial
    % :param y1: Valor de y1 para el x1
    % :param y2: Valor de y2 para el x2
    % :param y2: Valor de y3 para el x3
    % :return: Valor de la ecuacion en b
    % Se contruye la funcion a evaluar
    funcion = matlabFunction(sym(str_funcion));
    h = (b - a) / (n - 1);
    x = a + 3 * h;  % Variable para el x de la iteracion actual
    y = y3;  % Variable para el y de la iteracion actual
    x_ant = a + 2 * h;  % Variable para el x de la iteracion anterior
    y_ant = y2;  % Variable para el y de la iteracion anterior
    y_ant_2 = y1;  % Variable para el "y" de dos iteraciones anterior
    x_ant_2 = a + h;  % Variable para el "x" de dos iteraciones anterior
    y_ant_3 = y0;  % Variable para el "y" de tres iteraciones anterior
    x_ant_3 = a;  % Variable para el "x" de tres iteraciones anterior

    while x <= b - h
        y_temp = y;  % Variable temporal para guardar el valor de y
        y = y + h * (55 * funcion(x, y) - 59 * funcion(x_ant, y_ant) + 37 * funcion(x_ant_2, y_ant_2) - 9 * funcion(x_ant_3, y_ant_3)) / 24;

        % Se actualizan las varaibles
        x_ant_3 = x_ant_2;
        y_ant_3 = y_ant_2;
        x_ant_2 = x_ant;
        y_ant_2 = y_ant;
        y_ant = y_temp;
        x_ant = x;
        x = x + h;
    end

    resultado =  y;
end


%resultado = adams_bashforth_p2('1 + (x - y) ** 2', 2, 4, 11, 2, 1, 1.191);
%disp(resultado);
%
%resultado = adams_bashforth_p3('1 + (x - y) ** 2', 2, 4, 11, 1, 1.191, 1.365);
%disp(resultado);
%
%resultado = adams_bashforth_p4('1 + (x - y) ** 2', 2, 4, 11, 1, 1.191, 1.365, 1.528);
%disp(resultado);