from Token import Token
from Reservadas import PR
from Error import Error

class Parser:
    def __init__(self):
        self.tokens = []
        self.lista_errores = []

        


    def obtenerData(self,data): 
        
        estado = 0 
        aux = ''
        fila = 1
        columna =0
        i=0
        reset=0
        while i in range(len(data)):
            x = data[i]
            if(estado==0):
                
                if(x == '(' or x == ')' or x == '=' or x == ';' or x == ',' or x== '{'  or x == '}'  or x == '['  or x == ']' ): #Ignorar
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
                elif(x.isdigit()):
                    aux +=x
                    estado = 3
                elif(x == '"'):
                    aux+=x
                    estado = 2
                elif(x == '#'):
                    estado = 4
                    aux+=x
                elif(x == "'"):
                    #global reset 
                    reset = i
                    try:
                        if(data[i+1] == "'" and data[i+2] == "'"):
                            estado = 5
                            aux+="'''"
                            i+=2
                        else:
                            x=0
                            #Error
                    except:
                        x=0
                        #Error
                else:
                    #aux+=x
                    #err = Error(aux,fila,columna)
                    #self.lista_errores(err)
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
                    if(x=='.'):
                        estado = 7
                        aux+=x
                        columna+=1
                    else:
                        t = Token(PR.NUM,aux,fila,columna)
                        self.tokens.append(t) 
                        estado = 0
                        i-=1
                        aux = ''
            elif(estado==4): #comentario
                if(x!='\n'):
                    aux +=x
                    columna+=1
                else:
                    aux+=x
                    t = Token(PR.COMENTARIO,aux,fila,columna)
                    self.tokens.append(t)
                    estado = 0
                    i-=1
                    columna-=1
                    aux = ''
            elif(estado==5): #multi
                try:
                    if(data[i+1]=="'" and data[i+2] == "'" and data[i+3] == "'"):
                        aux+=x
                        aux+="'''"
                        t = Token(PR.MULTI,aux,fila,columna)
                        self.tokens.append(t)
                        estado = 0
                        i+=3
                        columna+=3
                        aux = ''
                    else:
                        aux +=x
                        columna+=1
                except:
                    #global reset
                    i = reset
                    x = data[i]
                    #Error  
                    x=0
            elif(estado==7): #Cualquier numero decimal
                if(x.isdigit()):
                    aux +=x
                    columna+=1
                else:
                    t = Token(PR.DECI,aux,fila,columna)
                    self.tokens.append(t) 
                    estado = 0
                    i-=1
                    aux = ''
            i+=1

                
