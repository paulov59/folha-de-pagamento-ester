class Funcionario():
    nome = ''
    endereco = ''

    def __init__(self, nome):
        pass
        self.nome = nome


    def adicionarFuncionario(self):
        self.endereco = input("Insira o endereço: ")

        print("""Selecione o tipo de funcionário:
        1 - Horista
        2 - Assalariado
        3 - Comissionado""")
        escolha = int(input())
        while escolha > 3:
            escolha = int(input("Não entendi, escolha novamente: "))
        self.tipo_funcionario = escolha
        self.salario = 0
        if self.tipo_funcionario == 1:
            self.salario_por_hora = float(input("Insira o salário por hora trabalhada: "))
            self.tipo_pagamento = 1
        elif self.tipo_funcionario == 2:
            self.salario = float(input("Insira o salário: "))
            self.tipo_pagamento = 3
        else:
            self.taxa_comissao = float(input("Insira a taxa da comissão: "))
            self.tipo_pagamento = 2

        print("""Faz parte de sindicato:
        1 - Sim
        2 - Não""")
        escolha = int(input())
        while escolha > 2:
            escolha = int(input("Não entendi, escolha novamente: "))
        if escolha == 1:
            self.sindicato = True
            self.taxa_sindicato = float(input("Insira a taxa sindical: "))
        else:
            self.sindicato = False
            self.taxa_sindicato = 0
        
    def ponto(self):
        if self.tipo_funcionario == 1:
            horas = int(input("Insira a quantidade de horas trabalhadas: "))
            if horas > 8:
                extra = (horas-8) * self.salario_por_hora * 1.5
                self.salario += (8 * self.salario_por_hora) + extra
            else :
                self.salario += horas * self.salario_por_hora
            print("Horas cadastradas com sucesso!")
        else:
            print("Esse funcionário não pode submeter cartão de ponto")
            return

    def venda(self):
        if self.tipo_funcionario == 3:
            valor = float(input("Insira o valor da venda realizada: "))
            self.salario += valor * self.taxa_comissao
            print("Venda cadastradas com sucesso!")
        else:
            print("Esse funcionário não pode submeter venda")
            return

    def servico(self):
        if self.sindicato:
            valor = float(input("Insira a taxa do serviço sindical: "))
            self.salario -= valor
            print("Serviço sindical cadastrado com sucesso!")
        else:
            print("Esse funcionário não pertence ao sindicato")
            return

    def alterarDados(self):
        print("\nOpções de alteração:")
        print("""    1 - Nome
        2 - Endereço
        3 - Tipo de funcionário
        4 - Salário/taxa de comissão
        5 - Opções do sindicato""")
        escolha = int(input("O que deseja?\n"))
        
        if escolha == 1:
            self.nome = input("Insira o novo nome: ")
        
        elif escolha == 2:
            self.endereco = input("Insira o novo endereço: ")
        
        elif escolha == 3:
            print("""Selecione o novo tipo de funcionário:
        1 - Horista
        2 - Assalariado
        3 - Comissionado""")
            escolha = int(input())
            while escolha > 3:
                escolha = int(input("Não entendi, escolha novamente: "))
            self.tipo_funcionario = escolha
            if self.tipo_funcionario == 1:
                self.salario_por_hora = float(input("Insira o salário por hora trabalhada: "))
                self.tipo_pagamento = 1
            elif self.tipo_funcionario == 2:
                self.salario = float(input("Insira o salário: "))
                self.tipo_pagamento = 3
            else:
                self.taxa_comissao = float(input("Insira a taxa da comissão: "))
                self.tipo_pagamento = 2
        
        elif escolha == 4:
            if self.tipo_funcionario == 1:
                self.salario_por_hora = float(input("Insira o novo salário por hora: "))
            elif self.tipo_funcionario == 2:
                self.salario = float(input("Insira o novo salário: "))
            else:
                self.taxa_comissao = float(input("Insira a nova taxa da comissão: "))
        
        elif escolha == 5:
            print("\nOpções de sindicato:")
            print("""    1 - Alterar participação
        2 - Alterar valor""")
            escolha = int(input("O que deseja?\n"))
            if escolha == 1:
                if self.sindicato == True:
                    self.sindicato = False
                    self.taxa_sindicato = 0
                else:
                    self.sindicato = True
                    self.taxa = float(input("Insira a taxa sindical: "))
            else:
                if self.sindicato == True:
                    self.taxa = float(input("Insira a nova taxa sindical: "))
                else:
                    print("Esse funcionário não pertence ao sindicato")
                    return
        print("Alterações realizadas com sucesso!")
