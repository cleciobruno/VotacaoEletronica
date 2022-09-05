from tkinter import *
import forms


def cadastrar():
    janela2 = Tk()
    janela2.title("Cadastrar Candidato")
    janela2.geometry("490x560+540+153")
    janela2.iconbitmap(default="imagens/cat.ico")
    janela2.resizable(width=1, height=1)

    def sindico():
        janela2.destroy()
        forms.form_sindico()

    # imagens cadastrar
    cad = PhotoImage(file="imagens/cadastrar.png")
    cad_sindico = PhotoImage(file="imagens/cad_sindico.png")
    cad_secretario = PhotoImage(file="imagens/cad_secretario.png")

    # fundo cadastrar
    fundo2 = Label(janela2, image=cad)
    fundo2.pack()
    

    # botoes
    but_sindico = Button(janela2, bd=0, bg="#00c4cc", image=cad_sindico, command=sindico)
    but_sindico.place(width=190, height=56, x=150, y=228)

    but_secretario = Button(janela2, bd=0, bg="#00c4cc", image=cad_secretario)
    but_secretario.place(width=190, height=56, x=150, y=330)


    janela2.mainloop()
