# importar do tkinter

from tkinter import *
from tkinter import ttk
import tkinter as tk
import backend

# cores

cor1 = "#1f1d1d"   # preto
cor2 = "#ebf4fa"   # branco
cor3 = "#041c40"   # azul
cor4 = "#c1cfd9"   # cinza claro
cor5 = "#ff8585"   # salmão


# Janela

janela = Tk()
janela.title("Calculadora")
janela.geometry("390x435")
janela.config(bg=cor1)

# repartição

frame_tela = Frame(janela, width=390, height=90, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_teclado = Frame(janela, width=390, height=380,
                      bg=cor1)
frame_teclado.grid(row=2, column=0)


todos_valores = ""


# label

valor_texto = StringVar()

app_label = Label(frame_tela, width=30, height=4, padx=15, relief=FLAT, anchor="e",
                  justify=RIGHT, font=("Ivy 15 bold"), bg=cor2, fg=cor3, textvariable=valor_texto)
app_label.place(x=0, y=0)


# funções

def entrar_valores(bola):

    global todos_valores

    todos_valores = todos_valores + str(bola)

    if todos_valores.endswith("6+9"):
        valor_texto.set("esperando '=' ...")

    else:
        valor_texto.set(todos_valores)

    valor_texto.set(todos_valores)


# expressões

def calcular():

    global todos_valores

    if todos_valores == "6+9":
        valor_texto.set("eu amo peitos")

    else:
        try:
            resultado = backend.calculadora(todos_valores)
            valor_texto.set(str(resultado))

        except Exception as e:
            valor_texto.set("Errou bobinho")
    todos_valores = ""


def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


# botoes
b_1 = Button(frame_teclado, command=limpar_tela, text="C", width=9, height=3, bg=cor5, fg=cor3,
             font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_teclado, command=lambda: entrar_valores("sqrt"), text="√", width=9, height=3, bg=cor5, fg=cor2,
             font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=98, y=0)

b_3 = Button(frame_teclado, command=lambda: entrar_valores("**"), text="^", width=9, height=3, bg=cor5, fg=cor2,
             font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=196, y=0)

b_4 = Button(frame_teclado, command=lambda: entrar_valores("%"), text="%", width=9, height=3, bg=cor5, fg=cor2,
             font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=294, y=0)       # coluna colorida

b_5 = Button(frame_teclado, command=lambda: entrar_valores("7"), text="7", width=9, height=3, bg=cor4,
             font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=0, y=69)

b_6 = Button(frame_teclado, command=lambda: entrar_valores("8"), text="8", width=9, height=3, bg=cor4,
             font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=98, y=69)

b_7 = Button(frame_teclado, command=lambda: entrar_valores("9"), text="9", width=9, height=3, bg=cor4,
             font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=196, y=69)

b_8 = Button(frame_teclado, command=lambda: entrar_valores("*"), text="x", width=9, height=3, bg=cor5, fg=cor2,
             font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=294, y=69)       # coluna colorida

b_9 = Button(frame_teclado, command=lambda: entrar_valores("4"), text="4", width=9, height=3, bg=cor4,
             font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=0, y=138)

b_10 = Button(frame_teclado, command=lambda: entrar_valores("5"), text="5", width=9, height=3, bg=cor4,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=98, y=138)

b_11 = Button(frame_teclado, command=lambda: entrar_valores("6"), text="6", width=9, height=3, bg=cor4,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=196, y=138)

b_12 = Button(frame_teclado, command=lambda: entrar_valores("/"), text="÷", width=9, height=3, bg=cor5, fg=cor2,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=294, y=138)       # coluna colorida

b_13 = Button(frame_teclado, command=lambda: entrar_valores("1"), text="1", width=9, height=3, bg=cor4,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=0, y=207)

b_14 = Button(frame_teclado, command=lambda: entrar_valores("2"), text="2", width=9, height=3, bg=cor4,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=98, y=207)

b_15 = Button(frame_teclado, command=lambda: entrar_valores("3"), text="3", width=9, height=3, bg=cor4,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=196, y=207)

b_16 = Button(frame_teclado, command=lambda: entrar_valores("+"), text="+", width=9, height=3, bg=cor5, fg=cor2,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=294, y=207)       # coluna colorida

b_17 = Button(frame_teclado, command=lambda: entrar_valores("0"), text="0", width=9, height=3, bg=cor4,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=0, y=276)

b_18 = Button(frame_teclado, command=lambda: entrar_valores("."), text=".", width=9, height=3, bg=cor4,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=98, y=276)

b_19 = Button(frame_teclado, command=lambda: entrar_valores("-"), text="-", width=9, height=3, bg=cor5, fg=cor2,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_19.place(x=294, y=276)  # 294

b_20 = Button(frame_teclado, command=calcular, text="=", width=9, height=3, bg=cor4,
              font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b_20.place(x=196, y=276)  # 196    # coluna colorida


janela.mainloop()

