from tkinter import *
import forms
import lista

# função principal


def cadastrar():

    # janela
    janela = Tk()
    janela.title("Cadastrar Candidato")
    janela.geometry("490x560+540+153")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=False, height=False)

    # função voltar
    def voltar():
        janela.destroy()
        lista.mostrar()

    # redireciona para formulário do síndico
    def sindico():
        janela.destroy()
        forms.form_sindico()

    # redireciona para formulário do secretário
    def secretario():
        janela.destroy()
        forms.form_secretario()

    # imagens cadastrar
    cad = PhotoImage(file="imagens/cadastrar.png")
    cad_sindico = PhotoImage(file="imagens/cad_sindico.png")
    cad_secretario = PhotoImage(file="imagens/cad_secretario.png")
    but_voltar = PhotoImage(file="imagens/voltar.png")

    # fundo cadastrar
    fundo2 = Label(janela, image=cad)
    fundo2.pack()

    # botoes
    but_sindico = Button(janela, bd=0, bg="#00c4cc",
                         image=cad_sindico, command=sindico)
    but_sindico.place(width=190, height=56, x=150, y=228)
    but_secretario = Button(janela, bd=0, bg="#00c4cc",
                            image=cad_secretario, command=secretario)
    but_secretario.place(width=190, height=56, x=150, y=330)
    volta = Button(janela, bd=0, bg="#00c4cc",
                   image=but_voltar, command=voltar)
    volta.place(width=40, height=40, x=7, y=514)

    # loop da janela
    janela.mainloop()
