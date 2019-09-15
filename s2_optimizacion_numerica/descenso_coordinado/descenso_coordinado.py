from sympy import sympify, Symbol, lambdify
from scipy import optimize
from numpy import linalg


def descenso_coordinado(str_funcion, variables, vector, tol, iter_max=200):
    """
    Funcion que implementa el metodo de descenso coordinado
    :param str_funcion: string con la funcion que se debe evaluar
    :param variables: lista con las variables de la ecuacion
    :param vector: vector inicial de necesita el metodo
    :param tol: tolerancia al fallo que debe tener el resultado
    :param iter_max: iteraciones maximas que no debe superar el metodo
    :return: lista con dos elementos, vector calculado y numero de iteraciones
    """
    funcion = sympify(str_funcion)  # Se obtiene la funcion a partir del string
    itr = 1  # Se inicializa el contador de iteraciones

    # Lista de variables debe tener mismo len que el vector
    if len(variables) != len(vector):
        return "La lista de variables y el vector deben tener la misma longitud"

    lista_simb = []
    n = len(variables)

    # Se crean los Symbol de las variables de la funcion
    for i in range(0, n):
        lista_simb += [Symbol(variables[i])]

    # Se crea el vector anterior inicial
    vector_ant = [0] * n

    while itr <= iter_max:
        # Se recorren cada una de las variables de la funcion
        for z in range(0, n):
            funcion_k = funcion

            # Se reemplazan las variables por sus valores numericos
            for a in range(0, n):
                if a != z:
                    funcion_k = funcion_k.subs(lista_simb[a], vector[a])

            # Se declara la funcion a minimizar (optimizar)
            func = lambdify(lista_simb[z], funcion_k)

            # Se obtiene el resutado de minimizar la funcion
            resultado = optimize.minimize_scalar(func)
            vector[z] = resultado.x

        # Se calcula el vector para la condicion de parada
        vec = [x1 - x2 for (x1, x2) in zip(vector, vector_ant)]

        # Se calcula la norma 2 del vector para la condicion de parada
        norma_2 = linalg.norm(vec, 2)

        # Se verifica la condicion de parada
        if norma_2 < tol:
            break

        itr += 1
        vector_ant = vector.copy()

    return [vector, itr]


# str_funcion1 = '(x - 2) ** 2 + (y + 3) ** 2 + x * y'
# variables1 = ['x', 'y']
# vector1 = [1, 1]
# print(descenso_coordinado(str_funcion1, variables1, vector1, 10**-5))


# str_funcion2 = 'x ** 3 + y ** 3 + z ** 3 - 2 * x * y - 2 * x * z - 2 * y * z'
# variables2 = ['x', 'y', 'z']
# vector2 = [1, 1, 1]
# print(descenso_coordinado(str_funcion2, variables2, vector2, 10**-5))
