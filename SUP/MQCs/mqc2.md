# QCM n°2 (13/09)

## OCaml

### Question 1

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let f x = let conv = float_of_int x in conv < 42.;;
```
<!-- Réponse (c) : `val f : int -> bool = <fun>` -->

### Question 2

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let f x = x + 1 in
    let g x = x/8 in
        g 4 + f 16;;
```
<!-- Réponse (c) : `- : int = 17` -->

### Question 3

> Quel est le résultat de l'évaluation de la définition suivante ?

```ocaml
let f x y z =
    let b = x < int_of_float y in
        b = z;;
```
<!-- Réponse (c) : `val f : int -> float -> bool -> bool = <fun>` -->

### Question 4

> Quel est le résultat de l'évaluation de l'expression suivante ?

```ocaml
let f x y = x/y in
    let g x y = x*y in
        f ((g (3*2) 4)+1) (5 - f 1 2) ;;
```
<!-- Réponse (b) : `- : int = 5` -->

### Question 5

> Quel est le résultat de l'évaluation de la définition suivante ?

```ocaml
let f x y =
    let f2 x y z = z = (x + y)/2 in
        if f2 x 10 y then
            x
        else
            z ;;
```
<!-- Réponse (d) : Une erreur -->

### Question 6

> Quel est le résultat de l'évaluation de la définition suivante ?

```ocaml
let f x y = if x > 4 then
        y
    else
        let y = false;;
```
<!-- Réponse (e) : Une erreur -->

### Question 7

> Quel est le résultat de l'évaluation de la définition suivante ?

```ocaml
let f x y =
    if x > y then
        (if x mod 2 = 0 then false else true)
    else
        false;;
```
<!-- Réponse (c) : `val f : int -> int -> bool = <fun>` -->

### Question 8

> Que calcule la fonction suivante appliquée à deux valeurs booléennes `a` et `b` ?

```ocaml
let op a b = if a then b else true ;;
```
<!-- Réponse (c) : `not a || b` -->

### Question 9

> Quel est le résultat de l'évaluation de l'expression suivante ?

```ocaml
let a = 13 and b = 3 in
    2* ((if a > b then a - b else b - a) + (if a > b then a / b else b / a)) ;;
```
<!-- Réponse (b) : `- : int = 28` -->

### Question 10

> Parmis les phrases suivantes, quelle est l'intruse ?

```ocaml
(a) let even n = if n mod 2 = 0 then true else false ;;
(b) let even n = n mod 2 = 0 ;;
(c) let even n = let r = n - n/2*2 in r = 0 ;;
(d) let even n = n mod 2
(e) let even n = n - n/2*2 = 0 ;;
```
<!-- Réponse (d) : `let even n = n mod 2` -->
