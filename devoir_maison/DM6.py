def modular_inverse(number: int, modulo: int) -> int:
    for inverse in range(modulo):
        if (number * inverse) % modulo == 1:
            return inverse
    return None


def encode_number_affine(a: int, b: int, x: int, modulo: int) -> int:
    return (a * x + b) % modulo


def decode_number_affine(a: int, b: int, y: int, modulo: int) -> int:
    if modular_inverse(a, modulo) is None:
        return None
    mod_inv = modular_inverse(a, modulo)
    return (y - b) * mod_inv % modulo

def display_table(a: int, b: int):
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

display_table(3, 11)