function resultado =  metodo_qr(A, tol)
    % Metodo QR para encontrar todos los autovalores de una matriz
    % :param A: Matriz A
    % :param tol: Tolerancia al fallo que debe tener el resultado
    % :return: Matriz con todos los autovalores de la matriz A
    size_A = size(A);
    A_ant = zeros(size_A);

    while 1
        [Q, R] = qr(A);
        A_ant = A;
        A = R * Q;

        % Se verifica la condicion de parada
        norma = norm(A_ant - A);
        if norma < tol
            break;
        end
    end
    resultado = A;
end

%resultado = metodo_qr([12 -51 4; 6 167 -68; -4 24 -41], 10 ^ -6);
%disp(resultado);
