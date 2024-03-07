from ply import lex

# Lista de tokens
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'IDENTIFIER',
    'NUMBER',
    'OPERATOR',
    'COMMA',
)

# Expressões regulares para tokens simples
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_COMMA = r','
t_OPERATOR = r'[><=!]+'

# Função para identificar IDENTIFIERs
def t_IDENTIFIER(t):
    r'[a-zA-Z_]\w*'
    return t

# Função para identificar NUMBERs
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# Ignorar espaços em branco
t_ignore = ' \t'

# Ignorar comentários
def t_comment(t):
    r'\#.*'
    pass

# Contador de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print("Caráter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def ana(input):
    final = []
    
    # Criar analisador léxico
    lexer = lex.lex()
    lexer.input(input)
    while True:
        tok = lexer.token()
        if not tok:
            break
        final.append(tok)
    return str(final)