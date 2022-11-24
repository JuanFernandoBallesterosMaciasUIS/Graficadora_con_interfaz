import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import numpy as np


N = 100

    
def operacion():   
    
    def func_lineal():

        def funcion_lineal(m, b, x):
            return m*x + b
        
        
        x = np.linspace(-10,10,num=N)
        y = funcion_lineal(2,3,x)
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


    x = StringVar()

    frame_entrada = Frame(ventana_secundaria)
    frame_entrada.config(bg = "light grey", width = 380 , height = 240)
    frame_entrada.place(x = 10, y = 10)



    titulo = Label(frame_entrada, text = "Graficador de función Lineal")
    titulo.config(bg = "light grey", fg = "gray21", font = ("Rubik",18))
    titulo.place(x = 70, y = 20)

    titulo2 = Label(frame_entrada, text = "Eliga una opción:")
    titulo2.config(bg = "light grey", fg = "gray21", font = ("Rubik",14))
    titulo2.place(x = 50, y = 80)
    
    bt_convertir = Button(frame_entrada, text="Función Lineal",bg="slategray4", fg="light grey", command= func_lineal)
    bt_convertir.place(x=50, y=120, width=120, height=30)

    ventana_secundaria.mainloop