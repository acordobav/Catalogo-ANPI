pkg load symbolic


function matriz = factorizacion_cholesky(matriz_a, matriz_b)
%   Metodo Factorizacion de Cholesky para resolver un sistema A x = B
%   :param matriz_a: matriz cuadrada de nxn
%   :param matriz_b: matriz columna de nx1
%   :return: matriz x que resuelve el sistema A x = b

    % Se verifica que la matriz A tenga simetria
    norm_a = norm(matriz_a, 1);
    norma_a_t = norm(matriz_a', 1);
    if norm_a - norma_a_t ~= 0
        error("La matriz debe ser simetrica");
    end  % if norm_a - norma_a_t ~= 0

    % Se calcula la factorizacion de Cholesky para la matriz_a
    matriz_l = chol(matriz_a)';

    % Se resuelve el sistema L y = b utilizando una sustitucion hacia adelante
    matriz_y = double(sustitucion_adelante(matriz_l, matriz_b));

    % Se resuelve el sistema Lt x = y utilizando una sustitucion hacia adelante
    matriz_x = double(sustitucion_atras(matriz_l', matriz_y));

    matriz = matriz_x;

end  % matriz = factorizacion_cholesky(matriz_a, matriz_b)


function matriz = sustitucion_adelante(matriz_a, matriz_b)
%   Funcion para realizar una sustitucion hacia adelante
%   :param matriz_a: matriz triangular inferior
%   :param matriz_b: matriz columna
%   :return: matriz con el resultado de realizar la sustitucion
    [n, m] = size(matriz_a);
    lista_simb = []

    % Se crea una lista con las variables simbolicas de la ecuacion
    for i = 1:n
        lista_simb = [lista_simb; sym(strcat('x', num2str(i)))];
    end  % for i = 1:n

    % Se resuelve el sistema A x = b utilizando una sustitucion hacia adelante
    for i = 1:n
        sub_lista = matriz_a(i,:);
        ecuacion = strcat('-', num2str(matriz_b(i)));

        % Se forma la ecuacion a resolver
        for x = 1:m
            ecuacion = strcat(ecuacion, ' + ', num2str(sub_lista(x)), ' * ', char(lista_simb(x)));
        end  % for i = 1:n

        % Se obtiene el resultado de la ecuacion
        resultado = solve(sym(ecuacion));
        lista_simb(i) = resultado;

    end  % for i = 1:n

    matriz = lista_simb;

end  % matriz = sustitucion_adelante(matriz_a, matriz_b)


function matriz = sustitucion_atras(matriz_a, matriz_b)
%   Funcion para realizar una sustitucion hacia adelante
%   :param matriz_a: matriz triangular superior
%   :param matriz_b: matriz columna
%   :return: matriz con el resultado de realizar la sustitucion
    [n, m] = size(matriz_a);
    lista_simb = [];
    % Se crea una lista con las variables simbolicas de la ecuacion
    for i = 1:n
        lista_simb = [lista_simb; sym(strcat('x', num2str(i)))];
    end  % for i = 1:n

    % Se realiza una sustitucion hacia atras
    for i = 1:n
        sub_lista = matriz_a(1+n-i,:);
        ecuacion = strcat('-', num2str(matriz_b(1+n-i)));

        % Se forma la ecuacion a resolver
        for x = 1:m
            ecuacion = strcat(ecuacion, ' + ', num2str(sub_lista(x)), ' * ', char(lista_simb(x)));
        end  % for i = 1:n

        % Se obtiene el resultado de la ecuacion
        resultado = solve(sym(ecuacion));
        lista_simb(1+n-i) = resultado;

    end  % for i = 1:n

    matriz = lista_simb;
end  % matriz = sustitucion_adelante(matriz_a, matriz_b)


% a = [25 15 -5 -10; 15 10 1 -7; -5 1 21 4; -10 -7 4 18];
% b = [-25; -19; -21; -5];
% disp(factorizacion_cholesky(a, b))
