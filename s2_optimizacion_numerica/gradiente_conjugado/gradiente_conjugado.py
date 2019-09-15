from sympy import sympify, Symbol, diff
from numpy import linalg, array


def gradiente_conjugado(str_funcion, variables, vector, tol, regla_bk='FR'):
    """
    Funcion que implementa el metodo de gradiente conjugado
    :param str_funcion: string con la funcion que se debe evaluar
    :param variables: lista con las variables de la ecuacion
    :param vector: vector inicial que necesita el metodo
    :param tol: tolerancia al fallo que debe tener el resultado
    :param regla_bk: metodo seleccionado para el calcular el Bk
    :return: lista con dos elementos, vector calculado y numero de iteraciones
    """
    funcion = sympify(str_funcion)  # Se obtiene la funcion a partir del string
    itr = 1  # Se inicializa el contador de iteraciones

    # Lista de variables debe tener mismo len que el vector
    if len(variables) != len(vector):
        return "La lista de variables y el vector deben tener la misma longitud"

    # Se verifica el metodo seleccionado para calcular el Bk
    if regla_bk != 'FR' and regla_bk != 'CD' and regla_bk != 'DY':
        return 'Parametro regla_bk debe ser "FR", "CD" o "DY"'

    lista_simb = []
    n = len(variables)

    # Se crean los Symbol de las variables de la funcion
    for i in range(0, n):
        lista_simb += [Symbol(variables[i])]

    # Se calcula el gradiente de la funcion
    gradiente = []
    for i in range(0, n):
        gradiente += [diff(funcion, variables[i])]

    # Se calculan los valores iniciales de gk y dk
    gk = evaluar_gradiente(gradiente, variables, vector)
    dk = [i * -1 for i in gk]

    while 1:
        # Se calcula el alpha
        ak = calcular_ak(funcion, variables, vector, dk, gk)

        # Se calcula el nuevo valor del vector: x1 = x0 + a * d0
        ak_dk = [i * ak for i in dk]
        vec_1 = [x1 + x2 for (x1, x2) in zip(vector, ak_dk)]

        # Se calcula el nuevo valor del vector gk
        gk_1 = evaluar_gradiente(gradiente, variables, vec_1)

        # Se calcula el vector para la condicion de parada
        vec_parada = evaluar_gradiente(gradiente, variables, vec_1)

        # Se calcula la norma 2 del vector para la condicion de parada
        norma_2 = linalg.norm(array(vec_parada, dtype='float'), 2)

        # Se verifica la condicion de parada
        if norma_2 < tol:
            break

        # Se calcula el valor de beta
        bk = calcular_bk(gk_1, gk, dk, regla_bk)

        # Se calcula el nuevo valor del vector dk
        bk_dk = [i * bk for i in dk]
        m_gk_1 = [i * -1 for i in gk_1]
        dk = [x1 + x2 for (x1, x2) in zip(m_gk_1, bk_dk)]

        vector = vec_1.copy()
        gk = gk_1.copy()
        itr += 1

    return [vec_1, itr]


def evaluar_gradiente(gradiente, variables, vector):
    """
    Funcion para evaluar el gradradiente con un vector ingresado
    :param gradiente: gradiente que se debe evaluar
    :param variables: lista con las variables simbolicas de la ecuacion
    :param vector: vector que se debe evaluar en el gradiente
    :return: resultado de evaluar el vector en el gradiente
    """
    n = len(variables)
    resultado = []

    # Se recorre cada una de las derivadas parciales en el gradiente
    for i in range(0, n):
        # Se obtiene la derivada parcial
        funcion = gradiente[i]

        # Se sustituyen cada una de las variables por el valor en el vector
        for x in range(0, n):
            funcion = funcion.subs(variables[x], vector[x])

        resultado += [funcion.doit()]

    return resultado


def evaluar_funcion(funcion, variables, vector):
    """
    Funcion para evaluar un vector en una funcion
    :param funcion: funcion a evaluar
    :param variables: lista con las variables simbolicas de la ecuacion
    :param vector: vector a evaluar en la funcion
    :return: resultado de evaluar el vector en la funcion
    """
    n = len(variables)
    # Se sustituyen cada una de las variables por el valor en el vector
    for x in range(0, n):
        funcion = funcion.subs(variables[x], vector[x])
    return funcion


def calcular_ak(funcion, variables, vector, d_k, g_k):
    """
    Se calcula el ak, encontrando el primer valor que cumpla con la desigualdad
    f(vector + ak * dk) - f(vector) <= 0.5 * ak * gk * dk
    :param funcion: funcion que se debe evaluar
    :param variables: lista con las variables de la ecuacion
    :param vector: vector de la solucion aproximada
    :param d_k: vector d de la iteracion k
    :param g_k: vector g de la iteracion k
    :return: valor de a que cumple con la desigualdad
    """
    a = 1
    while 1:
        # Se calcula la multiplicacion de ak * dk
        a_dk = [i * a for i in d_k]

        # Se calcula la operacion vector + a * dk
        vec_a_dk = [x1 + x2 for (x1, x2) in zip(vector, a_dk)]

        # Se evalua la funcion f(vector + a * dk)
        f_vec_a_dk = evaluar_funcion(funcion, variables, vec_a_dk)

        # Se evalua la funcion f(vector)
        f_vec = evaluar_funcion(funcion, variables, vector)

        # Se calcula la primera parte de la desigualdad
        parte1 = f_vec_a_dk - f_vec

        # Se calcula la operacion gk * dk
        gk_dk = [x1 * x2 for (x1, x2) in zip(g_k, d_k)]

        # Se suman todos los elementos de gk_dk
        suma_gk_dk = sum(gk_dk)

        # Se calcula la multiplicacion de 0.5 * ak * gk * dk
        parte2 = 0.5 * a * suma_gk_dk

        # Se verifica la desigualdad
        if parte1 <= parte2:
            break

        a /= 2

    return a


def calcular_bk(gk, gk_ant, dk, regla_bk):
    """
    Funcion para calcular la regla_bk
    :param gk: vector gk
    :param gk_ant: vector gk de la iteracion anterior
    :param dk: vector dk
    :param regla_bk: regla deseada para calcular bk
    :return: valor de bk calculado
    """
    # Se calcula la norma 2 del vector actual
    gk_norma_2 = linalg.norm(array(gk, dtype='float'), 2)

    # Metodo de Fletcher and Reeves
    if regla_bk == 'FR':
        # Se calcula la norma 2 del vector anterior
        gk_ant_norma_2 = linalg.norm(array(gk_ant, dtype='float'), 2)

        b = gk_norma_2 ** 2 / gk_ant_norma_2 ** 2
        return b

    # Metodo de Descenso Conjugado CD
    if regla_bk == 'CD':
        # Se calcula la operacion -dk * gk
        m_dk = [i * -1 for i in dk]
        dk_gk = [x1 * x2 for (x1, x2) in zip(gk_ant, m_dk)]
        suma = sum(dk_gk)

        b = gk_norma_2 ** 2 / suma
        return b

    # Metodo de Dai y Yuan
    else:
        yk = [x1 - x2 for (x1, x2) in zip(gk, gk_ant)]
        dk_yk = [x1 * x2 for (x1, x2) in zip(dk, yk)]
        b = gk_norma_2 ** 2 / sum(dk_yk)

        return b


# str_f = '(x-2)**4 + (x-2*y)**2'
# var = ['x', 'y']
# print(gradiente_conjugado(str_f, var, [0, 3], 10 ** -5, 'CD'))

# str_funcion1 = '(x - 2) ** 2 + (y + 3) ** 2 + x * y'
# variables1 = ['x', 'y']
# vector1 = [1, 1]
# print(gradiente_conjugado(str_funcion1, variables1, vector1, 10**-5))

# str_funcion2 = 'x ** 3 + y ** 3 + z ** 3 - 2 * x * y - 2 * x * z - 2 * y * z'
# variables2 = ['x', 'y', 'z']
# vector2 = [1, 1, 1]
# print(gradiente_conjugado(str_funcion2, variables2, vector2, 10**-5))
