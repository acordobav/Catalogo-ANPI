pkg load symbolic

function [vec_aprox, iter] = gradiente_conjugado(str_funcion, variables, vector, tol, regla_bk)
%    Funcion que implementa el metodo de gradiente conjugado
%    :param str_funcion: string con la funcion que se debe evaluar
%    :param variables: lista con las variables de la ecuacion
%    :param vector: vector inicial que necesita el metodo
%    :param tol: tolerancia al fallo que debe tener el resultado
%    :param regla_bk: metodo seleccionado para el calcular el Bk
%    :return: lista con dos elementos, vector calculado y numero de iteraciones
    if nargin == 4
        regla_bk = 'FR';
    end  % if nargin == 4

    if tol < 0
        error('tol debe ser un numero positivo');
    end  % if tol < 0

    if regla_bk ~= 'FR' && regla_bk ~= 'CD' && regla_bk ~= 'DY'
        error('Parametro regla_bk debe ser "FR", "CD" o "DY"');
    end  % if regla_bk ~= 'FR'

    funcion = sym(str_funcion);  % Se obtiene la funcion

    itr = 0;                 % Contador de iteraciones
    n = length(variables);   % Cantidad de variables

    % Se calcula el gradiente
    gradiente = [];
    for i = 1:n
        gradiente = [gradiente, diff(sym(str_funcion), sym(variables(i)))];
    end  % for i = 1:n

    % Se calculan los valores iniciales de gk y dk
    gk = evaluar_gradiente(gradiente, variables, vector);
    dk = -gk;

    while 1
        % Se calcula el alpha
        ak = calcular_ak(funcion, variables, vector, dk, gk);

        % Se calcula el nuevo vector: vec1 = vec0 + a * d0
        vec_1 = vector + (ak * dk);

        % Se calcula el nuevo valor del gk
        gk_1 = evaluar_gradiente(gradiente, variables, vec_1);

        % Se calcula el vector para la condicion de parada
        vec_parada = evaluar_gradiente(gradiente, variables, vec_1);

        % Se verifica la condicion de vec_parada
        if norm(vec_parada) < tol
            vector = vec_1;
            break;
        end  % norm(vec_parada) < tol

        % Se calcula el valor de beta
        bk = double(calcular_bk(gk_1, gk, dk, regla_bk));

        % Se calcula el nuevo valor de dk
        dk = -gk_1 + (bk * dk);

        vector = vec_1;
        gk = gk_1;
        itr = itr + 1;

    end  % while 1

    vec_aprox = vector
    iter = itr

end  % gradiente_conjugado(str_funcion, variables, vector, tol, regla_bl)

function result = evaluar_gradiente(gradiente, variables, vector)
%    Funcion para evaluar el gradradiente con un vector ingresado
%    :param gradiente: gradiente que se debe evaluar
%    :param variables: lista con las variables simbolicas de la ecuacion
%    :param vector: vector que se debe evaluar en el gradiente
%    :return: resultado de evaluar el vector en el gradiente

    n = length(variables);
    resultado = [];
    % Se recorren cada una de las derivadas parciales en el gradiente
    for i = 1:n
        % Se obtiene la derivada parcial
        funcion = gradiente(i);

        % Se sustituyen las variables por los valores en el vector
        for x = 1:n
            funcion = subs(funcion, variables(x), vector(x));
        end  %x = 1:n

        resultado = [resultado double(funcion)];

    end  %for i = 1:n
    result = resultado;

end  % evaluar_gradiente(gradiente, variables, vector)


function result = evaluar_funcion(funcion, variables, vector)
%    Funcion para evaluar un vector en una funcion
%    :param funcion: funcion a evaluar
%    :param variables: lista con las variables simbolicas de la ecuacion
%    :param vector: vector a evaluar en la funcion
%    :return: resultado de evaluar el vector en la funcion

    n = length(variables);
    % Se sustituyen cada una de las variables por el valor en el vector
    for x = 1:n
        funcion = subs(funcion, variables(x), vector(x));
    end  % for x = 1:n

    result = double(funcion);

end  % evaluar_funcion(funcion, variables, vector)



function ak = calcular_ak(funcion, variables, vector, d_k, g_k)
%    Se calcula el ak, encontrando el primer valor que cumpla con la desigualdad
%    f(vector + ak * dk) - f(vector) <= 0.5 * ak * gk * dk
%    :param funcion: funcion que se debe evaluar
%    :param variables: lista con las variables de la ecuacion
%    :param vector: vector de la solucion aproximada
%    :param d_k: vector d de la iteracion k
%    :param g_k: vector g de la iteracion k
%    :return: valor de a que cumple con la desigualdad
    a = 1;
    while 1
        % Se calcula el lado izquierdo de la desigualdad
        arg1 = vector + (a * d_k);
        f_vec_a_dk = evaluar_funcion(funcion, variables, arg1);
        f_vec = evaluar_funcion(funcion, variables, vector);
        parte1 = double(f_vec_a_dk - f_vec);

        % Se calcula el lado derecho de la desigualdad
        gk_dk = double(sum(g_k .* d_k));
        parte2 = double(0.5 * a * gk_dk);

        if parte1 <= parte2
            break;
        end  % if parte1 <= parte2

        a = a / 2;

    end  % while 1

    ak = double(a);

end  % calcular_ak(funcion, variables, vector, d_k, g_k)


function b = calcular_bk(gk, gk_ant, dk, regla_bk)
%    Funcion para calcular la regla_bk
%    :param gk: vector gk
%    :param gk_ant: vector gk de la iteracion anterior
%    :param dk: vector dk
%    :param regla_bk: regla deseada para calcular bk
%    :return: valor de bk calculado
    % Se calcula la norma 2 del vector gk
    gk_norma2 = double(norm(gk));

    % Metodo de Fletcher and Reeves
    if regla_bk == 'FR'
        % Se calcula la norma 2 del gk anterior
        gk_ant_norma2 = double(norm(gk_ant));

        b = gk_norma2 ^ 2 / gk_ant_norma2 ^ 2;

    end  % regla_bk == 'FR'
    % Metodo de Descenso Conjugado CD
    if regla_bk == 'CD'
        b = gk_norma2 ^ 2 / sum((-dk) .* gk);

    end  % regla_bk == 'CD'
    % Metodo de Dai and Yuan

    if regla_bk == 'DY'
        yk = gk - gk_ant;
        b = gk_norma2 ^ 2 / sum(dk .* yk);

    end  % regla_bk == 'DY'

end  % calcular_bk(gk, gk_ant, dk, regla_bk)


%str_f = '(x-2)^4 + (x-2*y)^2'
%var = ['x', 'y']
%disp(gradiente_conjugado(str_f, var, [0 3], 10 ^ -3, 'FR'))