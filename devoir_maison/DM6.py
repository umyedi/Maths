def modular_inverse(number: int, modulo: int) -> int:
    """
    Calcule l'inverse modulaire d'un nombre donné.

    Args:
        number (int): Nombre dont on veut calculer l'inverse modulaire.
        modulo (int): Modulo dans lequel l'inverse modulaire est calculé.

    Returns:
        int: Retourne l'inverse modulaire du nombre. Retourne None si l'inverse modulaire n'existe pas.
    """
    for inverse in range(modulo):
        if (number * inverse) % modulo == 1:
            return inverse
    return None


def encode_number_affine(a: int, b: int, x: int, modulo: int) -> int:
    """
    Encode un nombre en utilisant le chiffrement affine.

    Args:
        a (int): Coefficient multiplicatif.
        b (int): Coefficient additif.
        x (int): Nombre à encoder.
        modulo (int): Modulo dans lequel l'encodage est effectué.

    Returns:
        int: Nombre encodé après le chiffrement affine.
    """
    return (a * x + b) % modulo


def decode_number_affine(a: int, b: int, y: int, modulo: int) -> int:
    """
    Décode un nombre encodé avec le chiffrement affine.

    Args:
        a (int): Coefficient multiplicatif 
        b (int): Coefficient additif
        y (int): Nombre à décoder.
        modulo (int): Modulo dans lequel le décodage est effectué.

    Returns:
        int: Nombre décodé avec le chiffrement affine. Retourne None si le décodage est impossible.
    """
    if modular_inverse(a, modulo):
        return (y - b) * modular_inverse(a, modulo) % modulo
    return None

def display_table(a: int, b: int):
    """
    Affiche une table d'encodage/décodage basée sur le chiffrement affine pour les lettres de l'alphabet.

    Args:
        a (int): Coefficient multiplicatif
        b (int): Coefficient additif
    """
    letters = [chr(i + 65) for i in range(26)]
    indices = list(range(26))
    encoded_indices = [encode_number_affine(a, b, i, 26) for i in indices]
    encoded_letters = [chr(i + 65) for i in encoded_indices]

    print("-" * 106)
    print("|" + "|".join(f"{char:^3}" for char in letters) + "|")
    print("-" * 106)
    print("|" + "|".join(f"{i:^3}" for i in indices) + "|")
    print("-" * 106)
    print("|" + "|".join(f"{i:^3}" for i in encoded_indices) + "|")
    print("-" * 106)
    print("|" + "|".join(f"{char:^3}" for char in encoded_letters) + "|")
    print("-" * 106)


# Ex. 1 - Partie A - 1.b
display_table(3, 11)