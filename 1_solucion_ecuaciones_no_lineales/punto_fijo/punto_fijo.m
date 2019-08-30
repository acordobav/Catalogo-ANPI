pkg load symbolic


% Funcion que implementa el metodo de punto fijo
% :param str_funcion: string con la funcion a evaluar
% :param xk: valor inicial del punto fijo
% :param a: extremo inferior del intervalo
% :param b: extremo superior del intervalo
% :param tol: tolerancia al fallo que debe tener el resultado
% :return: lista: [xk calculado, numero de iteraciones]
function [x_aprox, iter] = punto_fijo(str_funcion, xk, a, b, tol)
    funcion = matlabFunction(sym(str_funcion));  % Se obtiene la funcion
    itr = 0  % Contador de iteraciones

    % Se verifica la existencia del punto fijo
    existencia = verificar_existencia(str_funcion, a, b)
    if existencia ~= 0
        x_aprox = "No se cumple el criterio de existencia"
        iter = 0
    end  % if existencia ~= 0

    % Se verifica la unicidad del punto fijo
    unicidad = verificar_unicidad(str_funcion)
    if unicidad ~= 0
        x_aprox = "No se cumple el criterio de unicidad"
        iter = 0
    end  % if unicidad ~= 0

    xk_ant = xk

    while 1
        % Se actualiza el valor de xk
        xk = funcion(xk)
        itr = itr + 1

        % Se verifica la condicion de parada
        if abs(xk - xk_ant) < tol
            break
        end  % if abs(xk - xk_ant) < tol

        xk_ant = xk

    end  % while 1

    x_aprox = xk
    iter = itr

end  % [x_aprox, iter] = punto_fijo(str_funcion, xk, a, b, tol)


% Funcion para verificar la existencia de un punto fijo dentro de [a, b]
% :param funcion: string con la funcion
% :param a: extremo inferior del intervalo
% :param b: extremo superior del intervalo
% :return: 0 si existe, un 1 en caso de que no exista
function [resultado] = verificar_existencia(funcion, a, b)
    % Se crea la funcion simbolica
    f = matlabFunction(sym(funcion))

    % Se obtienen los puntos criticos de la funcion
    puntos_criticos = solve(diff(sym(funcion)))

    % Puntos criticos deben estar  dentro del intervalo [a, b]
    n = length(puntos_criticos)
    if n == 1
        valor = f(puntos_criticos)
        % Se verifica que el valor este dentro de [a, b]
        if ~(a < valor && valor < b)
            resultado = 1
        end  % if ~(a < valor && valor < b)

    else
        for i = 1:n
            valor = f(puntos_criticos(i))
            if ~(a < valor && valor < b)
                resultado = 1
            end  % if ~(a < valor && valor < b)
        end  % for i = 1:n
    end  % if n == 1

    % Se evalua la funcion en los extremos
    f_a = f(a)
    f_b = f(b)

    % Funcion en los extremos debe estar dentro de [a. b]
    if ~(a < f_a && f_a < b) || ~(a < f_b && f_b < b)
        resultado = 1
    end

    resultado = 0

end  % [x_aprox, iter] = punto_fijo(str_funcion, xk, a, b, tol)


% Funcion para verificar la unicidad del punto fijo
% :param funcion: string con la funcion
% :return: 0 si el punto es unico, un 1 en caso contrario
function [resultado] = verificar_unicidad(funcion)
    % Se obtienen los puntos criticos de la funcion
    puntos_criticos = solve(diff(sym(funcion)))

    % Puntos criticos deben estar  dentro del intervalo [a, b]
    n = length(puntos_criticos)
    if n == 1
        % Se verifica que el valor este dentro de [a, b]
        if ~(-1 < puntos_criticos && puntos_criticos < 1)
            resultado = 1
        end  % if ~(a < valor && valor < b)

    else
        for i = 1:n
            valor = puntos_criticos(i)
            if ~(-1 < valor && valor < 1)
                resultado = 1
            end  % if ~(a < valor && valor < b)
        end  % for i = 1:n
    end  % if n == 1

    resultado = 0

end  % [resultado] = verificar_unicidad(funcion)


% punto_fijo('(x ** 2 - 1) / 3', 0, -1, 1, 10 ^ -5)

% punto_fijo('1 / (1 + x ** 2)', 0, -3, 3, 10 ^ -5)

% punto_fijo('log(2 * x + 1)', 0, 1, 2, 10 ^ -5)