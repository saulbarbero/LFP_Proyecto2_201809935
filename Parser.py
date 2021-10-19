from Token import Token
from Reservadas import PR

class Parser:
    def __init__(self):
        self.tokens = []
        self.lista_errores = []

        
    def imprimir(self):
        print("En parser")

    def obtenerData(self,data): 
        estado = 0 
        aux = ''
        fila = 1
        columna =0
        i=0
        while i in range(len(data)):
            x = data[i]
            if(estado==0):
                
                if(x == '=' or x == ',' or x== '{'  or x == '}'  or x == '['  or x == ']' ): #Ignorar
                    t = Token(PR.SYMBOL,x,fila,columna)
                    self.tokens.append(t)
                    pass  
                elif(x ==' ' or x == '\r' or x == '\t' ):
                    pass 
                elif(x == '\n'):
                    fila+=1
                    columna=0
                elif(x.isalpha()):
                    aux +=x
                    estado = 1
                elif(x == '"'):
                    aux+=x
                    estado = 2
                elif(x.isdigit()):
                    aux +=x
                    estado = 3
                elif(x == '#'):
                    estado = 4
                    aux+=x
                elif(x == "'"):
                    estado = 5
                    aux+=x
                else:
                    
                    aux = ''
                    pass
            elif (estado ==1): #ID 
                if(x.isalpha()):
                    aux +=x
                    columna+=1
                else:
                    t = Token(PR.ID,aux,fila,columna)
                    self.tokens.append(t) 
                    estado = 0
                    i -=1
                    aux = ''
                    
            elif(estado ==2): #Cualquier cadena "cadena"
                if(x!='"'):
                    aux +=x
                    columna+=1
                else:
                    aux+=x
                    t = Token(PR.CADENA,aux,fila,columna)
                    self.tokens.append(t) 
                    estado = 0
                    aux = ''
            elif(estado==3): #Cualquier numero
                if(x.isdigit()):
                    aux +=x
                    columna+=1
                else:
                    t = Token(PR.NUM,aux,fila,columna)
                    self.tokens.append(t) 
                    estado = 0
                    i-=1
                    aux = ''
            elif(estado==4): #Comentario
                if(x=='\n'):
                    aux +=x
                    columna+=1
                else:
                    t = Token(PR.COMENTARIO,aux,fila,columna)
                    self.tokens.append(t)
                    estado = 0
                    i-=1
                    columna-=1
                    aux = ''
            elif(estado==5): #multi
                if(x=="'"):
                    aux +=x
                    columna+=1
                else:
                    t = Token(PR.MULTI,aux,fila,columna)
                    self.tokens.append(t)
                    estado = 0
                    i-=1
                    columna-=1
                    aux = ''
            i+=1

                
