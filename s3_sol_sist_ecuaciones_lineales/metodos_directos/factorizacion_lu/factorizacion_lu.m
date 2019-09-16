pkg load symbolic


function matriz = factoricacion_lu(matriz_a, matriz_b)
%   Metodo de Factorizacion LU para resolver un sistema A x = B
%   :param matriz_a: matriz cuadrada de nxn
%   :param matriz_b: matriz columna de nx1
%   :return: matriz x que resuelve el sistema A x = b
    [n, m] = size(matriz_a);

    if n ~= m
        error("matriz_a debe ser cuadrada")
    end  % if n ~= m

    % Se obtiene las matrices L y U del sistema
    [matriz_l, matriz_u, P] = lu(matriz_a);

    % Se resuelve el sistema L y = b utilizando una sustitucion hacia adelante
    matriz_y = sustitucion_adelante(matriz_l, matriz_b);

    % Se resuelve el sistema U x = y utilizando una sustitucion hacia atras
    matrix_x = double(sustitucion_atras(matriz_u, double(matriz_y)));

    matriz = matrix_x



end  % matriz_r = factoricacion_lu(matriz_a, matriz_b)


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


% a = [4, -2, 1; 20, -7, 12; -8, 13, 17];
% b = [11;70; 17];
% factoricacion_lu(a, b);
