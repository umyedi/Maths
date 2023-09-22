# ----------------
# | EXERCICE 1.d |
# ----------------

def multiple_7(x: str):
    table_7 = [7*i for i in range(1, 11)]
    while int(x) not in table_7:
        a = int(x[:-1])
        b = int(x[-1])
        x = str(a + 5*b)
        print(f"{a} + 5 x {b} = {x}")
        
        if len(x) < 2:
            return False
    return True

# Résultat de mutiple_7("225533") :
# >> 22553 + 5 x 3 = 22568
# >> 2256 + 5 x 8 = 2296
# >> 229 + 5 x 6 = 259
# >> 25 + 5 x 9 = 70
