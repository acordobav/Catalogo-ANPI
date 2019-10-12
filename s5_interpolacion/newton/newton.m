pkg load symbolic


function resultado = newton(lista_puntos)
    % Diferencias Divididas de Newton para resolver un problema de interpolacion
    % :param lista_puntos: Los puntos deben ser ingresados en una lista, donde cada punto
    % es una lista, donde la primera posicion es el x, y la segunda posicion es el y. [x, y]
    % :return: Polinomio de interpolacion obtenido
    [n, m] = size(lista_puntos);  % Cantidad de puntos
    if m ~= 2
        error('Error en la lista de puntos');
    end  % if m ~=
    x = sym('x');   % Variable simbolica
    polinomio = lista_puntos(1, 2);  % Polinomio de interpolacion
    resul_previos = [];  % Lista para los resultados previos
    m = n - 1;
    multi = 1;  % Variable que almacena la multiplicacion (x-x0) * ... * (x-xn)

    for i = 1:n
        % Se agregan los "y" en la lista de resultados previos
        resul_previos = [resul_previos lista_puntos(i, 2)];
    end

    for i = 2:n
        multi = multi * (x - lista_puntos(i - 1, 1));  % Se multiplica por (x - xi)
        resul_nuevos = [];  % Lista para los resultados nuevos
        for j = 1:m
            % Se realiza el calculo de cada elemento del polinomio
            numerador = resul_previos(j) - resul_previos(j + 1);
            denominador = lista_puntos(j, 1) - lista_puntos(j + i - 1, 1);
            resul_nuevos = [resul_nuevos (numerador / denominador)];
        end
        m = m - 1;
        % Se actualiza el polinomio
        polinomio = polinomio + resul_nuevos(1) * multi;
        % Se actualiza la lista de resultados previos
        resul_previos = resul_nuevos;
    end
    resultado = expand(polinomio);
end


%lista_p = [-2 0; 0 1; 1 -1];
%resultado = newton(lista_p);
%disp(resultado);

%lista_p = [1 2/3; 3 1; 5 -1; 6 0];
%resultado = newton(lista_p);
%disp(resultado);
