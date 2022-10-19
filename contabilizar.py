from tkinter import *
from tkinter import messagebox, ttk
import votos

def janela():

    # janela principal
    janela = Tk()
    janela.title("Votação Eletrônica")
    janela.geometry("490x560+540+153")
    janela.iconbitmap(default="imagens/cat.ico")
    janela.resizable(width=False, height=False)

    # upload das imagens
    eleitos = PhotoImage(file="imagens2/eleitos.png")

    def tabelas():
        tabela = ttk.Treeview(janela)
        tabela["columns"] = ("Nome", "Votos")
        tabela.column("#0", width=0,  stretch=NO)
        tabela.column("Nome", anchor="center")
        tabela.column("Votos", anchor="center")
        tabela.heading("#0", text="", anchor="center")
        tabela.heading("Nome", text="Nome", anchor="center")
        tabela.heading("Votos", text="Votos", anchor="center")

        for i in range(len(votos.df1)):
            cand = votos.df1.loc[i]
            tabela.insert(parent='', index='end', iid=i, text='', values=(cand.Candidato, cand.Votos))

        tabela.place(width=451, height=181, x=19, y=118)
    
    def tabelas1():
        tabela = ttk.Treeview(janela)
        tabela["columns"] = ("Nome", "Votos")
        tabela.column("#0", width=0,  stretch=NO)
        tabela.column("Nome", anchor="center")
        tabela.column("Votos", anchor="center")
        tabela.heading("#0", text="", anchor="center")
        tabela.heading("Nome", text="Nome", anchor="center")
        tabela.heading("Votos", text="Votos", anchor="center")


        tabela.place(width=451, height=181, x=19, y=367)
    # fundo
    fundo = Label(janela, image=eleitos)
    fundo.pack()
    tabelas()
    tabelas1()
    # loop da janela
    janela.mainloop()