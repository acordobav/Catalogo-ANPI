function resultado = solv_sist_pinv(matriz_a, matriz_b, tol)
    % Solucion de sistemas de ecuaciones con el uso de pseudoinversa
    % :param matriz_a: Matriz A
    % :param matriz_b: Matriz b
    % :param tol: Tolerancia que debe cumplir el resultado
    % :return: Solucion del sistema A x = b
    if tol < 0
        error("La tolerancia debe ser mayor a cero");
    end
    % Calculo de la pseudo inversa de la matriz_a
    a_t = pseudoinversa_sbi(matriz_a, tol);

    % Calculo de la solucion del sistema
    x = a_t * matriz_b;

    resultado = x;

end  % solv_sist_pinv(matriz_a, matriz_b, tol)





function resultado = pseudoinversa_sbi(matriz_a, tol)
    % Metodo iterativo para encontrar la pseudoinversa de una matriz
    % :param matriz_a: Matriz a la que calcularle la pseudoinversa
    % :param tol: Tolerancia al fallo que debe cumplir el resultado
    % :return: Matriz pseudoinversa aproximada
    [n, m] = size(matriz_a);  % dimensiones de la matriz
    m_identidad = eye(n, n);  % matriz identidad de n x n
    xk = (1 / (norm(matriz_a) ^ 2)) * matriz_a';  % xk inicial

    while 1
        % Calculo del nuevo valor de xk
        xk = xk * (2 * m_identidad - matriz_a * xk);

        % Condicion de parada
        norma_2 = norm(matriz_a * xk * matriz_a - matriz_a);
        if norma_2 < tol
            break;
        end  % if norma_2 < tol
    end  % while 1

    resultado = xk;
end  % pseudoinversa_sbi(matriz_a, tol)

%resultado = pseudoinversa_sbi([1 3 9; 8 9 7], 10 ^ -5);
%disp(resultado);

%A = [1 3 9; 8 9 7];
%b = [8; 24];
%resultado = solv_sist_pinv(A, b, 10 ^ -5);
%disp(resultado);

