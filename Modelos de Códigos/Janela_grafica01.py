from tkinter import *
#janela.geometry('300x400')
#janela.config(bg='yellow')

janela = Tk()
janela.title('Exemplo')
janela.rowconfigure(4) # 6 linhas
janela.columnconfigure(3) # 3 colunas
# rótulo

rotuloA = Label(janela, text='RÓTULO A', bg='lightblue', font='Verdana 18 bold')
rotuloA.grid(row='0', column='0')

rotuloB = Label(janela, text='RÓTULO B', bg='gray', font='Verdana 18 bold')
rotuloB.grid(row='0', column='1', columnspan='2', stick='wesn') # columnspan mescla duas colunas

rotuloC = Label(janela, text='RÓTULO C', bg='lightgreen', font='Verdana 18 bold')
rotuloC.grid(row='1', column='0', columnspan='2', rowspan='2', stick='wesn') # rowspan mescla duas linhas

rotuloD = Label(janela, text='RÓTULO D', bg='yellow', font='Verdana 18 bold')
rotuloD.grid(row='1', column='2')

rotuloE = Label(janela, text='RÓTULO E', bg='lightpink', font='Verdana 18 bold')
rotuloE.grid(row='2', column='2')

rotuloF = Label(janela, text='RÓTULO F', bg='green', font='Verdana 18 bold')
rotuloF.grid(row='3', column='0')

rotuloG = Label(janela, text='RÓTULO G', bg='lightyellow', font='Verdana 18 bold')
rotuloG.grid(row='3', column='1')

rotuloH = Label(janela, text='RÓTULO H', bg='gray', font='Verdana 18 bold')
rotuloH.grid(row='3', column='2', stick='wesn')

rotuloI = Label(janela, text='RÓTULO I', bg='gray', font='Verdana 18 bold')
rotuloI.grid(row='4', column='0', stick='wesn')

rotuloK = Label(janela, text='RÓTULO K', bg='yellow', font='Verdana 18 bold')
rotuloK.grid(row='5', column='0', stick='wesn')

rotuloJ = Label(janela, text='RÓTULO J', bg='orange', font='Verdana 18 bold')
rotuloJ.grid(row='4', column='1', columnspan='2', rowspan='2', stick='wesn')

janela.mainloop()