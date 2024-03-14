from ply import lex

tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SALDO',
    'ADICIONAR',
    'SAIR',
]

menu = """
        Bem-vindo à máquina de venda automática.
        Comandos disponíveis:
        - SALDO
        - MOEDA <quantia>e e/ou <quantia>c
        - LISTAR
        - SELECIONAR <produto>  
        - SAIR
        """

def start(stock):
    lexer = lex.lex()

    lexer.stock = stock
    lexer.saldo = 0

    print(menu)

    lexer.state = 1

    while lexer.state != 0:
        pass

    while True:
        input("")