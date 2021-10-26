from Reporte import Reporte
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as MessageBox
import numpy as np
from Parser import Parser
from tkinter import Menu, filedialog,Tk

import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from Reservadas import PR

from Reporte import Reporte
from Clave import Clave
p = Parser()
r = Reporte()
claves = []




def abrir():
    
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo LFP",
        initialdir = "./",
        filetypes = (
            ("archivos LFP", "*.lfp"),
            ("todos los archivos",  "*.*")
        )
    )
    if archivo is None:
        MessageBox.showerror(title="Carga",message="No se seleccionó ningun archivo")
        
        return None
    else:
        texto = archivo.read()
        archivo.close()
        MessageBox.showinfo(title="Lectura",message="Exito") # título, mensaje
        return texto

def prueba ():
    txt = abrir()
    if txt is not None:
        dato = txt
        
        p.obtenerData(dato)  
    else:
        MessageBox.showerror(title="Error",message="Error de lectura")
        

def llenarClave(lista):
        titulo = ''
        
        i = 0
        end = len(lista)
        while i< end:
            token = lista[i]
            if token.lexema == PR.CADENA :
                titulo = token.lexema
            

            
            elif(titulo!='' ):
                    claves.append(Clave(titulo))
                    titulo = ''
                    
            i+=1


def cargarArchivos():
    prueba()
    
    r.reporteToken(p.tokens)
    i = 0
    size = len(p.tokens)
    while(i<size):
        x = p.tokens[i]
        print(x.lexema)
        i+=1
                

def escribir():
    nombrearch=fd.askopenfilename(initialdir = "./",title = "Seleccione archivo",filetypes = (("LFP files","*.lfp"),("todos los archivos","*.*")))
    if nombrearch!='':
        archi1=open(nombrearch, "r", encoding="utf-8")
        contenido=archi1.read()
        archi1.close()
        scrolledtext1.delete("1.0", tk.END) 
        scrolledtext1.insert("1.0", contenido) 

def guardar():
    nombrearch=fd.asksaveasfilename(initialdir = "./",title = "Guardar como",filetypes = (("LFP files","*.lfp"),("todos los archivos","*.*")))
    if nombrearch!='':
        archi1=open(nombrearch, "w", encoding="utf-8")
        archi1.write(scrolledtext1.get("1.0", tk.END))
        archi1.close()
        mb.showinfo("Información", "Los datos fueron guardados en el archivo.")  
    else:
        MessageBox.showerror(title="Error",message="Escriba un nombre")
    

def generarTokens():
    r.reporteToken(p.tokens)

def generarErrores():
    r.reporteErrores(p.lista_errores)
    
    
def generar():
    pass
    

def imagen():
    titulo =askopenfilename(filetypes = (("Imagenes", "*.jpg"), ("All files", "*")))
    img = Image.open(titulo)
    new_img = img.resize((500,300))
    render = ImageTk.PhotoImage(new_img)
    ing1 = Label(ventana, image=render)
    ing1.image = render
    ing1.place(x=10,y=30)

def salirAplicacion():
    salir = messagebox.askquestion("Salir", "¿Desea salir?")
    if salir =="yes":
        ventana.quit()
                    

    

if __name__ == "__main__":
    
    ventana = Tk()
    ventana.geometry("1100x640+150+10")
    ventana.title("Menu")
    ventana.iconbitmap("img\python_94570.ico")
    fondo = PhotoImage(file="img\Font.gif")
    fondo1= Label(ventana, image=fondo).place(x=0,y=0,relwidth=1,relheight=1)

    barraMenu=Menu(ventana)
    cargarArchivo=Menu(barraMenu,tearoff=0)
    modificarArchivo=Menu(barraMenu,tearoff=0)
    verReporte=Menu(barraMenu,tearoff=0)
    verImagen=Menu(barraMenu,tearoff=0)
    salir = Menu(barraMenu,tearoff=0)

    cargarArchivo.add_command(label="Abrir",command=cargarArchivos)

    modificarArchivo.add_command(label="Modificar", command=escribir)
    modificarArchivo.add_separator()
    modificarArchivo.add_command(label="Guardar", command=guardar)

    verReporte.add_command(label="Tokens",command=generarTokens)
    verReporte.add_separator()
    verReporte.add_command(label="Errores", command=generarErrores)

    verImagen.add_command(label="Ver Imagen", command=imagen)
    

    salir.add_command(label="Salir",command=salirAplicacion)



    barraMenu.add_cascade(label="Archivo",menu=cargarArchivo)
    barraMenu.add_cascade(label="Modificar",menu=modificarArchivo)
    barraMenu.add_cascade(label="Reporte",menu=verReporte)
    barraMenu.add_cascade(label="Ver",menu=verImagen)
    barraMenu.add_cascade(label="Salir",menu=salir)


    ventana.config(menu=barraMenu)

    scrolledtext1=st.ScrolledText(ventana, width=80, height=20)
    scrolledtext1.grid(column=0,row=0, padx=10, pady=10)
    scrolledtext2=st.ScrolledText(ventana, width=47, height=20)
    scrolledtext2.grid(column=1,row=0, padx=10, pady=10)
    scrolledtext2.insert(1.0,"Prueba")
    scrolledtext2.configure(state='disabled')

    ventana.mainloop()
  
    