import Controller
import os.path

def criaArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")

criaArquivos("categoria.txt", "clientes.txt", "estoque.txt", "fornecedores.txt", "funcionarios.txt", "venda.txt")

if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar ( Categorias )\n"
                           "Digite 2 para acessar ( Estoque )\n"
                           "Digite 3 para acessar ( Fornecedor )\n"
                           "Digite 4 para acessr ( Cliente )\n"
                           "Digite 5 para acessar ( Funcionários )\n"
                           "Digite 6 para acessar ( Vendas )\n"
                           "Digite 7 para ver os produtos mais vendidos\n"
                           "Digite 8 para sair\n"))

        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma nova categoria\n"
                                   "Digite 2 para remover uma categoria\n"
                                   "Digite 3 para alterar uma categoria\n"
                                   "Digite 4 para mostrar as categorias cadastradas\n"
                                   "Digite 5 para sair\n"))

                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar\n")
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que deseja remover\n")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input("Digite a categoria que deseja alterar\n")
                    novacat = input("Digite o nome da nova categoria\n")
                    cat.alterarCategoria(categoria, novacat)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break
        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = input("Digite 1 para cadastrar um produto\n"
                                "Digite 2 para remover um produto\n"
                                "Digite 3 para alterar um produto\n"
                                "Digite 4 para ver os produtos cadastrados\n"
                                "Digite 5 para sair\n")
                if decidir == 1:
                    nome = input("Digite um nome de um produto\n")
                    preco = input("Digite o preco do produto\n")
                    categoria = input("Digite a categoria do produto\n")
                    quantidade = input("Digite a quantidade do produto\n")
                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input("Digite o nome do produto que deseja remover\n")
                    cat.removerProduto(produto)
                elif decidir == 3:
                    produto = input("Digite ou informe o produto que deseja alterar\n")
                    novoprod = input("Digite o nome do novo produto\n")
                    categoria = input("Digite o categoria do produto\n")
                    preco = input("Digite o preco do produto\n")
                    qntd = input("Digite a quantidade do produto\n")
                    cat.alterarProduto(produto, novoprod, categoria, preco, qntd)
                elif decidir == 4:
                    cat.mostrarEstoque()
                else:
                    break

        elif local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = input("Digite 1 para cadastrar um fornecedor\n"
                                "Digite 2 para remover um fornecedor\n"
                                "Digite 3 para alterar um fornecedor\n"
                                "Digite 4 para ver os fornecedores cadastrados\n"
                                "Digite 5 para sair\n")
                if decidir == 1:
                    nome = input("Digite o nome do fornecedor\n")
                    cnpj = input("Digite o CNPJ do fornecedor\n")
                    telefone = input("Digite o telefone do fornecedor\n")
                    categoria = input("Digite a categoria do fornecedor\n")
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    forn = input("Digite ou informe o fornecedor que deseja remover\n")
                    cat.removerFornecedor(forn)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome que será alterado\n")
                    novoNome = input("Digite o novo nome do fornecedor\n")
                    novoCnpj = input("Digite o novo CNPJ do fornecedor\n")
                    novoTelefone = input("Digite o novo telefone do fornecedor\n")
                    novaCategoria = input("Digite a nova categoria do fornecedor\n")
                    cat.alterarFornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria)
                elif decidir == 4:
                    cat.mostrarFornecedor()
                else:
                    break
        elif local == 4:
            cat = Controller.ControllerCliente()
            while True:
                decidir = input("Digite 1 para cadastrar um cliente\n"
                                "Digite 2 para remover um cliente\n"
                                "Digite 3 para alterar um cliente\n"
                                "Digite 4 para ver os clientes cadastrados\n"
                                "Digite 5 para sair\n")
                if decidir == 1:
                    nome = input("Digite o nome do cliente\n")
                    cpf = input("Digite o CPF do cliente\n")
                    telefone = input("Digite o telefone do cliente\n")
                    email = input("Digite o E-mail do cliente\n")
                    endereco = input("Digite o endereço do cliente\n")
                    cat.cadastrarCliente(nome, cpf, telefone, email, endereco)
                elif decidir == 2:
                    client = input("Digite o cliente que deseja remover\n")
                    cat.removerCliente(client)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome que será alterado\n")
                    novoNome = input("Digite o novo nome do cliente\n")
                    novoCpf = input("Digite o novo CPF do cliente\n")
                    novoTelefone = input("Digite o novo telefone do cliente\n")
                    novoEmail = input("Digite a novo E-mail do cliente\n")
                    novoEndereco = input("Digite o novo endereco do cliente\n")
                    cat.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cat.mostrarCliente()
                else:
                    break

        elif local == 5:
            cat = Controller.ControllerFuncionario()
            while True:
                decidir = input("Digite 1 para cadastrar um funcionario\n"
                                "Digite 2 para remover um funcionario\n"
                                "Digite 3 para alterar um funcionario\n"
                                "Digite 4 para ver os funcionarios cadastrados\n"
                                "Digite 5 para sair\n")
                if decidir == 1:
                    nome = input("Digite o nome do funcionario\n")
                    cpf = input("Digite o CPF do funcionario\n")
                    telefone = input("Digite o telefone do funcionario\n")
                    email = input("Digite o E-mail do funcionario\n")
                    endereco = input("Digite o endereço do funcionario\n")
                    clt = input("Digite a CLT do funcionario\n")
                    cat.cadastrarFuncionario(nome, cpf, telefone, email, endereco, clt)
                elif decidir == 2:
                    funcio = input("Digite o funcionario que deseja remover\n")
                    cat.removerFuncionario(funcio)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome que será alterado\n")
                    novoNome = input("Digite o novo nome do funcionario\n")
                    novoCpf = input("Digite o novo CPF do funcionario\n")
                    novoTelefone = input("Digite o novo telefone do funcionario\n")
                    novoEmail = input("Digite a novo E-mail do funcionario\n")
                    novoEndereco = input("Digite o novo endereco do funcionario\n")
                    novaClt = input("Digite a nva CLT do funcionario")
                    cat.alterarFuncionario(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco, novaClt)
                elif decidir == 4:
                    cat.mostrarFuncionario()
                else:
                    break

        elif local == 6:
            cat = Controller.ControllerVenda()
            while True:
                decidir = input("Digite 1 para cadastrar uma venda\n"
                                "Digite 2 para ver o relatorio de vendas\n"
                                "Digite 3 para sair\n")
                if decidir == 1:
                    nome = input("Digite o nome do produto a ser adquirido\n")
                    vendedor = input("Digite o nome do vendedor\n")
                    comprador = input("Digite o nome do comprador\n")
                    qntd = input("Digite a quantidade comprada\n")
                    cat.cadastrarVenda(nome, vendedor, comprador, qntd)
                elif decidir == 2:
                    datainicial = input("Digite a data inicial no formato dia/ mes/ ano: \n")
                    datafinal = input("Digite a data final no formato dia/ mes/ ano:\n")
                    cat.mostrarVendas(datainicial, datafinal)
                else:
                    break
        elif local == 7:
            a = Controller.ControllerVenda()
            a.relatorioProdutos()
        else:
            break
