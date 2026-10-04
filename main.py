import tkinter as tk
from Calculadora import Calculadora

def sumar():
    n1 = int(caja1.get())
    n2 = int(caja2.get())

    c = Calculadora(n1, n2)

   # res = n1 + n2
    etiqueta.config(text=f"Resultado: {c.sumar()}")


# CREAR LA VENTANA PRINCIPAL DEL PROGRAMA
ventana = tk.Tk()

ventana.title("Calculadora")
ventana.geometry("300x250")


# Texto que se muestra en pantalla con sus respectivas "cajas" que reciben un valor
text1 = tk.Label(ventana, text="Numero 1")
text1.pack()

caja1 = tk.Entry(ventana)
caja1.pack()


text2 = tk.Label(ventana, text="Numero 2")
text2.pack()

caja2 = tk.Entry(ventana)
caja2.pack()


etiqueta = tk.Label(ventana, text="Resultado: ")
etiqueta.pack()

buttonSumar = tk.Button(ventana, text="Sumar", command=sumar)
buttonSumar.pack()



ventana.mainloop()