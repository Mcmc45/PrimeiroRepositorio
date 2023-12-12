import tkinter as tk
from Pessoa import Pessoa
from datetime import datetime as dt

janela = tk.Tk()
janela.geometry('320x320')
janela.title('Age Calculator')

nome = tk.Label(text = 'Nome:', height = 2,font = ('Bookman Old Style',14))
nome.grid(column = 0, row = 1)

dia = tk.Label(text = 'Dia:',height = 2, font = ('Bookman Old Style',14))
dia.grid(column = 0, row = 2)

mes = tk.Label(text = 'Mês:',height = 2, font = ('Bookman Old Style',14))
mes.grid(column = 0, row = 3)

ano = tk.Label(text = 'Ano:', height = 2,font = ('Bookman Old Style',14))
ano.grid(column = 0, row = 4)

# =========================================

campoNome = tk.Entry(width=12 ,font = ('Bookman Old Style',14))
campoNome.grid(column= 1 , row=1)

campoDia = tk.Entry(width=12 ,font = ('Bookman Old Style',14))
campoDia.grid(column= 1 , row=2)

campoMes = tk.Entry(width=12 ,font = ('Bookman Old Style',14))
campoMes.grid(column= 1 , row=3)

campoAno = tk.Entry(width=12 ,font = ('Bookman Old Style',14))
campoAno.grid(column= 1 , row=4)

#===============================================
def limpar() -> None:
    lista = [campoNome , campoDia, campoMes, campoAno]

    for input in lista:
        input.delete(0, tk.END)
#===============================================
bCalcular = tk.Button(janela, text = 'OK', width = 10 , font =('Bookman Old Style',14) )
bCalcular.grid (column= 1 , row=5)


bLimpar = tk.Button(janela, text = 'Limpar', command = limpar , width = 10 , font =('Bookman Old Style',14) )
bLimpar.grid (column= 0 , row=5)

#==============================================

janela.mainloop()