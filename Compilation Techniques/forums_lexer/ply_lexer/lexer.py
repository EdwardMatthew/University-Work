import ply.lex as lex

reserved = {
        'class' : 'CLASS',
        'function' : 'FUNCTION',
        'echo' : 'ECHO',
        '<?php' : 'PHPOPENINGTAG',
}


tokens = ['LPAREN', 'RPAREN', 'NUMBER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'ID']  + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PHPOPENINGTAG(t):
    r'(?:^|\W)\<?php(?:$|\W)'
    t.type = reserved.get(t.value, 'PHPOPENINGTAG')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


data = '<?php (10 + 10)'

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break 
    print(tok)
