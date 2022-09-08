from tkinter import *
import cadastrar
import lista
import os


def janela():
    os.system('cls')
    
    # janela principal
    janela = Tk()
    janela.title("Votação Eletrônica")
    janela.geometry("490x560+540+153")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=False, height=False)

    # redireciona para cadastro
    def cadastro():
        janela.destroy()
        cadastrar.cadastrar()

    # redireciona para lista
    def visualizar():
        janela.destroy()
        lista.mostrar()

    # upload das imagens
    votacao = PhotoImage(file="imagens/votacao.png")
    botao_cadastrar = PhotoImage(file="imagens/but_cadastrar.png")
    botao_visualizar = PhotoImage(file="imagens/but_visualizar.png")
    botao_atualizar = PhotoImage(file="imagens/but_atualizar.png")
    botao_remover = PhotoImage(file="imagens/but_remover.png")

    # fundo
    fundo = Label(janela, image=votacao)
    fundo.pack()

    # botões
    but_cadastrar = Button(janela, bd=0, bg="#00c4cc",
                           image=botao_cadastrar, command=cadastro)
    but_cadastrar.place(width=190, height=56, x=150, y=134)
    but_visualizar = Button(janela, bd=0, bg="#00c4cc",
                            image=botao_visualizar, command=visualizar)
    but_visualizar.place(width=190, height=56, x=150, y=227)
    but_atualizar = Button(janela, bd=0, bg="#00c4cc", image=botao_atualizar)
    but_atualizar.place(width=190, height=56, x=150, y=320)
    but_remover = Button(janela, bd=0, bg="#00c4cc", image=botao_remover)
    but_remover.place(width=190, height=56, x=150, y=413)

    janela.mainloop()


if __name__ == "__main__":
    janela()
