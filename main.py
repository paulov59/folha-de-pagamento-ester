from funcionario import Funcionario
from folha import Folha

funcionarios = []

def setId():
    for i in funcionarios:
        i.id = funcionarios.index(i)

def listar():
    if funcionarios == []:
        print("\nAinda não há funcionários cadastrados")
    else:
        print("\nid - Nome")
        for i in funcionarios:
            print("%2d" %i.id + " - " + i.nome)

def opcoesFuncionario():
    print("\nOpções de funcionário:")
    print("""    1 - Adicionar funcionário
    2 - Remover funcionário
    3 - Lançamentos
    4 - Alterar dados
    5 - Listar funcionários
    6 - Voltar""")
    escolha = int(input("O que deseja?\n"))

    if escolha == 1:
        nome = input("Insira o nome: ")
        funcionario = Funcionario(nome)
        funcionario.adicionarFuncionario()
        funcionarios.append(funcionario)
        setId()
        opcoes()

    elif escolha == 2:
        listar()
        id = int(input("Insira o id do funcionário deseja demitir: "))
        funcionarios.pop(id)
        setId()
        opcoes()

    elif escolha == 3:
        listar()
        id = int(input("Insira o id do funcionário que fará o lançamento: "))
        print("""Insira o tipo de lançamento
        1 - Cartão de ponto
        2 - Venda
        3 - Serviço""")
        escolha = int(input())
        if escolha == 1:
            funcionarios[id].ponto()
        elif escolha == 2:
            funcionarios[id].venda()
        elif escolha == 3:
            funcionarios[id].servico()
        opcoes()

    elif escolha == 4:
        listar()
        id = int(input("Insira o id do funcionário desejado: "))
        funcionarios[id].alterarDados()
        opcoes()

    elif escolha == 5:
        listar()
        opcoes()

    elif escolha == 6:
        opcoes()
        
    else:
        print("Não entendi, vamos recomeçar o atendimento")
        opcoesFuncionario()

def opcoesFolha():
    print("\nOpções da folha:")
    print("""    1 - Gerar Folha de Pagamento\n
    2 - Agenda de pagamento\n
    3 - Criar nova agenda de pagamento
    4 - Voltar""")
    escolha = int(input("O que deseja?\n"))

    if escolha == 1:
        print("vamos rodar a folha")
        opcoes()
    elif escolha == 2:
        print("opçoes de agenda")
        opcoes()
    elif escolha == 3:
        print("criar nova agenda")
        opcoes()
    elif escolha == 4:
        opcoes()
    else:
        print("Não entendi, vamos recomeçar o atendimento")
        opcoesFolha()

def opcoes():
    print("\nMenu principal:")
    print("""    1 - Espaço funcionario
    2 - Folha de Pagamento
    3 - Sair""")
    escolha = int(input("O que deseja?\n"))

    if escolha == 1:
        opcoesFuncionario()
    elif escolha == 2:
        opcoesFolha()
    elif escolha == 3:
        print("Obrigada por utilizar nosso sistema, volte sempre!")
        return
    else:
        print("\nNão entendi, vamos recomeçar o atendimento")
        opcoes()

print("Seja bem-vindo ao sistema Folha de Pagamento")

def iniciar():
    funcionario = Funcionario("primeiro funcionario")
    funcionarios.append(funcionario)
    funcionario = Funcionario("segundo funcionario")
    funcionarios.append(funcionario)
    funcionario = Funcionario("terceiro funcionario")
    funcionarios.append(funcionario)
    funcionario = Funcionario("quarto funcionario")
    funcionarios.append(funcionario)
    funcionario = Funcionario("quinto funcionario")
    funcionarios.append(funcionario)
    setId()

iniciar()
opcoes()