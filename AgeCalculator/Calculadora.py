import tkinter as tk
from Pessoa import Pessoa
from datetime import datetime as dt
from tkinter import messagebox as mb

janela = tk.Tk()
janela.geometry('320x320')
janela.title('Age Calculator')
janela.resizable(False,False)
janela.anchor(anchor='center')


nome = tk.Label(text = 'Nome:', height = 2,font = ('Bookman Old Style',14))
nome.grid(column = 0, row = 1)

ano = tk.Label(text = 'Ano:', height = 2,font = ('Bookman Old Style',14))
ano.grid(column = 0, row = 2)

# =========================================

campoNome = tk.Entry(width=12 ,font = ('Bookman Old Style',14))
campoNome.grid(column= 1 , row=1)

campoAno = tk.Entry(width=12 ,font = ('Bookman Old Style',14))
campoAno.grid(column= 1 , row=2)

#===============================================

def getInputs():
        try:
            humano = Pessoa(campoNome.get(), int(campoAno.get()))
            limpar()
            mb.showinfo(title = 'Resultado ' , message =f'Olá {humano.nome} , você tem {humano.idade()} , anos de idade')
        except ValueError :
            mb.showerror(title= 'Erro!', message = 'Informe apenas número no campo ANO')
#===============================================
def limpar() -> None:
    lista = [campoNome , campoAno]

    for input in lista:
        input.delete(0, tk.END)
#===============================================
bCalcular = tk.Button(janela, text = 'OK', command = getInputs ,width = 10 , font =('Bookman Old Style',14) )
bCalcular.grid (column= 1 , row=5)


bLimpar = tk.Button(janela, text = 'Limpar', command = limpar , width = 10 , font =('Bookman Old Style',14) )
bLimpar.grid (column= 0 , row=5)

#==============================================

janela.mainloop()