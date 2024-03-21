<h1 align="center">TP6</h1>

## Autor
- Pedro Silva
- A100745

## Descrição
Implementação de uma GIC (Gramática Independente de Contexto) para realização de operações matemáticas.
A gramática pode ser analisada em detalhe [aqui](https://github.com/Pedrosilva03/PL2024/blob/main/TP6/Gramatica.md)

## Funcionamento

- **Definições**: A gramática possui símbolos terminais como números, variáveis, operadores aritméticos, parênteses, igualdade, leitura e impressão. Possui também símbolos não-terminais que incluem o programa (P), declaração (D), expressão (E), termo (T) e fator (F).

- **Produções da Gramática**: descrevem como os diferentes símbolos da linguagem podem ser combinados para formar expressões válidas. 

- **Lookahead Sets**: são determinados para cada produção, indicando os símbolos que podem seguir imediatamente após a expansão da produção.
