

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as MessageBox
import numpy as np

from tkinter import Menu, filedialog,Tk


class Abrir:

    def carga(self):
        
        Tk().withdraw()
        archivo = filedialog.askopenfile(
            title = "Seleccionar un archivo FLP",
            initialdir = "./",
            filetypes = (
                ("archivos FLP", "*.lfp"),
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


    def prueba (self):
        txt = self.carga()
        if txt is not None:
            dato = txt
            #p.obtenerData(dato)  
        else:
            MessageBox.showerror(title="Error",message="Error de lectura")