pkg load symbolic


function resultado = lagrange(lista_puntos)
    % Metodo de interpolacion de Lagrange
    % :param lista_puntos: Los puntos deben ser ingresados en una lista, donde cada punto
    % es una lista, donde la primera posicion es el x, y la segunda posicion es el y. [x, y]
    % :return: Polinomio de interpolacion obtenido
    [n, m] = size(lista_puntos);  % Cantidad de puntos
    if m ~= 2
        error('Error en la lista de puntos');
    end  % if m ~=
    x = sym('x');   % Variable simbolica
    polinomio = 0;  % Polinomio de interpolacion

    % Se recorre cada punto en la lista ingresada
    for i = 1:n
        punto = lista_puntos(i,:);
        lk = 1;
        % Calculo de Lk(x)
        for j = 1:n
            if i ~= j
                % Se obtiene el xj
                xj = lista_puntos(j, 1);
                % Se calcula el producto actual
                lk = lk * (x - xj) / (punto(1) - xj);
            end
        end
        % Calculo de Pn(x)
        polinomio = polinomio + punto(2) * lk;
    end
    resultado = expand(polinomio);
end


%lista_p = [-2 0; 0 1; 1 -1];
%resultado = lagrange(lista_p);
%disp(resultado);

%lista_p = [1 2/3; 3 1; 5 -1; 6 0];
%resultado = lagrange(lista_p);
%disp(resultado);
