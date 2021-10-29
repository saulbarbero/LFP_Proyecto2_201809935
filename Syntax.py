from Token import Token
from Reservadas import PR
from Error import Error
class Syntax:
    def __init__(self,tokens):
        self.tokens = tokens
        self.lista_errores = []
        self.n = 0
        self.error = True


    def Llamada_funcion(self):
        self.match(self.tokens[self.n].lexema,"(")
        self.Parametro()
        self.match(self.tokens[self.n].lexema,")")
        self.match(self.tokens[self.n].lexema,";")