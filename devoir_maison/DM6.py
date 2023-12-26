import itertools
from typing import List


def encode(a: int, b: int, list_x: List[int]) -> List:
    """
    Encode une liste de valeurs en utilisant le chiffrement affine avec les coefficients 'a' et 'b'.

    Args:
        a (int): Coefficient multiplicatif, entier naturel compris entre 0 (inclus) et 26 (exclus).
        b (int): Coefficient additif, entier naturel compris entre 0 (inclus) et 26 (exclus).
        list_x (List[int]): Liste des valeurs originales à encoder (liste d'entiers relatifs).

    Returns:
        List: Liste des valeurs encodées correspondant à chaque élément de 'list_x'.

    Exemple:
        >>> encode(3, 1, [0, 1, 2])
        [1, 4, 7]
    """
    return [(a * x + b) % 26 for x in list_x]


def decode(list_x: List, list_y: List) -> List:
    """
    Décrypte une liste de valeurs encodées en utilisant le chiffrement affine et retourne les coefficients de décodage.

    Args:
        list_x (List): Liste des 26 indices des caractères avant encodage (liste d'entiers relatifs).
        list_y (List): Liste des indices des caractères après encodage (liste d'entiers relatifs).

    Returns:
        List: La paire (a, b) utilisée pour l'encodage si une solution existe, sinon None.

    Exemple:
        >>> decode([0, 1, 2], [1, 4, 7])
        (3, 1)
    """
    for a, b in itertools.product(range(1, 26), range(26)):
        if all(y == (a * x + b) % 26 for x, y in zip(list_x, list_y)):
            return (a, b)
    return None

list_x = list(range(26)) # Liste des entiers de 0 à 25 inclus
list_y = encode(3, 11, list_x) # Liste encodé

print(decode(list_x, list_y)) # Trouve les entiers a et b avec lesquelles la liste 'list_x' a été encodé