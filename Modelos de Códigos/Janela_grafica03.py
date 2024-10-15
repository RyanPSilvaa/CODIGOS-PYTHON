import sys
from tkinter import Tk, Label, Entry, Button, Frame, Scrollbar, Spinbox
from tkinter.messagebox import showinfo, showerror
from tkinter.ttk import Treeview, Combobox
from mysql.connector import connect, DatabaseError
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
class BancoLogin: # um objeto criado para cada janela
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def obter_conexao(self):
        return connect(host = self.host, user = self.user, password = self.password, database = self.database)
    def login_ok(self, email, senha):
        # esta consulta precisa ser alterada para funcionar
        # com o método de criptografia escolhido
        sql = "select nome from usuario where email=%s and senha= SHA2(%s, 256)"
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(sql, [email, senha])
        resultado = cursor.fetchall()
        conexao.close()
        # se for encontrado exatamente um usuário
        # com este usuário e senha, retorna o nome
        # desse usuário; senão, retorna None.
        if len(resultado) == 1:
            return resultado[0][0]
        return None
class JanelaLogin:
    def botaosair(self):
        print('botao clicado')
        sys.exit(0)
    def botaoconectar(self):
        usuario = self.campo1.get()
        senha = self.campo2.get()
        nome = self.banco.login_ok(usuario, senha)
        print('user:',usuario)
        print('password:',senha)
        if nome is not None:
            showinfo(title='sucesso!', message='Seja Bem vindo(a)' + nome)
            self.janela.destroy() # fecha a janela
            JanelaProduto() # abre a janela do CRUD de produtos
        else:
            showerror(title='Erro!', message='User não encontrado!')

    def __init__(self):
        self.banco = BancoLogin(host='localhost', user='root', password='2106', database='ap2')
        janela = Tk()
        self.janela = janela
        janela.title('Login')
        janela.rowconfigure(4) # 4 linhas
        janela.columnconfigure(4) # 4 colunas

        # rótulo
        rotuloautenticar = Label(janela, text='AUTENTICAÇÃO DE USUÁRIO',font='Verdana 18 bold', fg='white', bg='darkblue')
        rotuloautenticar.grid(row=0, column=0, columnspan=4, sticky='wesn')

        rotuloemail = Label(janela, text='E-mail', font='Verdana 18')
        rotuloemail.grid(row=1, column=0, sticky='wesn')

        rotulosenha = Label(janela, text='Senha', font='Verdana 18')
        rotulosenha.grid(row=2, column=0, sticky='wesn')

        #campos
        campo1 = Entry(janela, text='E-mail', font='Verdana 18')
        campo1.grid(row=1, column=1, columnspan=3, sticky='wesn')
        campo1.focus_force()
        self.campo1 = campo1

        campo2 = Entry(janela, text='Senha', font='Verdana 18', show='☠') #adicionei o show com caveiras
        campo2.grid(row=2, column=1, columnspan=3, sticky='wesn')
        self.campo2 = campo2

        botao1 = Button(janela, text='Conectar', font='Verdana 18', command=self.botaoconectar)
        botao1.grid(row=3, column=0, columnspan=2, sticky='wesn')

        botao2 = Button(janela, text='Fechar', font='Verdana 18', command=self.botaosair)
        botao2.grid(row=3, column=2, columnspan=2, sticky='wesn')

        centralizar_janela(janela)
        janela.mainloop()
class JanelaProduto:
    def __init__(self):
        self.banco = BancoProduto('localhost','root', '2106', 'ap2')
        janela = Tk()
        janela.title('CRUD - Produtos')
        janela.rowconfigure(6)
        janela.columnconfigure(4)
        fonte = 'Helvetica 14'

        rotulo = Label(janela, font=fonte, text='Digite o termo procurado:')
        rotulo.grid(row=0, column=0, columnspan=2, sticky='wesn')

        campo = Entry(janela, font=fonte)
        campo.grid(row=0, column=2, columnspan=2, sticky="wesn")
        campo.bind("<KeyRelease>", self.atualizar_produtos)
        self.campo = campo

        rotulo = Label(janela, font=fonte,
                       text='CADASTRO DE PRODUTOS',
                       bg='darkblue',fg='white')
        rotulo.grid(row=1, column=0, columnspan=4, sticky='wesn')

        frame = Frame(janela)
        frame.grid(row=2, column=0, columnspan=4, rowspan=3, sticky='wesn')
        frame.columnconfigure(2)
        frame.rowconfigure(1)

        # selecionador = 'browse' (somente uma linha pode ser selecionada)
        # show = 'headings'
        tabela = Treeview(frame, selectmode='browse',
                          columns=['nome', 'categoria', 'preco', 'estoque'],
                          show='headings')
        tabela.grid(row=0, column=0, sticky='wesn')
        tabela.heading('nome',text='Nome')
        tabela.heading('categoria', text='Categoria')
        tabela.heading('preco', text='Preço Unit.')
        tabela.heading('estoque', text='Estoque')
        tabela.selection()
        #tabela.grid(row=2, column=0, columnspan=4, rowspan=3, sticky='wesn')
        #incementando mais elementos no CRUD
        produtos = self.banco.obter_produtos()
        for produto in produtos:
            tabela.insert('','end', values=produto)

        # cria a barra de rolagem e define o comportamento da barra
        barra = Scrollbar(frame, orient='vertical', command=tabela.yview)
        barra.grid(row=0, column=1, sticky="wesn")
        # configura o comportamento da barra quando a tabela se movimento
        tabela.configure(yscrollcommand=barra.set)
        self.tabela = tabela

        botao = Button(janela, font=fonte, text='Novo')
        botao.grid(row=5, column=0, sticky='wesn')

        botao = Button(janela, font=fonte, text='Alterar')
        botao.grid(row=5, column=1, sticky='wesn')

        botao = Button(janela, font=fonte, text='Apagar', command=self.apagar_produtos)
        botao.grid(row=5, column=2, sticky='wesn')

        botao = Button(janela, font=fonte, text='Fechar')
        botao.grid(row=5, column=3, sticky='wesn')

    def apagar_produtos(self):
        print('botão clicado!')
        selecao = self.tabela.selection()
        if len(selecao) == 0:
            showerror(title='Apagar Produto', message='Selecione um produto para apagar')
        else:
            print(selecao)
            print(selecao[0])
            valores = self.tabela.item(selecao[0], 'values')
            cod_produtos = valores[-1]
            self.banco.apagar_produto(cod_produtos)
            self.atualizar_produtos()
            showinfo(title='Sucesso', message='Produto Apagado!')
    def atualizar_produtos(self, event=None):
        termo = self.campo.get()
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        registros = self.banco.obter_produtos(termo)
        for registro in registros:
            self.tabela.insert('', 'end', values=registro)
class BancoProduto:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def obter_conexao(self):
        return connect(host = self.host, user = self.user, password = self.password, database = self.database)
    def obter_produtos(self, termo = ''):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        sql = """
            select produto.nome, categoria.nome as nome_categoria, format(preco, 2, 'pt_BR') preco, estoque, produto.codigo from produto, categoria
            where produto.codigo_categoria = categoria.codigo and (produto.nome like %s or categoria.nome like %s) order by 1
        """
        termo = "%" + termo + "%"
        cursor.execute(sql, [termo, termo])
        resultado = cursor.fetchall()
        conexao.close()
        return resultado
    def apagar_produto(self, codigo):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        sql = "delete from produto where codigo = %s"
        cursor.execute(sql, [codigo])
        conexao.commit()
        conexao.close()

class JanelaFormulario:
    def __init__(self):
        janela = Tk()
        janela.title('A definir :)')
        janela.rowconfigure(4)
        janela.columnconfigure(4)

        campo1 = Label(janela, text='Nome:', font='Helvetica')
        campo1.grid(row=0, column=0, sticky='wesn')
        campo2 = Label(janela, text='Categoria:', font='Helvetica')
        campo2.grid(row=1, column=0, sticky='wesn')
        campo3 = Label(janela, text='Estoque:', font='Helvetica')
        campo3.grid(row=2, column=0, sticky='wesn')
        campo4 = Label(janela, text='Preço Unit.:', font='Helvetica')
        campo4.grid(row=3, column=0, sticky='wesn')

        campo1 = Entry(janela, text='Nome', font='Verdana 18')
        campo1.grid(row=0, column=1, columnspan=3, sticky='wesn')

        campo2 = Combobox(janela, values=['x','y','z'], font='Verdana 18')
        campo2.grid(row=1, column=1, columnspan=3, sticky='wesn')

        campo3 = Spinbox(janela, text='Estoque', font='Verdana 18', from_=0, to='inf')
        campo3.grid(row=2, column=1, columnspan=3, sticky='wesn')

        campo4 = Entry(janela, text='Preço Unit.:', font='Verdana 18')
        campo4.grid(row=3, column=1, columnspan=3, sticky='wesn')

        btn_salvar = Button(janela, text='Salvar', font='Verdana 18')
        btn_salvar.grid(row=4, column=0, columnspan=2,sticky='wesn')

        btn_cancelar = Button(janela, text='Cancelar', font='Verdana 18')
        btn_cancelar.grid(row=4, column=2, columnspan=2,sticky='wesn')

janelaLogin = JanelaLogin()