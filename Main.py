
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as MessageBox
from tkinter import Menu, filedialog,Tk

from Carga.Abrir import Abrir
 
a = Abrir()



def cargarArchivos():
    a.prueba()
    #llenarFigura(p.tokens)
    

def generarTokens():
    print("Tokens")
    #r.reporteToken(p.tokens)

def generarErrores():
    print("Errores")
    #r.reporteErrores(p.lista_errores)
    
    
def generar():
    for i in range(len(figuras)):
        figuras[i].generarImagen("MIRRORN") 
        figuras[i].generarImagen("MIRRORX")
        figuras[i].generarImagen("MIRRORY")
        figuras[i].generarImagen("MIRRORD")
    MessageBox.showinfo(title="Generar",message="Exito")
    

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
    ventana.geometry("450x675+300+10")
    ventana.title("Menu")
    ventana.iconbitmap("img\python_94570.ico")
    fondo = PhotoImage(file="img\Pin-en-Movimiento.gif")
    fondo1= Label(ventana, image=fondo).place(x=0,y=0,relwidth=1,relheight=1)

    barraMenu=Menu(ventana)
    cargarArchivo=Menu(barraMenu,tearoff=0)
    generarImagen=Menu(barraMenu,tearoff=0)
    verReporte=Menu(barraMenu,tearoff=0)
    verImagen=Menu(barraMenu,tearoff=0)
    salir = Menu(barraMenu,tearoff=0)

    cargarArchivo.add_command(label="Abrir",command=cargarArchivos)

    generarImagen.add_command(label="Generar imagenes", command=generar)

    verReporte.add_command(label="Tokens",command=generarTokens)
    verReporte.add_separator()
    verReporte.add_command(label="Errores", command=generarErrores)

    verImagen.add_command(label="Ver Imagen", command=imagen)
    

    salir.add_command(label="Salir",command=salirAplicacion)



    barraMenu.add_cascade(label="Archivo",menu=cargarArchivo)
    barraMenu.add_cascade(label="Generar",menu=generarImagen)
    barraMenu.add_cascade(label="Reporte",menu=verReporte)
    barraMenu.add_cascade(label="Ver",menu=verImagen)
    barraMenu.add_cascade(label="Salir",menu=salir)


    ventana.config(menu=barraMenu)
    ventana.mainloop()
  
    