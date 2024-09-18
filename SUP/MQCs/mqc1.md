# QCM n°1 (12/09)

## OCaml

### Question 1

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
2000 + 29;;
```

<!-- Réponse (a) : `- : int = 2029` -->

### Question 2

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let a = true;;
```
<!-- Réponse (d) : `val a : bool = true` -->

### Question 3

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let y = let x = 2 and y = 3 in x + y;;
```
<!-- Réponse (b) : `val y : int = 5` -->

### Question 4

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let a = true in
    let b = false in
        a && (b || a);;
```
<!-- Réponse (a) : `- : bool = true` -->

### Question 5

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let a =
    (let b = 3 in b*(a-1))
    + (let b = 2 in b*(a+1)) ;;
```
<!-- Réponse (d) : Une erreur -->

### Question 6

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let f x = let conv = float_of_int x in conv < 42.;;
```
<!-- Réponse (c) : `val f : int -> bool = <fun>` -->

### Question 7

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let cpt = 12 in let conv = float_of_int cpt;;
```
<!-- Réponse (d) : Une erreur -->

### Question 8

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let f x = x + 1 in
    let g x = x/8 in
        f 4 + g 16;;
```
<!-- Réponse (a) : `- : int = 7` -->

### Question 9

> Quel est le résultat de l'évaluation de la phrase suivante ?

```ocaml
let h2 x = let h x = x/2 + 8 in h (x-1) = 0;;
```
<!-- Réponse (d) : `val h2 : int -> bool = <fun>` -->

### Question 10

> Que donnera l'application `h2 42` (`h2` défini question précédente). 

<!-- Réponse (c) : `- : bool = false` -->
