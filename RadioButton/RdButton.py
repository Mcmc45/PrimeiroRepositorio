import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

frame = tk.Tk()
frame.geometry('350x300')
frame.resizable(False, False)
frame.title('Exemplo de radio Button')
#frame.tk.call('wm', 'incophoto', frame._w , tk.PhotoImage(file='python-logo-only.png'))

def mostrarEscolha():
    showinfo(title= 'Resultado', message= f'Voce escolheu {tam_selecionado.get()}')

lblPergunta = ttk.Label(text = 'Escolha o tamanho:')
lblPergunta.pack(fill= 'x', padx = 15 , pady = 5)

tam_selecionado = tk.StringVar(frame, value = 'M')
tamanhos = (('Pequeno ', 'P') ,( 'Médio', 'M'), ('Grande ', 'G'),('Extra Grande ','XG'),('Extra Extra Grande ', 'XXG'))

for tamanho in tamanhos:
    rd = ttk.Radiobutton(frame, text = tamanho[0] , value = tamanho[1] , variable = tam_selecionado)
    rd.pack(fill = 'x', padx = 15 , pady = 5 )

btnEscolha = ttk.Button(frame, text = 'Ler Tamanho ', command = mostrarEscolha)
btnEscolha.pack(fill = 'x', padx = 15 , pady = 15)

frame.mainloop()