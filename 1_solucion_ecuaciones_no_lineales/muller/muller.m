pkg load symbolic


function [x_aprox, iter] = muller(str_funcion, x0, x1, x2, tol)
    funcion = matlabFunction(sym(str_funcion));  % Se obtiene la funcion
    itr = 1  % Se inicializa el contador de iteraciones

    while 1
        % Se evalua la funcion en cada uno de los puntos ingresados
        f_x0 = funcion(x0)
        f_x1 = funcion(x1)
        f_x2 = funcion(x2)

        % Se obtiene la solucion del sistema de ecuaciones
        syms a b c
        [sol_a, sol_b, sol_c]= solve(a * x0 ^ 2 + b * x0 + c == f_x0,
                                    a * x1 ^ 2 + b * x1 + c == f_x1,
                                    a * x2 ^ 2 + b * x2 + c == f_x2)

        % Se calcula el discriminante de la funcion cuadratica
        discr = sol_b ^ 2  - 4 * sol_a * sol_c

        % Se calculan los ceros de la funcion
        cero1 = double((-sol_b + discr ^ (1 / 2)) / (2 * sol_a))
        cero2 = double((-sol_b - discr ^ (1 / 2)) / (2 * sol_a))

        % Se calcula el promedio de los ceros a cada punto
        prom_cero1 = (abs(cero1 - x0) + abs(cero1 - x1) + abs(cero1 - x2)) / 3
        prom_cero2 = (abs(cero2 - x0) + abs(cero2 - x1) + abs(cero2 - x2)) / 3

        % Se selecciona el que tenga menor promedio
        xk_aprox = cero1
        if prom_cero2 < prom_cero1
            xk_aprox = cero2
        end  % prom_cero2 < prom_cero1

        % Se determinan las distancias de los puntos al cero
        dist_x0 = abs(xk_aprox - x0)
        dist_x1 = abs(xk_aprox - x1)
        dist_x2 = abs(xk_aprox - x2)

        % Se crea un disccionario llave:valor donde la llave es la distancia de los
        % valores iniciales al cero, y el valor es el x0, x1 o x2
        keySet = [dist_x0, dist_x1, dist_x2]
        valueSet = [x0, x1, x2]
        map = containers.Map(keySet, valueSet)

        % Se ordenan las distancias para obtener las minimas
        keyOrdenado = sort(keySet)

        % Se verifica la condicion de parada
        f_xaprox = funcion(xk_aprox)
        if abs(f_xaprox) < tol
            break
        end % abs(f_xaprox) < tol

        x0 = xk_aprox
        x1 = map(keyOrdenado(1))
        x2 = map(keyOrdenado(2))
        itr = itr + 1

    end  % while 1

    x_aprox = xk_aprox
    iter = itr

end  % [x_aprox, iter] = muller(str_funcion, x0, x1, x2, tol)

% muller('sin(x) - x / 2', 2, 2.2, 1.8, 10 ^ -5)

% muller('(1 + x) * sin(x) - 1', 2.9, 3, 2.8, 10 ** -5)