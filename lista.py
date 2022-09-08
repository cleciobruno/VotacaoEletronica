from tkinter import ttk
import pandas as pd
from tkinter import *
import votacao

# dataframe (lista dos candidatos)
df = pd.DataFrame(columns=['Candidato', 'Nome',
                  'Proposta', 'Apartamento', 'Número da Chapa'])

# função para mostrar a tabela
def mostrar():

    # janela
    janela = Tk()
    janela.title("Visualizar Candidatos")
    janela.geometry("490x560+540+153")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=False, height=False)

    # função voltar
    def voltar():
        janela.destroy()
        votacao.janela()

    # imagens
    cad = PhotoImage(file="imagens/visualizar.png")
    but_voltar = PhotoImage(file="imagens/voltar.png")

    # fundo cadastrar
    fundo = Label(janela, image=cad)
    fundo.pack()

    # botão de voltar
    volta = Button(janela, bd=0, bg="#00c4cc",
                   image=but_voltar, command=voltar)
    volta.place(width=40, height=40, x=7, y=514)

    # frame da tabela
    frame = Frame(fundo, highlightcolor="black",
                  highlightbackground="black", highlightthickness=2)
    frame.place(width=460, height=430, x=13, y=74)

    # tabela
    tabela = ttk.Treeview(frame)
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

    # for para percorrer o dataframe
    for i in range(len(df)):
        cand = df.loc[i]
        tabela.insert(parent='', index='end', iid=i, text='', values=(
            cand.Candidato, cand.Nome, cand.Proposta, cand.Apartamento, cand["Número da Chapa"]))

    # ajustando tabela
    tabela.place(width=456, height=426)

    janela.mainloop()
