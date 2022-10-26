from tkinter import *
import tela_votacao
import contabilizar


def janela():

    # janela principal
    janela = Tk()
    janela.title("Votação Eletrônica")
    janela.geometry("490x560+540+153")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=False, height=False)

    # upload das imagens
    telaf = PhotoImage(file="imagens2/telaF.png")
    finalizar = PhotoImage(file="imagens2/finalizar.png")
    vota = PhotoImage(file="imagens2/vota.png")

    def voltar():
        janela.destroy()
        tela_votacao.votar()

    def contabilizacao():
        janela.destroy()
        contabilizar.janela()

    # fundo
    fundo = Label(janela, image=telaf)
    fundo.pack()

    # botões
    votar = Button(janela, bd=0, bg="#00c4cc", state='normal',
                   image=vota, command=voltar)
    votar.place(width=244, height=56, x=123, y=256)
    fina = Button(janela, bd=0, bg="#00c4cc",
                  image=finalizar, command=contabilizacao)
    fina.place(width=244, height=56, x=123, y=415)

    # loop da janela
    janela.mainloop()
