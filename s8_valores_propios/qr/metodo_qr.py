from scipy import linalg as la
from numpy import matrix, zeros


def metodo_qr(A, tol):
    """
    Metodo QR para encontrar todos los autovalores de una matriz
    :param A: Matriz A
    :param tol: Tolerancia al fallo que debe tener el resultado
    :return: Matriz con todos los autovalores de la matriz A
    """
    A = matrix(A)
    A_ant = matrix(zeros(A.shape))

    while 1:
        Q, R = la.qr(A)
        A_ant = A
        A = R * Q

        # Se verifica la condicion de parada
        norma = la.norm(A_ant - A)
        if norma < tol:
            break

    return A


# resultado = metodo_qr([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], 10 ** -6)
# print(resultado)
