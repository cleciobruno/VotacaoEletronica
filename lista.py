from tkinter import messagebox, ttk
import pandas as pd
from tkinter import *
import votacao
import cadastro_cand
import atualizar_cand 

# dataframe (lista dos candidatos)
df = pd.DataFrame(columns=['Candidato', 'Nome',
                  'Proposta', 'Apartamento', 'Número da Chapa'])

# função principal
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
    cad = PhotoImage(file="imagens/visualizar_att.png")
    but_voltar = PhotoImage(file="imagens/voltar.png")
    but_remover = PhotoImage(file="imagens/remo_atu.png")
    but_cadas = PhotoImage(file="imagens/cad_atu.png")
    but_atu = PhotoImage(file="imagens/visu_atu.png")

    # fundo cadastrar
    fundo = Label(janela, image=cad)
    fundo.pack()

    # frame da tabela
    frame = Frame(fundo, highlightcolor="black",
                  highlightbackground="black", highlightthickness=2)
    frame.place(width=460, height=380, x=13, y=63)

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

    # variável da pessoa selecionada
    pessoa = []

    # função selecionar
    def item_selected(event):
        pessoa.clear()
        for selected_item in tabela.selection():
            pessoa.append(selected_item)
            item = tabela.item(selected_item)
            record = item['values']
            pessoa.append(record)

    # função cadastro
    def cadastro():
        janela.destroy()
        cadastro_cand.cadastrar()

    # função deletar
    def deletar():
        if len(pessoa) != 0:
            x = messagebox.askquestion(
                "Deletar", f"Você deseja deletar '{pessoa[1][1]}'?")
            if x == "yes":
                df.drop(df.loc[df['Nome'] == pessoa[1][1]].index, inplace=True)
                janela.destroy()
                mostrar()

    # função atualizar
    def atualizar():
        if len(pessoa) != 0:
            janela.destroy()
            atualizar_cand.atu_cand(pessoa)
    
    # capta a linha selecionada da tabela
    tabela.bind('<<TreeviewSelect>>', item_selected)

    # for para percorrer o dataframe
    for i in range(len(df)):
        cand = df.loc[i]
        tabela.insert(parent='', index='end', iid=i, text='', values=(
            cand.Candidato, cand.Nome, cand.Proposta, cand.Apartamento, cand["Número da Chapa"]))

    # ajustando tabela
    tabela.place(width=456, height=390)
    
    # verifica o tamanho da lista para liberação dos botões
    if len(df) > 0:
        cond = "normal"
    else:
        cond = "disable"

    # botões
    volta = Button(janela, bd=0, bg="#00c4cc",
                   image=but_voltar, command=voltar)
    volta.place(width=40, height=40, x=7, y=514)
    remo = Button(janela, bd=0, bg="#00c4cc",
                  image=but_remover, command=deletar, state=cond)
    remo.place(width=147, height=43, x=329, y=460)
    cadastrar = Button(janela, bd=0, bg="#00c4cc",
                       image=but_cadas, command=cadastro)
    cadastrar.place(width=147, height=43, x=14, y=460)
    atu = Button(janela, bd=0, bg="#00c4cc",
                 image=but_atu, command=atualizar, state=cond)
    atu.place(width=147, height=43, x=172, y=460)

    # loop da janela
    janela.mainloop()
