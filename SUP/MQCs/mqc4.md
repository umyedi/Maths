# QCM n°4 (17/09)

## OCaml

### Question 1

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let f x y = match x mod y with
      0 -> failwith "error"
    | r -> true
    | r when r < 0 -> false;;
```
<!-- Réponse (a/b) : `Warning ... : this match case is unused.` et `val f : int -> int -> bool = <fun>` -->

### Question 2

> Quel sera le résultat de l'application de `f` (question précédente) aux valeurs `12` et `4` ?

```ocaml
f 12 4;;
```
<!-- Réponse (d) : `Exception: Failure "error".` -->

### Question 3

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let x = 42 in (42., x, "24");;
```
<!-- Réponse (b) : `- : float * int * string = (42., 42, "24")` -->

### Question 4

> Quel sera le dernier résultat après l'évaluation successive des phrases suivantes ?

```ocaml
let y = let x = (("one",(1,1.),'1'),"wow") in (x, "hum");;
let (x, y) = y in y;;
```
<!-- Réponse (c) : `- : string = "hum"` -->

### Question 5

> Quel est le résultat de l'évaluation de la définition suivante ?

```ocaml
let f x y =
    let g x = (x + 1)/2 in
        match (not x, g y) with
        (true, _) -> true
      | (_, 42) -> false
      | _ -> failwith "error";;
```
<!-- Réponse (e) : `val f : bool -> int -> bool = <fun>` -->

### Question 6

> Quel sera le dernier résultat après l'évaluation successive des phrases suivantes ?

```ocaml
let g x y z = match (y, x) with
      (1, x)    -> (1, x)
    | (y, true) -> (2*y, true)
    | _         -> failwith "error" ;;
g true 4 "error";;
```
<!-- Réponse (c) : `- : int * bool = (8, true)` -->

### Question 7

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let b = let a = 2. in function x -> let b = 5. in x*.a > b || x=0. ;;
```
<!-- Réponse (c) : `val b : float -> bool = <fun>` -->

### Question 8

> Quel sera le dernier résultat après l'évaluation successive des phrases suivantes ?

```ocaml
let f = function
      (x, y) when x = y   -> 1
    | (_, 0)            -> 0
    | _                 -> -1;;
f (0, 0);;
```
<!-- Réponse (b) : `- : int = 1` -->

### Question 9

> Quel est le résultat de l'évaluation de la définition suivante ?

```ocaml
let f = function
      "/"       -> (function (a,b) -> a/b)
    | "mod"     -> (function (a,b) -> a mod b)
    | "divmod"  -> (function (a,b) -> (a / b, a mod b))
    | _         -> (failwith "unknown") ;;
```
<!-- Réponse (d) : Une erreur -->

### Question 10

> Que contient le résultat de l'évaluation de la phrase suivante ?

```ocaml
let h x y = match x with
      y -> 1
    | _ -> x ;;
```
<!-- Réponse (a/c) : `Warning ... : this match case is unused.` et `val h : int -> 'a -> int = <fun>` -->
