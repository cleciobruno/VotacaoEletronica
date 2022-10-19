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

        s = ttk.Style()
        s.theme_use('default')

        # Configure the style of Heading in Treeview widget
        s.configure('Treeview.Heading', background="#D3D3D3", font=('Calibri', 11,'bold'))

        tabela = ttk.Treeview(janela)
        tabela["columns"] = ("Nome", "Votos")
        tabela.column("#0", width=0,  stretch=NO)
        tabela.column("Nome", anchor="center")
        tabela.column("Votos", anchor="center")
        tabela.heading("#0", text="", anchor="center")
        tabela.heading("Nome", text="Nome", anchor="center")
        tabela.heading("Votos", text="Votos", anchor="center")

        data = votos.df1.sort_values(by=['Votos'], ascending=False).reset_index(drop=True)
        maior = data['Votos'].iloc[0]
        quant = data.loc[data['Votos'] == maior]
        for i in range(len(data)):
            tag = ''
            if i <= len(quant) - 1:
                if i > 0:
                    tabela.tag_configure('br', background='#FA8700', foreground='white')
                    tag = 'br'
                else:
                    tabela.tag_configure('br', background='green', foreground='white')
                    tag = 'br'
            else:
                tag = ''
            cand = data.loc[i]
            tabela.insert(parent='', index='end', iid=i, text='', values=(cand.Candidato, cand.Votos), tags=tag)
            
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

        maior = data['Votos'].iloc[0]
        quant = data.loc[data['Votos'] == maior]
        for i in range(len(data)):
            tag = ''
            if i <= len(quant) - 1:
                if i > 0:
                    tabela.tag_configure('bru', background='#FA8700', foreground='white')
                    tag = 'bru'
                else:
                    tabela.tag_configure('bru', background='green', foreground='white')
                    tag = 'bru'
            else:
                tag = ''
            cand = data.loc[i]
            tabela.insert(parent='', index='end', iid=i, text='', values=(cand.Candidato, cand.Votos), tags=tag)

        tabela.place(width=451, height=181, x=19, y=367)
    # fundo
    fundo = Label(janela, image=eleitos)
    fundo.pack()
    tabelas()
    tabelas1()
    # loop da janela
    janela.mainloop()