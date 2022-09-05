from tkinter import *

def form_sindico():
    janela3 = Tk()
    janela3.title("Cadastrar Síndico")
    janela3.geometry("490x560+540+153")
    janela3.iconbitmap(default="imagens/cat.ico")
    janela3.resizable(width=1, height=1)

    # imagens cadastrar
    cad1 = PhotoImage(file="imagens/forms_sindico.png")
    but_cadastro = PhotoImage(file="imagens/but_cadastro.png")

    # fundo cadastrar
    fundo2 = Label(janela3, image=cad1)
    fundo2.pack()
    
    nome = Entry(janela3, bd=0, font=("Calibri",15),highlightcolor="black", highlightbackground="black", highlightthickness=2)
    nome.place(width=392, height=44, x= 49, y=201)

    proposta = Text(janela3, bd=0, font=("Calibri",15),highlightcolor="black", highlightbackground="black", highlightthickness=2, wrap=WORD)
    proposta.place(width=392, height=93, x= 49, y=287)

    ap = Entry(janela3, bd=0, font=("Calibri",15),highlightcolor="black", highlightbackground="black", highlightthickness=2)
    ap.place(width=147, height=44, x= 49, y=424)

    num = Entry(janela3, bd=0, font=("Calibri",15),highlightcolor="black", highlightbackground="black", highlightthickness=2)
    num.place(width=147, height=44, x= 294, y=424)

    but_secretario = Button(janela3, bd=0, bg="#00c4cc", image=but_cadastro)
    but_secretario.place(width=190, height=56, x=150, y=489)

    janela3.mainloop()
