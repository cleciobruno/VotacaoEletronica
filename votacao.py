from tkinter import *
import cadastrar

if __name__ == "__main__":

    # janela principal
    janela = Tk()
    janela.title("Votação Eletrônica")
    janela.geometry("490x560+540+153")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=1, height=1)

    # acao
    def cadastro():
        janela.destroy()
        cadastrar.cadastrar()

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
    but_visualizar = Button(janela, bd=0, bg="#00c4cc", image=botao_visualizar)
    but_visualizar.place(width=190, height=56, x=150, y=227)
    but_atualizar = Button(janela, bd=0, bg="#00c4cc", image=botao_atualizar)
    but_atualizar.place(width=190, height=56, x=150, y=320)
    but_remover = Button(janela, bd=0, bg="#00c4cc", image=botao_remover)
    but_remover.place(width=190, height=56, x=150, y=413)

    janela.mainloop()