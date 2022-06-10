from Models import Categoria, Estoque, Produto, Fornecedor, Pessoa, Funcionario, Venda
from DAO import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("Categoria cadastrada com sucesso!")

        else:
            print("A categoria que deseja cadastrar já existe!")

    def removerCategoria(self, categoriaRevomer):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRevomer, x))

        if len(cat) <= 0:
            print("A categoria que deseja remover não existe!")
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRevomer:
                    del x[i]
                    break
            print("Categoria removida com sucesso!")
            with open ("categoria.txt", 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, "Sem categoria"), x.quantidade)
                           if(x.produto.categoria == categoriaRevomer) else (x), estoque))

        with open("estoque.txt", 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines("\n")

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria == categoriaAlterar) else (x), x))
                print("Categoria alterada com sucesso!")

                estoque = DaoEstoque.ler()
                estoque = list(
                    map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade)
                    if (x.produto.categoria == categoriaAlterar) else (x), estoque))

                with open("estoque.txt", 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(
                            i.quantidade))
                        arq.writelines("\n")

            else:
                print("A categoria para qual deseja alterar já existe!")
        else:
            print("A categoria que deseja alterar não existe!")

        with open ("categoria.txt", 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print("Categorias vazias ou inexistentes!")
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))

        if len(h) >0:
            estoque = list(filter(lambda x: x.produto.nome == nome, x))
            if len(estoque) == 0:
                produto = Produto(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print("Produto cadastrado com sucesso!")
            else:
                print("O produto já está cadastrado no estoque")

        else:
            print("Categoria inexistente")

    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print("Produto removido com sucesso")
        else:
            print("O produto que deseja remover não existe")

        with open("estoque.txt", 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" +
                               str(i.quantidade))
                arq.writelines("\n")

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produto(novoNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), x))
                    print("Produto alterado com sucesso!")
                else:
                    print("Produto já cadastrado")
            else:
                print("O produto que deseja alterar não existe")

            with open("estoque.txt", 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" +
                                   str(i.quantidade))
                    arq.writelines("\n")

        else:
            print("A categoria informada não existe!")

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print("Estoque vazio")
        else:
            for i in estoque:
                print("==========Produtos==========")
                print(f"Nome: {i.produto.nome}\n"
                      f"Preco: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}")
                print("--------------------")

class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        '''
        return 1: Produto não existe
        return 2: Quantidade vendida não contem em estoque
        return 3: Venda efetuada com sucesso!

        :param nomeProduto: Nome do produto a ser vendido
        :param vendedor: Nome de quem realizou a venda do produto
        :param comprador: Nome de quem relizou a compra do produto
        :param quantidadeVendida: informe a quantidade de produtos vendidos
        :return:
        '''
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)
            temp.append([Produto(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        arq = open("estoque.txt", 'w')
        arq.writelines("")

        for i in temp:
            with open("estoque.txt", 'a') as arq:
                arq.writelines(i[0].nome + "|" + i[0].preco + "|" + i[0].categoria + "|" + str(i[1]))
                arq.writelines("\n")

        if existe == False:
            print("O produto não existe")
            return None
        elif not quantidade:
            print("A quantidade vendida não contem em estoque")
            return None
        else:
            print("Venda realizada com sucesso!")
            return valorCompra

    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendidos.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto' : nome, 'quantidade' : int(x['quantidade']) + int(quantidade)}
                if (x['produto'] == nome) else (x), produtos))
            else:
                produtos.append({'produto' : nome, 'quantidade' : int(quantidade)})

        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse = True)

        print("Esses são os produtos mais vendidos")
        a = 1
        for i in ordenado:
            print(f"==========Produtos [{a}]==========")
            print(f"Produto: {i['produto']}\n"
                  f"Quantidade: {i['quantidade']}\n")
            a += 1

    def mostrarVendas(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%y') >= dataInicio1 and datetime.strptime(x.data, '%d/%m/%y') <= dataTermino1, vendas ))

        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(F"==========Venda [{cont}]==========")
            print(f"Nome: {i.itensVendidos.nome}\n"
                  f"Categoria: {i.itensVendidos.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade: {i.quantidadeVendida}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}")
            total += int(i.itensVendidos.preco) * int(i.quantidadeVendida)
            cont += 1
        print(f"Total venddo: {total}")

class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.cnpj == cnpj, x))
        if len(listaCnpj) > 0:
            print("O CNPJ informado já existe!")
        elif len(listaTelefone) > 0:
            print(" O telefone informado já existe")
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >=10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print("Digite um CNPJ ou telefone válido")

    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if (x.nome == nomeAlterar) else(x), x))
            else:
                print("CNPJ já existente!")
        else:
            print("O fornecedor que deseja alterar não existe")

        with open("fornecedores.txt", 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines("\n")
                print("Fornecedor alterado com sucesso!")

    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("O fornecedor que deseja remover não exite!")
            return None

        with open("fornecedores.txt", 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines("\n")
            print("Fornecedor removido com sucesso!")

    def mostrarFornecedor(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print("Lista de fornecedores está vazia")

        for i in fornecedores:
            print("==========Fornecedores==========")
            print(f"Categoria fornecida: {i.categoria}\n"
                  f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}"
                  f"CNPJ: {i.cnpj}")

class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print("O CPF informado já existe!")
        else:
            if len(cpf) == 11 and len(telefone) == 10 and len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print("Cliente cadastrado com sucesso!")
            else:
                print("Digite um CPF ou telefone válido")

    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if (x.nome == nomeAlterar) else(x), x))
        else:
            print("O cliente que deseja alterar não existe")

        with open("clientes.txt", 'w') as arq:
            for i in x :
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")
            print("Cliente alterado com sucesso!")

    def removerCliente(self, nome):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("O cliente que deseja remover não existe")
            return None
        with open("clientes.txt", 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")
            print("Cliente removido com sucesso!")

    def mostrarCliente(self):
        clientes = DaoPessoa.ler()

        if len(clientes) == 0:
            print("Lista de clientes está vazia")

        for i in clientes:
            print("==========Clientes==========")
            print(f"Nome:: {i.nome}\n"
                  f"CPF: {i.cpf}\n"
                  f"Telefone: {i.telefone}"
                  f"Email: {i.email}\n"
                  f"Endereco: {i.endereco}")

class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))
        if len(listaCpf) > 0:
            print("O CPF informado já existe!")
        elif len(listaClt) > 0:
            print("Já existe um colaborador com essa CLT")
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print("Funcionário cadastrado com sucesso!")
            else:
                print("Digite um CPF ou telefone válido")

    def alterarFuncionario(self, nomeAlterar, novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
            if (x.nome == nomeAlterar) else (x), x))
        else:
            print("O funcionário que deseja alterar não existe")
        with open("funcionarios.txt", 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")
            print("Funcionário alterado com sucesso!")

    def removerFuncionario(self,nome):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("O funcionário que deseja remover não existe")
            return None
        with open("funcionarios.txt", 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")
            print("Funcionário removido com sucesso!")

    def mostrarFuncionario(self):
        funcionario = DaoFuncionario.ler()

        if len(funcionario) == 0:
            print("Lista de clientes está vazia")

        for i in funcionario:
            print("==========Clientes==========")
            print(f"Nome:: {i.nome}\n"
                  f"CPF: {i.cpf}\n"
                  f"Telefone: {i.telefone}"
                  f"Email: {i.email}\n"
                  f"Endereco: {i.endereco}\n"
                  f"CLT: {i.clt}")