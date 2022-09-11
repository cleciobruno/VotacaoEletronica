from tkinter import *
import lista

# função principal
def atu_cand(pessoa):
    janela = Tk()
    janela.title("Cadastrar Síndico")
    janela.geometry("490x560+540+153")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=False, height=False)

    # função voltar
    def voltar():
        janela.destroy()
        lista.mostrar()

    # função atualiza
    def atualiza():
        
        # declarando as mudanças
        cand = {pessoa[1][0]:candidato.get()}
        nom = {pessoa[1][1]:nome.get()}
        prop = {pessoa[1][2]:proposta.get("1.0", "end-1c")}
        apar = {pessoa[1][3]:ap.get()}
        chap = {pessoa[1][4]:num.get()}

        # executando o update no dataframe
        lista.df["Candidato"] = lista.df["Candidato"].map(cand)
        lista.df["Nome"] = lista.df["Nome"].map(nom)
        lista.df["Proposta"] = lista.df["Proposta"].map(prop)
        lista.df["Apartamento"] = lista.df["Apartamento"].map(apar)
        lista.df["Número da Chapa"] = lista.df["Número da Chapa"].map(chap)
        
        # fechando janela e redirecionando para lista
        janela.destroy()
        lista.mostrar()

    # imagens cadastrar
    cad = PhotoImage(file="imagens/form_att.png")
    but_att = PhotoImage(file="imagens/but_att.png")
    but_voltar = PhotoImage(file="imagens/voltar.png")

    # fundo cadastrar
    fundo = Label(janela, image=cad)
    fundo.pack()

    # caixas de texto e botões
    candidato = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                    highlightbackground="black", highlightthickness=2)
    candidato.place(width=193, height=52, x=32, y=127)
    candidato.insert("0",pessoa[1][0])
    nome = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                    highlightbackground="black", highlightthickness=2)
    nome.place(width=193, height=52, x=265, y=127)
    nome.insert("0",pessoa[1][1])
    proposta = Text(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                    highlightbackground="black", highlightthickness=2, wrap=WORD)
    proposta.place(width=392, height=138, x=49, y=228)
    proposta.insert("1.0",pessoa[1][2])
    ap = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                highlightbackground="black", highlightthickness=2)
    ap.place(width=117, height=52, x=63, y=414)
    ap.insert("0",pessoa[1][3])
    num = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                highlightbackground="black", highlightthickness=2)
    num.place(width=117, height=52, x=309, y=414)
    num.insert("0",pessoa[1][4])
    but_at = Button(janela, bd=0, bg="#00c4cc",
                        image=but_att, command=atualiza)
    but_at.place(width=160, height=52, x=165, y=496)
    volta = Button(janela, bd=0, bg="#00c4cc",
                    image=but_voltar, command=voltar)
    volta.place(width=40, height=40, x=7, y=514)
    
    # loop da janela
    janela.mainloop()