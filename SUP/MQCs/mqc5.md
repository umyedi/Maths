# QCM n°5 (19/09)

## OCaml

### Question 1

> Quel est le résultat de l'évaluation de la définition suivante ?

```ocaml
let f x y =
    let g x = (x + 1)/ 2 in
        match (not x, g y) with
        (true, _) -> true
      | (_, 42) -> false
      | _ -> failwith "error" ;;
```
<!-- Réponse (a) : `val f : bool -> int -> bool = <fun>` -->

### Question 2

> Quel sera le dernier résultat après l'évaluation des phrases suivantes ?

```ocaml
let f = function
    (x, y) when x <> y  -> 1
  | (_, 0)              -> 0
  | _                   -> -1;;
f (0, 0);;
```
<!-- Réponse (c) : `- : int = 0` -->

### Question 3

> Qu'affiche la fonction suivante appelée avec `f 5` ?

```ocaml
let rec f x = match x with
    0 -> ()
    | x when x mod 2 = 0 -> f (x-1) ; print_int x
    | _ -> print_int x ; f (x-1);;
```
<!-- Réponse (a) : `53124` -->

### Question 4

> Que calcule la fonction suivante appelée avec `f n` $(n\leq 1)$ ?

```ocaml
let rec f n =
    if n = 1 then
        1.
    else
        1. /. (float_of_int n) +. f (n - 1);;
```
<!-- Réponse (b) : $\sum_{i=1}^{n} \frac{1}{i}$ -->

### Question 5

> Quel sera le dernier résultat après l'évaluation des phrases suivantes ?

```ocaml
let rec f n =
    if n < 10 then
        n
    else
        f (n mod 10 + n / 10);;
f 12345;;
```
<!-- Réponse (d) : `- : int = 6` -->

### Question 6

> Quel sera le dernier résultat après l'évaluation des phrases suivantes ?


```ocaml
let rec f n k =
    if k = 0 then
        1
    else
        if n mod 2 = 0 then
            1 + f (n - 1) (k - 1)
        else
            2 + f (n - 1) k;;
f 3 1;;
```
<!-- Réponse (c) : `- : int = 4` -->

### Question 7

> Quel sera le dernier résultat après l'évaluation des phrases suivantes ?

```ocaml
let rec f n =
    if n <= 1 then
        n
    else
        2 * f (n - 1) + f (n - 1);;
f 4;;
```
<!-- Réponse (d) : `- : int = 27` -->

### Question 8

> Quel sera le dernier résultat après l'évaluation des phrases suivantes ?

```ocaml
let rec f n d =
    if n = 0 then
        0
    else
        (if n mod 10 = d then 1 else 0) + f (n / 10) d;;
f 5454253;;
```
<!-- Réponse (c) : `- : int = 3` -->

### Question 9

> Quel sera le dernier résultat après l'évaluation des phrases suivantes ?

```ocaml
let rec f n d =
    if n = 0 then
        0
    else
        if n mod d = 0 then
            1 + f (n/10) d
        else
            f (n/10) (d-1);;
f 4355 5;;
```
<!-- Réponse (c) : `- : int = 3` -->

### Question 10

> Quel sera le dernier résultat après l'évaluation des phrases suivantes ?

```ocaml
let rec f n =
    if n = 0 then
        0
    else if n mod 2 = 0 then
        -n + f (n - 1)
    else
        n + f (n - 1);;
f 5;;
```
<!-- Réponse (c) : `- : int = 3` -->
