from tkinter import *
from tkinter import ttk
import votos
import lista


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

        s = ttk.Style()
        s.theme_use('default')

        # Configure the style of Heading in Treeview widget
        s.configure('Treeview.Heading', background="#D3D3D3",
                    font=('Calibri', 11, 'bold'))

        tabela = ttk.Treeview(janela)
        tabela["columns"] = ("Nome", "Votos")
        tabela.column("#0", width=0,  stretch=NO)
        tabela.column("Nome", anchor="center")
        tabela.column("Votos", anchor="center")
        tabela.heading("#0", text="", anchor="center")
        tabela.heading("Nome", text="Nome", anchor="center")
        tabela.heading("Votos", text="Votos", anchor="center")

        data = votos.df1.sort_values(
            by=['Votos'], ascending=False).reset_index(drop=True)
        maior = data['Votos'].iloc[0]
        quant = data.loc[data['Votos'] == maior]
        tabela.tag_configure('a1', background='#FA8700', foreground='white')
        tabela.tag_configure('a2', background='green', foreground='white')

        for i in range(len(data)):

            if len(quant) == 1:
                if i == 0:
                    tag = 'a2'
                else:
                    tag = ''
            else:
                if i < len(quant):
                    tag = 'a1'
                else:
                    tag = ''

            cand = data.loc[i]
            tabela.insert(parent='', index='end', iid=i, text='',
                          values=(cand.Candidato, cand.Votos), tags=tag)

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

        data = votos.df.sort_values(by=['Votos'], ascending=False)

        quant = data.loc[data['Votos'] == data['Votos'].iloc[0]]
        quant1 = data.loc[data['Votos'] == data['Votos'].iloc[1]]
        tabela.tag_configure('a3', background='green', foreground='white')
        tabela.tag_configure('a4', background='#FA8700', foreground='white')
        func = 0

        if len(quant) == 2:
            func = 1

        if len(quant) == 1:
            if len(quant1) == 1:
                func = 1
            elif len(quant1) > 1:
                func = 2

        if len(quant) > 2:
            func = 3

        for i in range(len(data)):
            if func == 1:
                if i < 2:
                    tag = 'a3'
                else:
                    tag = ''

            if func == 2:
                if i == 0:
                    tag = 'a3'
                elif i < len(quant1) + 1:
                    tag = 'a4'
                else:
                    tag = ''

            if func == 3:
                if i < len(quant):
                    tag = 'a4'
                else:
                    tag = ''

            cand = data.loc[i]
            tabela.insert(parent='', index='end', iid=i, text='',
                          values=(cand.Candidato, cand.Votos), tags=tag)

        tabela.place(width=451, height=181, x=19, y=367)
    # fundo
    fundo = Label(janela, image=eleitos)
    fundo.pack()
    tabelas()
    tabelas1()

    lista.df.to_json('data2.json')

    # loop da janela
    janela.mainloop()
