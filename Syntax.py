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

    def match(self,token, token_esperado):
        print(str(token),":",str(token_esperado))
        if(self.error):
            if( token != token_esperado):
                if(self.tokens[self.n].lexema=="$"):
                    self.error = False
                e = Error("Error sintactico:"+str(token),0,0)
                self.lista_errores.append(e)
        self.n+=1