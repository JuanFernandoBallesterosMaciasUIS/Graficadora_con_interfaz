from tkinter import *
from tkinter import messagebox
import funcion_lineal


    

ventana_principal = Tk()
ventana_principal.title("Convertidor")
ventana_principal.geometry("400x450")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="snow")





frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "light grey", width = 380 , height = 240)
frame_entrada.place(x = 10, y = 10)



titulo = Label(frame_entrada, text = "Graficador de funciones")
titulo.config(bg = "light grey", fg = "gray21", font = ("Rubik",18))
titulo.place(x = 70, y = 20)

titulo2 = Label(frame_entrada, text = "Eliga una opción:")
titulo2.config(bg = "light grey", fg = "gray21", font = ("Rubik",14))
titulo2.place(x = 50, y = 80)




# Funciones
 
bt_convertir = Button(frame_entrada, text="Función Lineal",bg="slategray4", fg="light grey", command= funcion_lineal.operacion)
bt_convertir.place(x=50, y=120, width=120, height=30)

bt_borrar = Button(frame_entrada, text="Función Cuadratica",bg="slategray4", fg="light grey")
bt_borrar.place(x=50, y=155, width=120, height=30)

bt_salir = Button(frame_entrada, text="Función Cubica",bg="slategray4", fg="light grey")
bt_salir.place(x=50, y=190, width=120, height=30)





ventana_principal.mainloop()