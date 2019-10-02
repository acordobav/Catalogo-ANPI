pkg load symbolic


function matriz_x = iteracion_gauss_seidel(matriz_a, matriz_b, tol)
    % Funcion que implementa el metodo iterativo de Jacobi para resolver el
    % sistema A x = b
    % :param matriz_a: Matriz cuadrada diagonalmente dominante
    % :param matriz_b: Vector columna
    % :param tol: Tolerancia al fallo que debe tener el vector resultado
    % :return: Vector resultado
    [n, m] = size(matriz_a);  % n: numero filas, m:numero columnas
    if n ~= m
        error("matriz_a debe ser cuadrada");
    end
    x = sym('x');  % Variable simbolica para aplicar el metodo
    vec_x = zeros(n, 1);  % Vector x que resuelve el sistema A x = b
    while 1
        vec_x_ant = vec_x;  % Vector de la iteracion anterior
        for i = 1:n
            ecuacion = matriz_b(i);
            for j = 1:m
                if i == j
                    % Elementos en la diagonal, se multiplica por la variable
                    ecuacion = ecuacion - matriz_a(i, j) * x;
                else
                    % Se multiplica por el valor respectivo en el vector
                    ecuacion = ecuacion - matriz_a(i, j) * vec_x(j);
                end  % if i == j
            end  % for j = 1:m
            % Se actualiza el vector en la posicion obtenida
            vec_x(i) = double(solve(ecuacion));
        end  % for i = 1:n
        % Condicion de parada
        norma_2 = norm(vec_x - vec_x_ant);
        if norma_2 < tol
            break;
        end  % if norma_2 < tol
    end  % while 1
    matriz_x = vec_x;
end  % iteracion_gauss_seidel(matriz_a, matriz_b, tol):

%A = [10 3 1; 2 -10 3; 0 -1 2];
%b = [-5; 14; 14];
%resultado = iteracion_gauss_seidel(A, b, 10 ^ -5);
%disp(resultado);

%A = [5 3 0; 3 -6 2; 0 2 -3];
%b = [[3], [-2], [-4]];
%resultado = iteracion_gauss_seidel(A, b, 10 ^ -5);
%disp(resultado);
