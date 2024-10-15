import datetime
def questao1():
    SemanaD = []
    SemanaD.append('SEG')
    SemanaD.append('TER')
    SemanaD.append('QUA')
    SemanaD.append('QUI')
    SemanaD.append('SEX')
    SemanaD.append('SAB')
    SemanaD.append('DOM')
    dia = int(input('Digite o Dia:'))
    mes = int(input('Digite o Mes:'))
    ano = int(input('Digite o Ano:'))
    x = datetime.datetime(ano,mes,dia)
    semana = x.weekday()
    print('O dia da semana é: ', SemanaD[semana])
questao1()