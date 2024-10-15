import sys
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Tk, Label, Entry, Button, Frame, Scrollbar, Spinbox, simpledialog, Checkbutton, Scale, StringVar, IntVar
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter.ttk import Treeview, Combobox
from mysql.connector import connect


def centralizar_janela(janela):
    janela.update()
    largura_da_tela = janela.winfo_screenwidth()
    altura_da_tela = janela.winfo_screenheight()

    largura_da_janela = janela.winfo_width()
    altura_da_janela = janela.winfo_height()

    meio_x = largura_da_tela // 2
    meio_y = altura_da_tela // 2

    metade_da_largura = largura_da_janela // 2
    metade_da_altura = altura_da_janela // 2

    x = meio_x - metade_da_largura
    y = meio_y - metade_da_altura

    janela.geometry("+" + str(x) + "+" + str(y))

class BancoLogin:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def obter_conexao(self):
        return  connect(host = self.host, user = self.user, password = self.password, database = self.database) #realiza a conexao
    def login_ok(self,email, senha):
        sql = "select codigo from usuario where email=%s and senha= SHA2(%s, 256)"
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(sql, (email, senha))
        resultado = cursor.fetchall()
        print(resultado)
        # se for encontrado exatamente um usuário
        # com este usuário e senha, retorna o nome
        # desse usuário; senão, retorna None.
        if len(resultado) == 1:

            return resultado[0][0]
        return None

    def login_verificado(self,email,senha):
        sql = "select verificado from usuario where email=%s and senha= SHA2(%s, 256)"
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(sql, (email,senha))
        resultado = cursor.fetchall()
        print('resultado')
        print(resultado)
        print('resultado')
        if resultado == [(0,)]:
            return None
        return 1

    def login_verifica_codigo(self,email,cod_ver):
        sql = "select cod_verificado from usuario where email=%s and cod_verificado = %s"
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(sql, (email, cod_ver))
        resultado = cursor.fetchall()
        print(resultado)
        # se for encontrado algum codigo igual ao q o usuario informou
        # com este usuário e senha, retorna algo
        if len(resultado) == 1:
            return resultado[0][0]
        return None
    def alterar_verificado(self,email):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        sql = "update usuario set verificado = 1 where email = %s"
        cursor.execute(sql, [email])
        conexao.commit()
        conexao.close()
class JanelaLogin:
    def botao_cadastrar(self):
        codigo = str(random.randint(0, 9999))
        codigo = codigo.zfill(4)
        #inserindo os valores na tabela
        conexao = self.banco.obter_conexao()
        cursor = conexao.cursor()
        email = self.campo1.get()
        senha = self.campo2.get()
        print('user:', email)
        print('password:', senha)
        sql = "INSERT INTO usuario( email, senha, cod_verificado) values(%s,SHA2(%s, 256), %s);"
        cursor.execute(sql,[email, senha, codigo])
        cursor.fetchall()
        conexao.commit()
        print(codigo)

        host = 'smtp.gmail.com'
        port = '587'
        login = 'poo.cesit@gmail.com'
        senha = 'rjnb fhqw plsp afgz'

        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(login, senha)
        corpo = f"Para confirmar sua ientidade, efetue login no sistema e informe o código {codigo}quando solicitado"
        # montando o e-mail

        email_msg = MIMEMultipart()
        email_msg['from'] = login
        email_msg['To'] = email
        email_msg['Subject'] = f"Código de verificação:{codigo}"
        email_msg.attach(MIMEText(corpo, 'plain'))

        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        server.quit()
        print("E-mail enviado!")
        showinfo(title='Cadastrado', message='Para finalizar seu cadastro, efetue login novamente e informe o código de verificação enviado para o seu e-mail.')
    def botaosair(self):
        print('botao clicado')
        var = askyesno(title='Sair', message='Confirmar a Saída?')
        print(var)
        if var is True:
            self.janela.destroy()
        else:
            return
    def botaoconectar(self):
        email = self.campo1.get()
        senha = self.campo2.get()
        user = self.banco.login_ok(email,senha)
        ver = self.banco.login_verificado(email,senha)
        print('user:', email)
        print('password:', senha)
        if user is not None:
            if ver is None:
                verificacao = simpledialog.askstring("Verificação de usuário","Por favor, insira abaixo o código enviado para o e-mail padovani@uea.edu.br para validar o seu cadastro:")
                verificado = self.banco.login_verifica_codigo(email,verificacao)
                if verificado is not None:
                    showinfo(title='sucesso!', message='Seja Bem vindo(a)')
                    #mudando o valo de verificado para 1
                    self.banco.alterar_verificado(email)
                    self.janela.destroy()
                    JanelaSupermercado()  # abre a janela do CRUD de Supermercado
                else:
                    showerror(title='Erro!', message="Código de verificação incorreto!")
            else:
                showinfo(title='sucesso!', message='Seja Bem vindo(a)')
                self.janela.destroy()
                JanelaSupermercado()  # abre a janela do CRUD de Supermercado
        else:
            showerror(title='Erro!', message='User não encontrado!')

    def __init__(self):
        self.banco = BancoLogin(host='localhost', user='root', password='2106', database='ap2')
        janela = Tk()
        self.janela = janela
        janela.title('Login')
        janela.rowconfigure(4) # 4 linhas
        janela.columnconfigure(4) # 4 colunas

        rotuloautenticar = Label(janela, text='AUTENTICAÇÃO DE USUÁRIO',font='Verdana 18 bold', fg='white', bg='darkblue')
        rotuloautenticar.grid(row=0, column=0, columnspan=4, sticky='wesn')

        rotuloemail = Label(janela, text='E-mail', font='Verdana 18')
        rotuloemail.grid(row=1, column=0, sticky='wesn')

        rotulosenha = Label(janela, text='Senha', font='Verdana 18')
        rotulosenha.grid(row=2, column=0, sticky='wesn')

        campo1 = Entry(janela, text='E-mail', font='Verdana 18')
        campo1.grid(row=1, column=1, columnspan=3, sticky='wesn')
        campo1.focus_force()
        self.campo1 = campo1

        campo2 = Entry(janela, text='Senha', font='Verdana 18', show='☠')
        campo2.grid(row=2, column=1, columnspan=3, sticky='wesn')
        self.campo2 = campo2

        botao1 = Button(janela, text='Conectar', font='Verdana 18',bg='gray', command=self.botaoconectar)
        botao1.grid(row=3, column=0, sticky='wesn')


        botao2 = Button(janela, text='Cadastrar', font='Verdana 18',bg='gray', command=self.botao_cadastrar)
        botao2.grid(row=3, column=1, sticky='wesn')

        botao3 = Button(janela, text='Fechar', font='Verdana 18',bg='gray',command=self.botaosair)
        botao3.grid(row=3, column=2, columnspan=2, sticky='wesn')

        centralizar_janela(janela)
        janela.mainloop()
class JanelaSupermercado:
    def __init__(self):
        self.alt_inser = 0
        self.banco = BancoSupermercado('localhost','root', '2106', 'ap2')
        janela = Tk()
        janela.title('Supermercado')
        janela.rowconfigure(11)
        janela.columnconfigure(4)
        fonte = 'Helvetica 14'

        rotulo = Label(janela, font=fonte,
                       text='LISTAGEM DE REGISTROS',
                       bg='darkblue',fg='white')
        rotulo.grid(row=1, column=0, columnspan=4, sticky='wesn')

        frame = Frame(janela)
        frame.grid(row=2, column=0, columnspan=4,sticky='wesn')
        frame.columnconfigure(2)
        frame.rowconfigure(1)

        tabela = Treeview(frame, selectmode='browse',
                          columns=['Código', 'Nome', 'Deficiente', 'Quantidade de dependentes', 'Gênero'],
                          show='headings')
        tabela.grid(row=0, column=0, sticky='wesn')
        tabela.heading('Código',text='Código')
        tabela.heading('Nome', text='Nome')
        tabela.heading('Deficiente', text='Deficiente')
        tabela.heading('Quantidade de dependentes', text='Quantidade de dependentes')
        tabela.heading('Gênero', text='Gênero')
        frame.grid(row=2, column=0, columnspan=4, rowspan=3, sticky="wesn")
        tabela.selection()
        funcionarios = self.banco.obter_funcionarios()
        for funcionarios in funcionarios:
            tabela.insert('', 'end', values=funcionarios)

        # cria a barra de rolagem e define o comportamento da barra
        barra = Scrollbar(frame, orient='vertical', command=tabela.yview)
        barra.grid(row=0, column=1, sticky='wesn')
        # configura o comportamento da barra quando a tabela se movimento
        tabela.configure(yscrollcommand=barra.set)
        self.tabela = tabela

        botao_inserir = Button(janela, font=fonte, text='Inserir', command=self.inserir)
        botao_inserir.grid(row=5, column=0)

        botao_alterar = Button(janela, font=fonte, text='Alterar', command=self.alterar)
        botao_alterar.grid(row=5, column=1)

        botao_apagar = Button(janela, font=fonte, text='Apagar', command=self.apagar)
        botao_apagar.grid(row=5, column=2)

        botao_sair = Button(janela, font=fonte, text='Sair', command=self.sair)
        botao_sair.grid(row=5, column=3)

        rotulo_atualizacao = Label(janela, font=fonte,
                        text='ATUALIZAÇÃO DE REGISTROS',
                        bg='darkblue', fg='white')
        rotulo_atualizacao.grid(row=7, column=0, columnspan=4, sticky='wesn')

        self.alt_entry1 = StringVar()
        self.info1 = Label(janela, text='Codigo:', font=fonte)
        self.info1.grid(row=8, column=0)
        self.info1 = Entry(janela, font=fonte, textvariable=self.alt_entry1)
        self.info1.grid(row=8, column=1, columnspan=4, sticky='wesn')
        self.info1.config(state='disabled')

        self.alt_entry2 = StringVar()
        self.info2 = Label(janela, text='Nome:', font=fonte)
        self.info2.grid(row=9, column=0)
        self.info2 = Entry(janela, font=fonte, textvariable=self.alt_entry2)
        self.info2.grid(row=9, column=1, columnspan=4, sticky='wesn')
        self.info2.config(state='disabled')

        self.alt_info3 = IntVar()
        self.info3 = Label(janela, text='Deficiente:', font=fonte)
        self.info3.grid(row=10, column=0)
        self.info3 = Checkbutton(janela, text='tem esta característica?', variable=self.alt_info3, onvalue= 1, offvalue=0, font=fonte)
        self.info3.grid(row=10, column=1)
        self.info3.config(state='disabled')

        self.alt_info4 = IntVar
        self.info4 = Label(janela, text='Quantidade de dependentes:', font=fonte)
        self.info4.grid(row=11, column=0)
        self.info4 = Spinbox(janela, from_=0,to=5,font=fonte, textvariable=self.alt_info4)
        self.info4.grid(row=11, column=1, columnspan=4, sticky='wesn')
        self.info4.config(state='disabled')

        self.info5 = Label(janela, text='Gênero:', font=fonte)
        self.info5.grid(row=12, column=0)
        self.info5 = Combobox(janela, values=['Masculino','Feminino','Outro',], font=fonte)
        self.info5.grid(row=12, column=1, columnspan=4, sticky='wesn')
        self.info5.config(state='disabled')

        self.botao_salvar = Button(janela,text='Salvar', font=fonte, command=self.botao_salvar)
        self.botao_salvar.grid(row=13, column=1)
        self.botao_salvar.config(state='disabled')

        self.botao_cancelar = Button(janela, text='Cancelar', font=fonte, command=self.botao_cancelar)
        self.botao_cancelar.grid(row=13, column=2)
        self.botao_cancelar.config(state='disabled')

        centralizar_janela(janela)
        janela.mainloop()
    def inserir(self):
        print('Botão clicado!')
        self.info1.config(state='normal')
        self.info2.config(state='normal')
        self.info3.config(state='normal')
        self.info4.config(state='normal')
        self.info5.config(state='normal')
        self.botao_salvar.config(state='normal')
        self.botao_cancelar.config(state='normal')
        self.alt_inser == 0

    def alterar(self):
        escolhido = self.tabela.selection()
        if(escolhido is not None):
            self.info1.config(state='normal')
            self.info2.config(state='normal')
            self.info3.config(state='normal')
            self.info4.config(state='normal')
            self.info5.config(state='normal')
            self.botao_salvar.config(state='normal')
            self.botao_cancelar.config(state='normal')
            self.alt_inser = 1
            self.alt_info4.set(1)
            print(self.alt_info4)
        else:
            showerror(title='Erro!', message='Nenhuma linha selecionada!')
    def apagar(self):
        print('botão clicado!')
        selecao = self.tabela.selection()
        if len(selecao) == 0:
            showerror(title='Apagar', message='Selecione um item para apagar')
        else:
            print(selecao)
            print(selecao[0])
            valores = self.tabela.item(selecao[0], 'values')
            cod_verificado = valores[-1]
            self.banco.apagar(codigo)
            showinfo(title='Sucesso', message='Produto Apagado!')
    def sair(self):
        sair = askyesno(title='Sair', message='Confirmar a Saída?')
        print(sair)
        if sair is True:
            sys.exit(0)
        else:
            return
    def botao_salvar(self):
        escolhido = self.tabela.selection()
        if self.alt_inser == 1:
            selecionado = self.tabela.item(escolhido, 'values')
            self.alt_entry1.set(selecionado[0])
            self.alt_entry2.set(selecionado[1])
            if selecionado[2] == '1':
                print(selecionado[2])
                self.info3.select()
                valor_deficiente = self.alt_info3.get()
            else:
                self.info3.deselect()
                valor_deficiente = self.alt_info3.get()


            valor_codigo = self.info1.get()
            valor_nome = self.info2.get()
            valor_dependente = self.info4.get()
            valor_genero = self.info5.get()

            self.banco.alter_funcionario(valor_codigo,valor_nome,valor_deficiente,valor_dependente, valor_genero)
            showinfo(title='Salvar', message='User salvo com sucesso!')
        else:
            valor_codigo = self.info1.get()
            valor_nome = self.info2.get()
            valor_deficiente = self.alt_info3.get()
            valor_dependente = self.info4.get()
            valor_genero = self.info5.get()
            self.banco.cadastrar(valor_codigo, valor_nome, valor_deficiente, valor_dependente, valor_genero)

    def botao_cancelar(self):
        print('botão cancelar')
class BancoSupermercado:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def obter_conexao(self):
        return connect(host = self.host, user = self.user, password = self.password, database = self.database)

    def obter_funcionarios(self):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        sql = """
                    select codigo, nome,deficiente, qtd_dependentes, genero from funcionario order by 1;
                """
        cursor.execute(sql,)
        resultado = cursor.fetchall()
        conexao.close()
        print('resultado: ')
        print(resultado)
        return resultado
    def apagar(self, escolhido):
        escolhido = escolha
        codigo = escolhido[0]
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        sql = "delete from funcionario where codigo = %s"
        cursor.execute(sql, [codigo])
        conexao.commit()
        conexao.close()

    def cadastrar(self, codigo, nome,deficiente, qtd_dependentes, genero = None):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        sql = "INSERT INTO funcionario(codigo, nome, deficiente, qtd_dependentes, genero) values(%s,%s,%s,%s,%s);"
        cursor.execute(sql, [codigo, nome,deficiente, qtd_dependentes, genero])
        cursor.fetchall()
        conexao.commit()
        showinfo(title='sucesso!', message='Cadastrado com sucesso!')

    def alter_funcionario(self, codigo, nome, deficiente, qtd_dependentes, genero):
        print('fazoL')

janelalogin = JanelaLogin()
