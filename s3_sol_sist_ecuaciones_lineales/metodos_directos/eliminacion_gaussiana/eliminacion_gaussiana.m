pkg load symbolic

function matriz_x = eliminacion_gaussiana(matriz_a, matriz_b)
%   Funcion para realizar una sustitucion hacia adelante
%   :param matriz_a: matriz triangular inferior
%   :param matriz_b: matriz columna
%   :return: matriz con el resultado de realizar la sustitucion
    [n, m] = size(matriz_a);
    lista_simb = [];

    if n ~= m
        error("matriz_a debe ser cuadrada")
    end  % if n ~= m

    % Se construye la matriz aumentada del sistema
    m_aumentada = [];
    for i = 1:n
        m_aumentada =[m_aumentada; [matriz_a(i,:),  matriz_b(i)]];
        lista_simb = [lista_simb sym(strcat('x', num2str(i)))];
    end  % for i = 1:n

    % Se obtiene la matriz triangular superior del sistema
    [L, U] = lu(m_aumentada);

    % Se realiza una sustitucion hacia atras
    for i = 1:n
        sub_lista = U(1+n-i,:);
        ecuacion = strcat('-', num2str(sub_lista(m+1)));

        % Se forma la ecuacion a resolver
        for x = 1:m
            ecuacion = strcat(ecuacion, ' + ', num2str(sub_lista(x)), ' * ', char(lista_simb(x)));
        end  % for i = 1:n

        % Se obtiene el resultado de la ecuacion
        resultado = solve(sym(ecuacion));
        lista_simb(1+n-i) = resultado;

    end  % for i = 1:n

    matriz_x = lista_simb;
end  % matriz_x = eliminacion_gaussiana(matriz_a, matriz_b)

% a = [2, -6, 12, 16; 1, -2, 6, 6; -1, 3, -3, -7; 0, 4, 3, 6];
% b = [70; 26; -30; -26];
%eliminacion_gaussiana(a, b)