import sys
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Tk, Label, Entry, Button, Frame, Scrollbar, Spinbox, simpledialog, Checkbutton, Scale
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
        return  connect(host = self.host, user = self.user, password = self.password, database = self.database)
    def login_ok(self,email, senha):
        sql = "select cod_verificado from usuario where email=%s and senha= SHA2(%s, 256)"
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(sql, (email, senha))
        resultado = cursor.fetchall()
        conexao.close()
        # se for encontrado exatamente um usuário
        # com este usuário e senha, retorna o nome
        # desse usuário; senão, retorna None.
        if len(resultado) == 1:
            return resultado[0][0]
        return None
class JanelaLogin:
    def botao_cadastrar(self):
        codigo = str(random.randint(0, 9999))
        codigo = codigo.zfill(4)
        conexao = self.banco.obter_conexao()
        cursor = conexao.cursor()
        email = self.campo1.get()
        senha = self.campo2.get()
        print('user:', email)
        print('password:', senha)
        sql = "INSERT INTO usuario( email, senha) values(%s,SHA2(%s, 256));"
        cursor.execute(sql,[email, senha])
        cursor.fetchall()
        conexao.commit()
        print(codigo)

        host = 'smtp.gmail.com'
        port = '587'
        login = 'rpds.lic21@uea.edu.br'
        senha = '04741529282'

        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(login, senha)
        corpo = f"Para confirmar sua ientidade, efetue login no sistema e informe o código {codigo}quando solicitado"
        # montando o e-mail

        email_msg = MIMEMultipart()
        email_msg['from'] = login
        email_msg['To'] = login
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
        print('user:', email)
        print('password:', senha)
        if user is not None:
            simpledialog.askstring("Verificação de usuário","Por favor, insira abaixo o código enviado para o e-mail padovani@uea.edu.br para validar o seu cadastro:")
            showinfo(title='sucesso!', message='Seja Bem vindo(a)' + user)
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
                          columns=['Info1', 'Info2', 'Info3', 'Info4'],
                          show='headings')
        tabela.grid(row=0, column=0, sticky='wesn')
        tabela.heading('Info1',text='Info1')
        tabela.heading('Info2', text='Info2')
        tabela.heading('Info3', text='Info3')
        tabela.heading('Info4', text='Info4')
        frame.grid(row=2, column=0, columnspan=4, rowspan=3, sticky="wesn")
        tabela.selection()


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

        info1 = Label(janela, text='Info 1:', font=fonte)
        info1.grid(row=8, column=0)
        info1 = Entry(janela, font=fonte, text='Info1')
        info1.grid(row=8, column=1, columnspan=4, sticky='wesn')

        info2 = Label(janela, text='Info 2:', font=fonte)
        info2.grid(row=9, column=0)
        info2 = Entry(janela, font=fonte, text='Info2')
        info2.grid(row=9, column=1, columnspan=4, sticky='wesn')

        info3 = Label(janela, text='Info 3:', font=fonte)
        info3.grid(row=10, column=0)
        info3 = Checkbutton(janela, text='tem esta característica?', font=fonte)
        info3.grid(row=10, column=1)

        info4 = Label(janela, text='Info 4:', font=fonte)
        info4.grid(row=11, column=0)
        info4 = Spinbox(janela, from_=1,to=5, font=fonte)
        info4.grid(row=11, column=1, columnspan=4, sticky='wesn')

        info5 = Label(janela, text='Info 5:', font=fonte)
        info5.grid(row=12, column=0)
        info5 = Combobox(janela, values=['x','y','z',], font=fonte)
        info5.grid(row=12, column=1, columnspan=4, sticky='wesn')

        botao_salvar = Button(janela,text='Salvar', font=fonte, command=self.botao_salvar)
        botao_salvar.grid(row=13, column=1)

        botao_cancelar = Button(janela, text='Cancelar', font=fonte, command=self.botao_cancelar)
        botao_cancelar.grid(row=13, column=2)

        centralizar_janela(janela)
        janela.mainloop()
    def inserir(self):
        print('Botão clicado!')
    def alterar(self, event=None):
        termo = self.campo.get()
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        registros = self.banco.obter_conexao(termo)
        for registro in registros:
            self.tabela.insert('', 'end', values=registro)
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
            self.banco.apagar(cod_verificado)
            self.alterar()
            showinfo(title='Sucesso', message='Produto Apagado!')
    def sair(self):
        sair = askyesno(title='Sair', message='Confirmar a Saída?')
        print(sair)
        if sair is True:
            sys.exit(0)
        else:
            return
    def botao_salvar(self):
        showinfo(title='Salvar', message='User salvo com sucesso!')
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
    def apagar(self, codigo):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        sql = "delete from funcionario where codigo = %s"
        cursor.execute(sql, [codigo])
        conexao.commit()
        conexao.close()

    def cadastrar(self, termo):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        sql = """
                insert into usuario( email, senha) values(
                'rkazuto2@gmail.com',
                SHA2('1111', 256));
               """
        termo = "%" + termo + "%"
        cursor.execute(sql, [termo, termo])
        resultado = cursor.fetchall()
        conexao.close()
        print(resultado)

janelalogin = JanelaLogin()