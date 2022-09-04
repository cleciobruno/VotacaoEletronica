from tkinter import *
import time


def cadastrar():
    time.sleep(0.2)
    janela2 = Tk()
    janela2.title("Cadastrar Candidato")
    janela2.geometry("490x560+540+153")
    janela2.iconbitmap(default="imagens/cat.ico")
    janela2.resizable(width=1, height=1)

    # imagens cadastrar
    cad = PhotoImage(file="imagens/cadastrar.png")
    cad_sindico = PhotoImage(file="imagens/cad_sindico.png")
    cad_secretario = PhotoImage(file="imagens/cad_secretario.png")

    # fundo cadastrar
    fundo2 = Label(janela2, image=cad)
    fundo2.pack()
    

    # botoes
    but_sindico = Button(janela2, bd=0, bg="#00c4cc", image=cad_sindico)
    but_sindico.place(width=190, height=56, x=150, y=413)
    # but_secretario = Button(janela2, bd=0, bg="#00c4cc", image=cad_secretario)
    # but_secretario.place(width=190, height=56, x=150, y=343)



    janela2.mainloop()

cadastrar()
