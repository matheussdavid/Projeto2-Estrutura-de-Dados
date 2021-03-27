valorMenu = 9999
while valorMenu != 0:
    print('--------------------- SysJurídico v12.01 -----------------------------')
    print('----------------------------- MENU -----------------------------------\n')
    print('1 - Impressão teste')
    print('2 - Listar os advogados')
    print('3 - Listar os custos processuais de uma pessoa')
    print('4 - Listar os custos processuais de uma pessoa de acordo com o advogado')
    print('0 - Sair do Sistema')
    print('----------------------------------------------------------------------\n')
    valorMenu = int(input('Informe o número corresponde ao que deseja realizar: '))
    if valorMenu == 1:
        print("Teste")
        valorMenu = int(input('Deseja voltar ao menu? Digite 1 para voltar ao Menu e 0 para encerrar: '))
    elif valorMenu == 2 :
        cod_adv = input('Informe o código do advogado (Ex: OAB-DF 222.222): ')
        adv = encontra_adv(cod_adv)
        print(adv.lista_clientes())
    elif valorMenu == 3 :
        cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
        pessoa = encontra_pessoa(cpf)
        print(pessoa.custo_total())
    elif valorMenu == 4 :
        cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
        cod_adv = input('Informe o código do advogado (Ex: OAB-DF 222.222): ')
        pessoa = encontra_pessoa(cpf)
        adv = encontra_adv(cod_adv)
        print(pessoa.custo_total_adv(adv.get_cod_oab()))
    elif valorMenu == 0 :
        print('\n\nFinalizando o sistema! Até mais')
        print('SysJurídico v12.00\n\n')
        valorMenu = 0
    else:
        print('Erro! O valor informado é inválido !!! Tente outra vez\n')

