from tkinter import *
#janela.geometry('300x400')
#janela.config(bg='yellow')

janela = Tk()
janela.title('Exemplo')
janela.rowconfigure(5) # 5 linhas
janela.columnconfigure(1) # 1 colunas

# rótulo
rotuloA = Label(janela, text='Primeiro Rótulo', bg='gray', font='Verdana 18 bold')
rotuloA.grid(row='0', column='0')

#botão
botao = Button(janela, text='Clique aqui')
botao.grid(row='1', column='0', sticky='wesn')

#campotexto
campo_texto = Entry(janela)
campo_texto.grid(row='2', column='0', sticky='wesn')

#botao pra marcar
sim_nao = Checkbutton(janela, text='Atendimento Especial', font='Verdana 18')
sim_nao.grid(row='3', column='0', sticky='wesn')

#botao escala
escala = Scale(janela, from_=0,to=10, font='Verdana 18')
escala.grid(row='4', column='0', sticky='wesn')

numero = Spinbox(janela, from_=1,to=5, font='Verdana 18')
numero.grid(row='5', column='0', sticky='wesn')

janela.mainloop()