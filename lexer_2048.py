from sly import Lexer
import sys


class MyLexer(Lexer):

    tokens = { NAME, NUMBER, ASSIGN,ADD,SUBTRACT,MULTIPLY,DIVIDE,LEFT,RIGHT,
                 UP,DOWN,ASSIGN,TO,VAR,
                IS,VALUE,IN,COMMA,FS,TRASH}
    ignore = ' \t'

    # Tokens
    ADD=r'ADD'
    SUBTRACT=r'SUBTRACT'
    MULTIPLY=r'MULTIPLY'
    DIVIDE=r'DIVIDE'
    LEFT=r'LEFT'
    RIGHT=r'RIGHT'
    UP=r'UP'
    DOWN=r'DOWN'
    ASSIGN=r'ASSIGN'
    TO=r'TO'
    VAR=r'VAR'
    IS=r'IS'
    VALUE=r'VALUE'
    IN=r'IN'
    COMMA=r','
    FS=r'\.'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    #NUMBER = r'\d+'

    # Ignored pattern
    ignore_newline = r'\n+'

    @_(r"(0|[1-9][0-9]*)")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t
    
    @_(r"[@!#$%^&*()_+-=~`]+")
    def TRASH(self,t):
        return t
    
    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
        return 
        
