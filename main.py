from trabalhador import Trabalhador
from folha import Folha

def opcoesFuncionario():
    print("\nOpções de funcionário:")
    print("""    1 - Adicionar funcionário
    2 - Lançamento
    3 - Remover funcionário
    4 - Voltar""")
    escolha = int(input("O que deseja?\n"))

    if escolha == 1:
        print("vamos add funcionario")
    elif escolha == 2:
        print("vamos fazer um lançamento")
    elif escolha == 3:
        print("vamos demitir")
    elif escolha == 4:
        opcoes()
    else:
        print("Não entendi, vamos recomeçar o atendimento")
        opcoesFuncionario()

def opcoesFolha():
    print("\nOpções da folha:")
    print("""    1- Gerar Folha de Pagamento\n
    2 - Agenda de pagamento\n
    3 - Criar nova agenda de pagamento
    4 - Voltar""")
    escolha = int(input("O que deseja?\n"))

    if escolha == 1:
        print("vamos rodar a folha")
    elif escolha == 2:
        print("opçoes de agenda")
    elif escolha == 3:
        print("criar nova agenda")
    elif escolha == 4:
        opcoes()
    else:
        print("Não entendi, vamos recomeçar o atendimento")
        opcoesFolha()

def opcoes():
    print("\nMenu principal:")
    print("""    1- Espaço funcionario
    2- Folha de Pagamento
    3- Sair""")
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
opcoes()
