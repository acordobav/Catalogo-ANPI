pkg load symbolic


% Funcion que implementa el metodo de descenso coordinado
% :param str_funcion: string con la funcion que se debe evaluar
% :param variables: lista con las variables de la ecuacion
% :param vector: vector inicial de necesita el metodo
% :param tol: tolerancia al fallo que debe tener el resultado
% :param iter_max: iteraciones maximas que no debe superar el metodo
% :return: lista con dos elementos, vector calculado y numero de iteraciones

function [v_aprox, iter] = descenso_coordinado(str_funcion, variables, vector, tol, iter_max)
    if nargin == 4
        iter_max = 200
    end  % if nargin == 4

    itr = 0                 % Contador de iteraciones
    vector_ant = []         % Vector de la iteracion anterior
    lista_simb = []         % Lista con las variables simbolicas
    n = length(variables)   % Cantidad de variables

    % Se crea el vector anterior inicial (cada elemento en cero)
    % Se crean las variables simbolicas
    for i = 1:n
        vector_ant = [vector_ant, 0]
        lista_simb = [lista_simb, sym(variables(i))]
    end  % for i = 1:n

    while itr < iter_max
        % Se recorren cada una de las variables de la funcion
        for z = 1:n
            % Se hace una copia de la funcion original
            funcion_k = str_funcion

            % Se reemplazan las variables por sus valores numericos
            for a = 1:n
                if a ~= z
                    funcion_k = subs(funcion_k, lista_simb(a), vector(a))

                end  % if a ~= z
            end  % for a = 1:n

            % Se calcula el minimo de la funcion obtenida
            funcion = matlabFunction(funcion_k)

            % Se busca el minimo de la funcion obtenida
            min = fminsearch(funcion, 0)

            vector(z) = min

        end  % for z = 1:n

        % Se calcula el vector para la condicion de parada
        vec = vector - vector_ant

        % Se calcula la norma 2 del vector para la condicion de parada
        norma_2 = norm(vec)

        % Se verifica la condicion de parada
        if norma_2 < tol
            break
        end  % if norma_2 < tol

        itr = itr + 1
        vector_ant = vector

    end  % while 1

    v_aprox = vector
    iter = itr
end  % descenso_coordinado(str_funcion, variables, vector, tol)


% str_f1 = '(x - 2) ^ 2 + (y + 3) ^ 2 + x * y'
% descenso_coordinado(str_f1, ['x', 'y'], [1, 1], 10 ^ -5)

% str_f2 = 'x ** 3 + y ** 3 + z ** 3 - 2 * x * y - 2 * x * z - 2 * y * z'
% descenso_coordinado(str_f2, ['x', 'y', 'z'], [1, 1, 1], 10 ^ -5)