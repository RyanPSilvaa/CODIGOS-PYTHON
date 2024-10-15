import sys
from tkinter import Tk, Label, Entry, Button, Frame, Scrollbar
from tkinter.messagebox import showinfo, showerror
from tkinter.ttk import Treeview
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


class BancoLogin: # um objeto criado para cada janela
    def _init_(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def obter_conexao(self):
        return connect(host = self.host, user = self.user, password = self.password, database = self.database)
    def login_ok(self, email, senha):
        # esta consulta precisa ser alterada para funcionar
        # com o método de criptografia escolhido
        sql = "select nome from usuario where email=%s and senha=SHA2(%s, 256)"
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
    def clique_botao2(self):
        sys.exit(0)

    def clique_botao1(self):
        usuario = self.campo1.get()
        senha = self.campo2.get()
        print(usuario, senha)
        nome = self.banco.login_ok(usuario, senha)
        if nome is not None:
            showinfo(title="Sucesso", message="Seja bem-vindo(a), " + nome + ".")
            self.janela.destroy() # fecha a janela de login
            JanelaProduto() # abre a janela do CRUD de produtos
        else:
            showerror(title="Acesso negado",
                message="Não foi encontrado um usuário com este e-mail e senha.")

    def _init_(self):
        self.banco = BancoLogin("localhost", "user1405", "poo", "aula0406")

        janela = Tk()
        self.janela = janela
        janela.title('Login')
        janela.rowconfigure(4)
        janela.columnconfigure(4)

        rotulo1 = Label(janela,
                       text="AUTENTICAÇÃO DE USUÁRIO",
                       font="Verdana 18 bold",
                       fg="white", # cor da letra
                       bg="darkblue")
        rotulo1.grid(row=0, column=0, columnspan=4, sticky="wesn")

        rotulo2 = Label(janela, text="E-mail:", font="Verdana 18")
        rotulo2.grid(row=1, column=0, sticky="wesn")

        rotulo3 = Label(janela, text="Senha:", font="Verdana 18")
        rotulo3.grid(row=2, column=0, sticky="wesn")

        # campo de e-mail
        campo1 = Entry(janela, font="Verdana 18")
        campo1.grid(row=1, column=1, columnspan=3, sticky="wesn")
        campo1.focus_force()
        self.campo1 = campo1

        # campo de senha
        campo2 = Entry(janela, font="Verdana 18", show="☠")
        campo2.grid(row=2, column=1, columnspan=3, sticky="wesn")
        self.campo2 = campo2

        # botões
        botao1 = Button(janela, text="Conectar", font="Verdana 18", bg="gray", command=self.clique_botao1)
        botao1.grid(row=3, column=0, columnspan=2, sticky="wesn")

        botao2 = Button(janela, text="Cadastrar",font="Verdana 18", bg="gray", command=self.clique_botao1)
        botao2.grid(row=3, column=1, columnspan=2, sticky="wesn")

        botao3 = Button(janela,
                        text="Fechar",
                        font="Verdana 18",
                        bg="gray",
                        command=self.clique_botao2
                        )
        botao3.grid(row=3, column=2, columnspan=2, sticky="wesn")
        centralizar_janela(janela)
        janela.mainloop()

class JanelaProduto:
    def _init_(self):
        self.banco = BancoProduto("localhost", "user1405", "poo", "aula1405")
        janela = Tk()
        janela.title("CRUD - Produtos")
        janela.rowconfigure(6)
        janela.columnconfigure(4)
        fonte = "Helvetica 14"

        rotulo = Label(janela, font=fonte, text="Digite o termo procurado:")
        rotulo.grid(row=0, column=0, columnspan=2, sticky="wesn")

        campo = Entry(janela, font=fonte)
        campo.grid(row=0, column=2, columnspan=2, sticky="wesn")
        campo.bind("<KeyRelease>", self.atualizar_produtos)
        self.campo = campo

        rotulo = Label(janela, font=fonte,
                       text="CADASTRO DE PRODUTOS", bg="darkblue", fg="white")
        rotulo.grid(row=1, column=0, columnspan=4, sticky="wesn")

        frame = Frame(janela)
        frame.columnconfigure(2)
        frame.rowconfigure(1)
        # selectmode='browse' (somente uma linha pode ser selecionada)
        # show='headings' (exibe o rótulo das colunas no cabeçalho)
        tabela = Treeview(frame, selectmode="browse",
                          columns=["nome", "categoria", "preco",  "estoque"],
                          show='headings')
        tabela.grid(column=0, row=0, sticky="wesn")
        tabela.heading("nome", text="Nome")
        tabela.heading("categoria", text="Categoria")
        tabela.heading("preco", text="Preço Unit.")
        tabela.heading("estoque", text="Estoque")
        frame.grid(row=2, column=0, columnspan=4, rowspan=3, sticky="wesn")
        # ===========> PARAMOS AQUI <===============
        # Adicione 20 linhas de teste usando insert('', 'end', values=[])
        produtos = self.banco.obter_produtos()
        for produto in produtos:
            tabela.insert('', 'end', values=produto)

        # cria a barra e define o comportamento da tabela
        # quando os botões da barra forem clicados
        barra = Scrollbar(frame, orient='vertical', command=tabela.yview)
        barra.grid(row=0, column=1, sticky="wesn")
        # configura o comportamento da barra quando a tabela se movimento
        tabela.configure(yscrollcommand=barra.set)
        self.tabela = tabela

        botao = Button(janela, font=fonte, text="Novo")
        botao.grid(row=5, column=0, sticky="wesn")

        botao = Button(janela, font=fonte, text="Alterar")
        botao.grid(row=5, column=1, sticky="wesn")

        botao = Button(janela, font=fonte, text="Apagar")
        botao.grid(row=5, column=2, sticky="wesn")

        botao = Button(janela, font=fonte, text="Fechar")
        botao.grid(row=5, column=3, sticky="wesn")

        centralizar_janela(janela)
        janela.mainloop()
    def atualizar_produtos(self, event):
        termo = self.campo.get()
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        registros = self.banco.obter_produtos(termo)
        for registro in registros:
            self.tabela.insert('', 'end', values=registro)

class BancoProduto:
    def _init_(self, host, user, password, database):
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
            select produto.nome, categoria.nome as nome_categoria, format(preco_unitario, 2, 'pt_BR') preco, estoque, produto.codigo from produto, categoria
            where produto.cod_categoria = categoria.codigo and (produto.nome like %s or categoria.nome like %s) order by 1
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

janelaLogin = JanelaLogin()