import itertools
import string
from typing import List
from pprint import pprint

ALPHABET = string.ascii_uppercase
def encodage(alphabet: List, a:int, b:int) -> List:
    codage, list_y = [], []
    for x in range(len(alphabet)):
        y = (a*x + b) % 26
        list_y.append(y)
        codage.append(alphabet[y])
    return [list_y, codage]

def decodage(list_x: List, list_y: List):
    resultat = []
    for i, a, b in itertools.product(range(len(list_x)), range(26), range(26)):
        if (list_x[i]%26) == (a*list_y[i] + b):
            resultat.append((a,b))
    for a, b in resultat:
        print([(list_y[i] - list_x[i] * a + b % 26) == 0 for i in range(len(list_x))])
    # pprint(sorted(resultat))

encode = encodage(ALPHABET, 3, 11)
print(encode)
decode = decodage(list(range(26)), 
                  [11, 14, 17, 20, 23, 0, 3, 6, 9, 12, 15, 18, 21, 24, 1, 4, 7, 10, 13, 16, 19, 22, 25, 2, 5, 8])
