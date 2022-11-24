import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import numpy as np


N = 100

    
def operacion():   
    
    def func_lineal():
    
        def funcion_lineal(m, b, x):
            return m*x + b
        
        m.set(5)
        b.set(4)
        m1 = int(m.get())
        b1 = int(b.get())

        
        
        x = np.linspace(-10,10,num=N)
        y = funcion_lineal(m1,b1,x)
        # Crear la figura y los ejes
        fig, ax = plt.subplots()
        # Dibujar puntos
        ax.scatter(x , y)
        # Guardar el gráfico en formato png
        plt.savefig('diagrama-dispersion.png')
        # Mostrar el gráfico
        plt.show()
        
    ventana_secundaria = Tk()
    ventana_secundaria.title("Convertidor")
    ventana_secundaria.geometry("400x450")
    ventana_secundaria.resizable(0,0)
    ventana_secundaria.config(bg="snow")

    
    
    m = StringVar()
    b = StringVar()

    frame_entrada = Frame(ventana_secundaria)
    frame_entrada.config(bg = "light grey", width = 380 , height = 280)
    frame_entrada.place(x = 10, y = 10)



    titulo = Label(frame_entrada, text = "Graficador de función Lineal")
    titulo.config(bg = "light grey", fg = "gray21", font = ("Rubik",18))
    titulo.place(x = 30, y = 20)

    titulo2 = Label(frame_entrada, text = " y = mx + b ")
    titulo2.config(bg = "light grey", fg = "gray21", font = ("Rubik",14))
    titulo2.place(x = 140, y = 80)
    
    titulo = Label(frame_entrada, text = "Digita la pendiente 'm':")
    titulo.config(bg = "light grey", fg = "gray21", font = ("Rubik",10))
    titulo.place(x=40, y=150)
    
    # Entry para la pendiente "m"

    entry_s = Entry(frame_entrada, textvariable= m)
    entry_s.config(font=("Rubik",20), justify=LEFT, fg="gray21")
    entry_s.focus_set()
    entry_s.place(x=200, y=150, width=115, height=30)
    

    
    # Entry para el corte en el eje y "b"

    entry_b = Entry(frame_entrada, textvariable= b)
    entry_b.config(font=("Rubik",20), justify=LEFT, fg="gray21")
    entry_b.place(x=200, y=190, width=115, height=30)
    



    bt_convertir = Button(frame_entrada, text="Ejecutar",bg="slategray4", fg="light grey", command= func_lineal)
    bt_convertir.place(x=125, y=240, width=120, height=30)
    
    

    ventana_secundaria.mainloop