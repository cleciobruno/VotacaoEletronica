from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import lista
import votos
import tela_votacaoS
import tela_finalizacao

# função principal


def votar():
    janela = Tk()
    janela.title("Votação Eletrônica")
    janela.geometry("700x600+480+120")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=False, height=False)

    tela = PhotoImage(file="imagens2/telaV.png")
    confirma = PhotoImage(file="imagens2/confirma.png")
    corrige = PhotoImage(file="imagens2/corrige.png")
    branco = PhotoImage(file="imagens2/branco.png")
    secretarios = PhotoImage(file="imagens2/secretarios.png")
    but_voltar = PhotoImage(file="imagens2/voltar.png")
    lupa = PhotoImage(file="imagens2/lupa.png")
    b0 = PhotoImage(file="imagens2/0.png")
    b1 = PhotoImage(file="imagens2/1.png")
    b2 = PhotoImage(file="imagens2/2.png")
    b3 = PhotoImage(file="imagens2/3.png")
    b4 = PhotoImage(file="imagens2/4.png")
    b5 = PhotoImage(file="imagens2/5.png")
    b6 = PhotoImage(file="imagens2/6.png")
    b7 = PhotoImage(file="imagens2/7.png")
    b8 = PhotoImage(file="imagens2/8.png")
    b9 = PhotoImage(file="imagens2/9.png")

    fundo = Label(janela, image=tela)
    fundo.pack()

    x = []

    def cont(f):
        if len(x) != 3:
            x.append(f)
        bruno()

    def corrigindo():
        x.clear()
        bruno()

    def passar():
        janela.destroy()
        tela_votacaoS.votar()

    def retornar():
        janela.destroy()
        tela_finalizacao.janela()

    def votoBranco():
        votos.votar('Branco')
        passar()

    def confirmacao():
        g = x[0]+x[1]+x[2]
        secre = lista.df.loc[lista.df['Número da Chapa'] == g]
        if len(secre) > 0:
            num = lista.df['Nome'].loc[lista.df['Número da Chapa'] == g]
            votos.votar(num.iloc[0])
            passar()
        else:
            messagebox.showwarning("Erro", "Este candidato não existe")

    def candi():
        if len(x) == 3:
            g = x[0]+x[1]+x[2]
            br = lista.df.loc[lista.df["Número da Chapa"] == g]
            rb = lista.df.index[lista.df["Número da Chapa"] == g].tolist()
            if len(br) != 0:
                global clecio
                clecio = formar(br, rb)

    def pesquisar():
        nome = busca.get()
        br = lista.df.loc[lista.df["Nome"] == nome]
        rb = lista.df.index[lista.df["Nome"] == nome].tolist()
        if len(br) != 0:
            global clecio3
            clecio3 = formar(br, rb)
        else:
            messagebox.showwarning("Erro", "Este candidato não existe")

    def ler():
        global clecio2
        clecio2 = ver()

    # função para mostrar os secretários cadastrados
    def ver():
        frame1 = Frame(janela, borderwidth=2, relief="solid")
        frame1.place(width=488, height=189, x=105, y=411)

        tabela = ttk.Treeview(frame1)
        tabela["columns"] = ("candidato", "nome",
                             "apartamento", "num_chapa")
        tabela.column("#0", width=0,  stretch=NO)
        tabela.column("candidato", anchor="center", width=20)
        tabela.column("nome", anchor="center", width=15)
        tabela.column("apartamento", anchor="center", width=40)
        tabela.column("num_chapa", anchor="center", width=65)
        tabela.heading("#0", text="", anchor="center")
        tabela.heading("candidato", text="Candidato", anchor="center")
        tabela.heading("nome", text="Nome", anchor="center")
        tabela.heading("apartamento", text="Apartamento", anchor="center")
        tabela.heading("num_chapa", text="Número da Chapa", anchor="center")

        consul = lista.df.loc[lista.df['Candidato']
                              == 'Secretário'].reset_index(drop=True)
        for i in range(len(consul)):
            cand = consul.loc[i]
            tabela.insert(parent='', index='end', iid=i, text='', values=(
                cand.Candidato, cand.Nome, cand.Apartamento, cand["Número da Chapa"]))

        tabela.place(width=490, height=189)
        return frame1

    # função para mostrar o secretário digitado na urna
    def formar(br, rb):

        frame1 = Frame(janela, borderwidth=2, relief="solid")
        frame1.place(width=488, height=189, x=105, y=411)

        tabela = ttk.Treeview(frame1)
        tabela["columns"] = ("candidato", "nome", "proposta",
                             "apartamento", "num_chapa")
        tabela.column("#0", width=0,  stretch=NO)
        tabela.column("candidato", anchor="center", width=20)
        tabela.column("nome", anchor="center", width=15)
        tabela.column("proposta", anchor="center", width=100)
        tabela.column("apartamento", anchor="center", width=40)
        tabela.column("num_chapa", anchor="center", width=65)
        tabela.heading("#0", text="", anchor="center")
        tabela.heading("candidato", text="Candidato", anchor="center")
        tabela.heading("nome", text="Nome", anchor="center")
        tabela.heading("proposta", text="Proposta", anchor="center")
        tabela.heading("apartamento", text="Apartamento", anchor="center")
        tabela.heading("num_chapa", text="Número da Chapa", anchor="center")

        cand = br.loc[rb[0]]

        tabela.insert(parent='', index='end', iid=rb[0], text='', values=(
            cand.Candidato, cand.Nome, cand.Proposta, cand.Apartamento, cand["Número da Chapa"]))

        tabela.place(width=490, height=189)
        return frame1

    def bruno():
        if len(x) == 0:
            entra1 = Button(janela, bd=0, font=(
                "Calibri", 15), borderwidth=1, relief="solid", justify="center", text="")
            entra1.place(width=48, height=48, x=156, y=201)
            entra2 = Button(janela, bd=0, font=(
                "Calibri", 15), borderwidth=1, relief="solid", justify="center", text="")
            entra2.place(width=48, height=48, x=204, y=201)
            entra3 = Button(janela, bd=0, font=(
                "Calibri", 15), borderwidth=1, relief="solid", justify="center", text="")
            entra3.place(width=48, height=48, x=252, y=201)
            try:
                clecio.destroy()
            except:
                pass
            try:
                clecio2.destroy()
            except:
                pass
            try:
                clecio3.destroy()
            except:
                pass

        if len(x) == 1:
            entra1 = Button(janela, bd=0, font=(
                "Calibri", 15), borderwidth=1, relief="solid", justify="center", text=x[0])
            entra1.place(width=48, height=48, x=156, y=201)

        elif len(x) == 2:
            entra1 = Button(janela, bd=0, font=(
                "Calibri", 15), borderwidth=1, relief="solid", justify="center", text=x[0])
            entra1.place(width=48, height=48, x=156, y=201)
            entra2 = Button(janela, bd=0, font=(
                "Calibri", 15), borderwidth=1, relief="solid", justify="center", text=x[1])
            entra2.place(width=48, height=48, x=204, y=201)

        elif len(x) == 3:
            entra1 = Button(janela, bd=0, font=(
                "Calibri", 15), borderwidth=1, relief="solid", justify="center", text=x[0])
            entra1.place(width=48, height=48, x=156, y=201)
            entra2 = Button(janela, bd=0, font=(
                "Calibri", 15), borderwidth=1, relief="solid", justify="center", text=x[1])
            entra2.place(width=48, height=48, x=204, y=201)
            entra3 = Button(janela, bd=0, font=(
                "Calibri", 15), borderwidth=1, relief="solid", justify="center", text=x[2])
            entra3.place(width=48, height=48, x=252, y=201)
            candi()

    confirmar = Button(janela, bd=0, bg="#00c4cc",
                       image=confirma, command=confirmacao)
    confirmar.place(width=133, height=77, x=311, y=317)

    corrigir = Button(janela, bd=0, bg="#00c4cc",
                      image=corrige, command=corrigindo)
    corrigir.place(width=128, height=53, x=159, y=329)

    branca = Button(janela, bd=0, bg="#00c4cc",
                    image=branco, command=votoBranco)
    branca.place(width=122, height=53, x=13, y=329)

    secretario = Button(janela, bd=0, bg="#00c4cc",
                        image=secretarios, command=ler)
    secretario.place(width=140, height=47, x=280, y=547)

    n0 = Button(janela, bd=0, bg="#00c4cc",
                image=b0, command=lambda: cont("0"))
    n0.place(width=51, height=51, x=545, y=300)
    n1 = Button(janela, bd=0, bg="#00c4cc",
                image=b1, command=lambda: cont("1"))
    n1.place(width=51, height=51, x=482, y=110)
    n2 = Button(janela, bd=0, bg="#00c4cc",
                image=b2, command=lambda: cont("2"))
    n2.place(width=51, height=51, x=545, y=110)
    n3 = Button(janela, bd=0, bg="#00c4cc",
                image=b3, command=lambda: cont("3"))
    n3.place(width=51, height=51, x=608, y=110)
    n4 = Button(janela, bd=0, bg="#00c4cc",
                image=b4, command=lambda: cont("4"))
    n4.place(width=51, height=51, x=482, y=173)
    n5 = Button(janela, bd=0, bg="#00c4cc",
                image=b5, command=lambda: cont("5"))
    n5.place(width=51, height=51, x=545, y=173)
    n6 = Button(janela, bd=0, bg="#00c4cc",
                image=b6, command=lambda: cont("6"))
    n6.place(width=51, height=51, x=608, y=173)
    n7 = Button(janela, bd=0, bg="#00c4cc",
                image=b7, command=lambda: cont("7"))
    n7.place(width=51, height=51, x=482, y=236)
    n8 = Button(janela, bd=0, bg="#00c4cc",
                image=b8, command=lambda: cont("8"))
    n8.place(width=51, height=51, x=545, y=236)
    n9 = Button(janela, bd=0, bg="#00c4cc",
                image=b9, command=lambda: cont("9"))
    n9.place(width=51, height=51, x=608, y=236)

    busca = Entry(janela, bd=0, font=("Calibri", 15), highlightcolor="black",
                  highlightbackground="black", highlightthickness=2)
    busca.place(width=243, height=43, x=228, y=484)

    lupas = Button(janela, bd=0, bg="#ffffff", image=lupa, command=pesquisar)
    lupas.place(width=30, height=30, x=427, y=491)

    volta = Button(janela, bd=0, bg="#00c4cc",
                   image=but_voltar, command=retornar)
    volta.place(width=40, height=40, x=7, y=555)

    janela.mainloop()
