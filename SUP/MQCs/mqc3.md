# QCM n°3 (16/09)

## OCaml

### Question 1

> Quel est le résultat de l'évaluation de la définition suivante ?

```ocaml
let f x y z =
    let b = x < int_of_float y in
        b = z;;
```
<!-- Réponse (c) : `val f : int -> float -> bool -> bool = <fun>` -->

### Question 2

> Quel est le résultat de l'évaluation de l'expression suivante ?

```ocaml
let a = 13 and b = 3 in
    2* ((if a > b then b - a else a - b) + (if a > b then a / b else b / a)) ;;
```
<!-- Réponse (c) : `- : int = -12` -->

### Question 3

> Quel est le résultat de l'évaluation de la définition suivante ?

```ocaml
let f x y = match x with
    | 0 -> failwith "error1"
    | x when x > 0 -> x/y
    | _ -> failwith "error2";;
```
<!-- Réponse (a) : `val f : int -> int -> int = <fun>` -->

### Question 4

> Quel sera le résultat de l'application de `f` (question précédente) aux valeurs `(-3)` et `0` ?

```ocaml
f (-3) 0;;
```
<!-- Réponse (a) : `Exception: Failure "error2".` -->

### Question 5

> Quel est le type de la fonction `divide` ?

```ocaml
let divide x y =
    if x = 0 then
        failwith "impossible1"
    else
        if x > 0 then
            (match y with
                 y when y > 0 -> x/y
                |_ -> x/(-y)
            )
        else
            failwith "impossible2";;
```
<!-- Réponse (d) : `int -> int -> int` -->

### Question 6

> Quel sera le résultat de l'application de `divide` (question précédente) aux valeurs `12` et `0` ?

```ocaml
divide 12 0;;
```
<!-- Réponse (b) : `Exception: Division_by_zero.` -->

### Question 7

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let f x y = match x mod y with
      r when r < 0 -> false
    | r -> true
    | 0 -> failwith "error" ;;
```
<!-- Réponse (a/b) : `Warning ... : this match case is unused.` et `val f : int -> int -> bool = <fun>` -->

### Question 8

> Quel sera le résultat de l'application de `f` (question précédente) aux valeurs `12` et `4` ?

```ocaml
f 12 4;;
```
<!-- Réponse (b) : `- : bool = true` -->

### Question 9

> Que contient le résultat de l'évaluation de la phrase suivante ?

```ocaml
let h x y = match x with
      'A' -> let tmp = y * 10 in
        (match tmp with
             0 -> tmp
            |_ -> y)
    | 'B' -> y * 10;;
```
<!-- Réponse (a/c) : `Warning ... : this pattern-matching is not exhaustive.` et `val h : char -> int -> int = <fun>` -->

### Question 10

> Quel sera le résultat de l'application de `h` (question précédente) aux valeurs `'A'` et `13` ?

```ocaml
h 'A' 13;;
```
<!-- Réponse (a) : `- : int = 13` -->
