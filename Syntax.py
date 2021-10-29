from Token import Token
from Reservadas import PR
from Error import Error
class Syntax:
    def __init__(self,tokens):
        self.tokens = tokens
        self.lista_erroresS = []
        self.n = 0
        self.error = True

    def Analizar(self):
        t= Token(PR.SYMBOL,"$",0,0)
        self.tokens.append(t)
        e = Error("Error sintactico: prueba",0,0)
        self.lista_erroresS.append(e)
        while self.tokens[self.n].lexema != None:
            if(self.tokens[self.n].lexema=="$"):
                break
            self.match(self.tokens[self.n].token,PR.ID)
            
            if self.tokens[self.n].lexema == "(":
                self.Llamada_funcion()
            elif self.tokens[self.n].lexema == "=":
                self.match(self.tokens[self.n].lexema,"=")

                self.match(self.tokens[self.n].lexema,"[")
                #if self.tokens[self.n].lexema == "{":
                    #Registro()
                #else:
                    #Parametro_clave()
            else:
                self.error = False
                e = Error("Error sintactico:"+self.tokens[self.n].lexema,0,0)
                self.lista_erroresS.append(e)
                break
                #Error


    def Llamada_funcion(self):
        self.match(self.tokens[self.n].lexema,"(")
        self.Parametro()
        self.match(self.tokens[self.n].lexema,")")
        self.match(self.tokens[self.n].lexema,";")

    def Parametro (self):
        if(self.tokens[self.n].token == PR.CADENA):
           self.match(self.tokens[self.n].token,PR.CADENA)
        elif(self.tokens[self.n].token == PR.NUM):
           self.match(self.tokens[self.n].token,PR.NUM)
        elif(self.tokens[self.n].token == PR.DECI):
           self.match(self.tokens[self.n].token,PR.DECI)
        else:
            self.error = False
            e = Error("Error sintactico:"+self.tokens[self.n].lexema,0,0)
            self.lista_erroresS.append(e)


        if(self.tokens[self.n].lexema == ","):
                self.match(self.tokens[self.n].lexema,",")
                self.Parametro()

    def match(self,token, token_esperado):
        print(str(token),":",str(token_esperado))
        if(self.error):
            if( token != token_esperado):
                if(self.tokens[self.n].lexema=="$"):
                    self.error = False
                e = Error("Error sintactico:"+str(token),0,0)
                self.lista_erroresS.append(e)
        self.n+=1