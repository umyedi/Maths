from random import randint
from typing import List
from math import sqrt

# Lien de la démonstration (PDF) : https://bit.ly/download_demo_DM5

# La fontion 'check_result' à été testé avec les valeures suivantes :
#   - iterations = 100 000 000
#   - minimum = -100
#   - maximum = 100
# et aucune matrice ne remplissant pas les conditions n'a été trouvée

def generate_matrix(
    n: int, p: int, min: int = None, max: int = None) -> List[List[int]]:
    """Retourne une matrice nulle de dimensions n*p.
    Si 'min' et 'max' sont définis, chaque coefficient de la matrice est remplacée avec une valeur aléatoire comprise
    entre 'min' et 'max'

    Args:
        n (int): Nombre de lignes de la matrice.
        p (int): Nombre de colonnes de la matrice.
        min (int) : Valeur minimale de chaque coefficients. Valeur par défault : None.
        max (int) : Valeur maximale de chaque coefficients. Valeur par défault : None.

    Returns:
        List[List[int]]: Matrice de taille n*p.
    """
    if min and max:
        return [[randint(min, max) for _ in range(p)] for _ in range(n)]
    return [[0 for _ in range(p)] for _ in range(n)]


def display_matrix(matrix: List[List[int]]) -> None:
    """Affiche proprement une matrice donnée.

    Args:
        matrix (List[List[int]]): Matrice à afficher.
    """
    for line in matrix:
        print(line)


def square_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """Renvoie le carré d'une matrice donnée.

    Args:
        matrix (List[List[int]]): Matrice originale.

    Returns:
        List[List[int]]: Matrice carrée
    """
    n = len(matrix)
    p = len(matrix[0])
    squared_matrix = generate_matrix(n, p)
    for i in range(n):
        for j in range(p):
            for k in range(p):
                squared_matrix[i][j] += matrix[i][k] * matrix[k][j]
    return squared_matrix


def conditions(matrix: List[List[int]]) -> bool:
    """Renvoie un booléen qui vérifie que les conditions trouvées dans les exercices sont remplies.

    Args:
        matrix (List[List[int]]): Matrice de dimensions 2*2.

    Returns:
        bool: Vrai si au moins une contidion est remplie. False sinon.
    """
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    # CONDITIONS 1
    if (
        b * c <= 1
        and a + d == 0
        and (
            a == -sqrt(1 - b * c)
            and d == sqrt(1 - b * c)
            or a == sqrt(1 - b * c)
            and d == -sqrt(1 - b * c)
        )
    ):
        return True
    # CONDITIONS 2
    if matrix == [[1, 0], [0, 1]] or matrix == [[-1, 0], [0, -1]]:
        return True
    # CONDITIONS 3
    if matrix == [[0, 1], [1, 0]] or matrix == [[0, -1], [-1, 0]]:
        return True
    return False


def check_result(iterations: int) -> None:
    """Vérifie qu'il n'existe pas d'autre conditions que celles trouvées.
    Pour un nombre donnée d'itérations, on génère une matrice de dimensions 2*2 avec des valeurs aléatoires : si le
    carrée de la matrice est égal à l'identité et que les conditions ne sont pas rempliques, on affiche cette matrice

    Args:
        iterations (int): Nombre de fois qu'on génère une matrice.
    """
    minimum = int(input("Minimum argument value: "))
    maximum = int(input("Maximum argument value: "))

    for i in range(iterations):
        matrix = generate_matrix(2, 2, minimum, maximum)
        print(f"Working: {round(i/iterations*100, 1)}% : {matrix}", end="\r")

        if square_matrix(matrix) == [[1, 0], [0, 1]] and conditions(matrix) == False:
            print("--------------")
            display_matrix(matrix)
            print("--------------")


if __name__ == "__main__":
    check_result(int(input("Number of operations: ")))
