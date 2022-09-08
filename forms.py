from tkinter import *
import candidatos
import cadastrar
import votacao

# formulário do síndico
def form_sindico():
    janela = Tk()
    janela.title("Cadastrar Síndico")
    janela.geometry("490x560+540+153")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=False, height=False)

    # função voltar
    def voltar():
        janela.destroy()
        cadastrar.cadastrar()

    # função cadastrar síndico
    def cadastro_sindico():
        p = candidatos.Sindico(nome.get(), proposta.get(
            "1.0", "end-1c"), ap.get(), num.get())
        candidatos.Sindico.cad_sindico(p)
        janela.destroy()
        votacao.janela()

    # imagens cadastrar
    cad = PhotoImage(file="imagens/forms_sindico.png")
    but_cadastro = PhotoImage(file="imagens/but_cadastro.png")
    but_voltar = PhotoImage(file="imagens/voltar.png")

    # fundo cadastrar
    fundo = Label(janela, image=cad)
    fundo.pack()

    # caixas de texto e botçoes
    nome = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                 highlightbackground="black", highlightthickness=2)
    nome.place(width=392, height=44, x=49, y=201)

    proposta = Text(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                    highlightbackground="black", highlightthickness=2, wrap=WORD)
    proposta.place(width=392, height=93, x=49, y=287)

    ap = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
               highlightbackground="black", highlightthickness=2)
    ap.place(width=147, height=44, x=49, y=424)

    num = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                highlightbackground="black", highlightthickness=2)
    num.place(width=147, height=44, x=294, y=424)

    but_cad = Button(janela, bd=0, bg="#00c4cc",
                     image=but_cadastro, command=cadastro_sindico)
    but_cad.place(width=190, height=56, x=150, y=489)

    volta = Button(janela, bd=0, bg="#00c4cc",
                   image=but_voltar, command=voltar)
    volta.place(width=40, height=40, x=7, y=514)

    janela.mainloop()

# formulário secretário
def form_secretario():
    janela = Tk()
    janela.title("Cadastrar Síndico")
    janela.geometry("490x560+540+153")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=False, height=False)

    # função voltar

    def voltar():
        janela.destroy()
        cadastrar.cadastrar()

    # função cadastrar secretário
    def cadastro_secretario():
        p = candidatos.Secretario(nome.get(), ap.get(), num.get())
        candidatos.Secretario.cad_secretario(p)
        janela.destroy()
        votacao.janela()

    # imagens cadastrar
    cad = PhotoImage(file="imagens/forms_secre.png")
    but_cadastro = PhotoImage(file="imagens/but_cadastro.png")
    but_voltar = PhotoImage(file="imagens/voltar.png")

    # fundo cadastrar
    fundo = Label(janela, image=cad)
    fundo.pack()

    # caixas de texto e botçoes
    nome = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                 highlightbackground="black", highlightthickness=2)
    nome.place(width=392, height=44, x=49, y=236)

    ap = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
               highlightbackground="black", highlightthickness=2)
    ap.place(width=147, height=44, x=49, y=390)

    num = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                highlightbackground="black", highlightthickness=2)
    num.place(width=147, height=44, x=294, y=390)

    but_cad = Button(janela, bd=0, bg="#00c4cc",
                     image=but_cadastro, command=cadastro_secretario)
    but_cad.place(width=190, height=56, x=150, y=472)

    volta = Button(janela, bd=0, bg="#00c4cc",
                   image=but_voltar, command=voltar)
    volta.place(width=40, height=40, x=7, y=514)

    janela.mainloop()
