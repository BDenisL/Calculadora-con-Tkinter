import tkinter as tk
from Calculadora import Calculadora

def sumar():
    n1 = int(value_x_box.get())
    n2 = int(value_y_box.get())

    c = Calculadora(n1, n2)

    lab.config(text=f"Resultado: {c.sumar()}")

def restar():
    n1 = int(value_x_box.get())
    n2 = int(value_y_box.get())

    c = Calculadora(n1, n2)

    lab.config(text=f"Resultado: {c.restar()}")

def mult():
    n1 = int(value_x_box.get())
    n2 = int(value_y_box.get())

    c = Calculadora(n1, n2)

    lab.config(text=f"Resultado: {c.mult()}")

def div():
    n1 = int(value_x_box.get())
    n2 = int(value_y_box.get())

    c = Calculadora(n1, n2)

    lab.config(text=f"Resultado: {c.div()}")



ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x250")

value_x_text = tk.Label(ventana, text="Numero 1")
value_x_text.pack()

value_x_box = tk.Entry(ventana)
value_x_box.pack()

value_y_text = tk.Label(ventana, text="Numero 2")
value_y_text.pack()

value_y_box = tk.Entry(ventana)
value_y_box.pack()

lab = tk.Label(ventana, text="Resultado: ")
lab.pack()


buttonSuma = tk.Button(ventana, text="Sumar", command=sumar)
buttonSuma.pack()

buttonRest = tk.Button(ventana, text="Restar", command=restar)
buttonRest.pack()

buttonMult = tk.Button(ventana, text="Multiplicar", command=mult)
buttonMult.pack()

buttonDiv = tk.Button(ventana, text="Dividir", command=div)
buttonDiv.pack()


ventana.mainloop()

