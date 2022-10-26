from tkinter import *
import lista
import os
import tela_votacao

# função principal


def janela():
    os.system("cls")

    # janela principal
    janela = Tk()
    janela.title("Votação Eletrônica")
    janela.geometry("490x560+540+153")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=False, height=False)

    # redireciona para lista
    def visualizar():
        janela.destroy()
        lista.mostrar()

    # redireciona para a votação
    def iniciar():
        janela.destroy()
        tela_votacao.votar()

    # upload das imagens
    votacao = PhotoImage(file="imagens/inicial.png")
    but_crud = PhotoImage(file="imagens/crud.png")
    but_votacaoe = PhotoImage(file="imagens/votacao_enable.png")

    # fundo
    fundo = Label(janela, image=votacao)
    fundo.pack()

    # puxar a quantidade de síndicos e secretários
    sindi = lista.df.loc[lista.df["Candidato"] == "Síndico"]
    secre = lista.df.loc[lista.df["Candidato"] == "Secretário"]

    # verificar se há a quantidade certa para liberar a votação
    if len(sindi) >= 2 and len(secre) >= 3:
        cond = "normal"
    else:
        cond = "disabled"

    # botões
    votac = Button(janela, bd=0, bg="#00c4cc", state=cond,
                   image=but_votacaoe, command=iniciar)
    votac.place(width=217, height=63, x=136, y=402)
    crud = Button(janela, bd=0, bg="#00c4cc",
                  image=but_crud, command=visualizar)
    crud.place(width=217, height=63, x=136, y=280)

    # loop da janela
    janela.mainloop()


if __name__ == "__main__":
    janela()
