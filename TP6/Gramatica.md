<h1 align="center">Símbolos gramaticais</h1>

## Terminais:

- Números: `num`
- Variáveis: `var`
- Operadores Aritméticos: `+ | - | * | /`
- Parênteses: `( | )`
- Igualdade: `=`
- Leitura: `?`
- Impressão: `!`

## Não-Terminais:

- Programa: `P`
- Declaração: `D`
- Expressão: `E`
- Termo: `T`
- Fator (expressão entre parênteses): `F`

## Produções

```
p1: P -> D P | ε
p2: D -> ? var | var = E
p3: E -> E + T | E - T | T
p4: T -> T * F | T / F | F
p5: F -> ( E ) | num | var
```

## Lookaheads
```
LA(P → D P): ?, var, !
LA(P → ε): EOF (fim do arquivo)
LA(D → ? var): ?
LA(D → var = E): var
LA(D → ! E): !
LA(E → E + T): +, -, (, num, var
LA(E → E - T): +, -, (, num, var
LA(E → T): (, num, var
LA(T → T * F): *, /, (, num, var
LA(T → T / F): *, /, (, num, var
LA(T → F): (, num, var
LA(F → ( E )): (
LA(F → num): num
LA(F → var): var
```
