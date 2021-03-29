from Processo import *
from Feeders import *
from Fila import Fila
from Pilha import Pilha
from Lista import Lista

def cria_processo():
    print("Informe os dados do processo a ser inserido")
    descricao  = input('Informe a descrição do processo: ')
    custo  = int(input('Informe a custo do processo: '))
    decisao  = input('Informe a decisão do processo: ')
    status  = input('Informe o status do processo: ')
    cod  = input('Informe o código do processo: ')
    processo = Processo(descricao, custo, decisao, status, cod)
    return processo

valorMenu = 9999
while valorMenu != 0:
    print('--------------------- SysJurídico v12.01 -----------------------------')
    print('----------------------------- MENU -----------------------------------\n')
    print('1 - Advogados')
    print('2 - Listar todos os processos')
    print('3 - Processos Penais (ProcessosP)')
    print('4 - Processos Trabalhistas (ProcessosF)')
    print('5 - Processos Cíveis (ProcessosL)')
    print('0 - Sair do Sistema')
    print('----------------------------------------------------------------------\n')
    valorMenu = int(input('Informe o número corresponde ao que deseja realizar: '))
    if valorMenu == 1:
        print(advogado1)
        valorMenu = int(input('Deseja voltar ao menu? Digite 1 para voltar ao Menu e 0 para encerrar: '))
    elif valorMenu == 2 :
        print('\n Processos PENAIS \n')
        print(advogado1.get_processosP().imprimir())
        print('\n\n Processos TRABALHISTAS \n')
        print(advogado1.get_processosF().imprimir())
        # print('\n\n Processos TRABALHISTAS \n')
        # print(advogado1.get_processosF().imprimir())
        valorMenu = int(input('Deseja voltar ao menu? Digite 1 para voltar ao Menu e 0 para encerrar: '))
    elif valorMenu == 3 :
        while valorMenu == 3:
            print('\n Processos PENAIS \n')
            print('1 - Listar Processos')
            print('2 - Adicionar Processo')
            print('3 - Remover Processo')
            print('4 - Quantidade de Processos')
            print('5 - Sair')

            valorProcessoP = int(input('Informe o número corresponde ao que deseja realizar: '))
            
            if valorProcessoP == 1:
                print(advogado1.get_processosP().imprimir())
            
            elif valorProcessoP == 2:
                processo = cria_processo()
                advogado1.adicionar_processo_P(processo)
                print(advogado1.get_processosP().imprimir())
            
            elif valorProcessoP == 3:
                advogado1.remover_processo_P()
                print(advogado1.get_processosP().imprimir())

            elif valorProcessoP == 4:
                
                print(f'\nTamanho: {advogado1.get_processosP().tamanho()}')
            
            elif valorProcessoP == 5:
                valorMenu = 9999

    elif valorMenu == 4 :
        while valorMenu == 4:
            print('\n Processos TRABALHISTA \n')
            print('1 - Listar Processos')
            print('2 - Adicionar Processo')
            print('3 - Remover Processo')
            print('4 - Quantidade de Processos')
            print('5 - Sair')

            valorProcessoF = int(input('Informe o número corresponde ao que deseja realizar: '))
            
            if valorProcessoF == 1:
                print(advogado1.get_processosF().imprimir())
            
            elif valorProcessoF == 2:
                processo = cria_processo()
                advogado1.adicionar_processo_F(processo)
            
            elif valorProcessoF == 3:
                advogado1.remover_processo_F()
                print(advogado1.get_processosF().imprimir())

            elif valorProcessoF == 4:
                print(f'\nTamanho: {advogado1.get_processosF().tamanho()}')

            elif valorProcessoF == 5:
                valorMenu = 9999

    elif valorMenu == 5 :
        while valorMenu == 5:
            print('\n Processos Cíveis \n')
            print('1 - Listar Processo')
            print('2 - Adicionar Processo')
            print('3 - Remover Processo')
            print('4 - Quantidade de Processos')
            print('5 - Maior Custo')
            print('6 - Menor Custo')
            print('7 - Incrementar Custo do Processo')
            print('8 - Busca Processo')
            print('9 - Ordena Processo')
            print('10 - Imprime Processos')
            print('9999 - Sair')

            valorProcessoL = int(input('Informe o número corresponde ao que deseja realizar: '))
            
            if valorProcessoL == 1:
                print(advogado1.get_processosL().imprimir())
            
            elif valorProcessoL == 2:
                processo = cria_processo()
                posicao = int(input('Informe o número da posição que deseja adicionar o processo: '))
                advogado1.adicionar_processo_L(processo, posicao)

            
            elif valorProcessoL == 3:
                posicao = int(input('Informe o número da posição que deseja remover o processo: '))
                advogado1.get_processosL().remover(posicao)

            elif valorProcessoL == 4:
                print(f'\nTamanho: {advogado1.get_processosL().tamanho()}')

            elif valorProcessoL == 5:
                print('')
                print(advogado1.maior_custo())

            elif valorProcessoL == 6:
                print('')
                print(advogado1.menor_custo())
            
            elif valorProcessoL == 7:
                cod = input('Informe o código do processo que deseja aumentar o custo: ')
                valor = int(input('Informe o valor que deseja acrescer no custo do processo: R$ '))
                advogado1.incrementa_custo_processo(cod, valor)
            
            elif valorProcessoL == 8:
                cod = input('Informe o código do processo que deseja buscar: ')
                print('')
                print(advogado1.busca_processo(cod))
            
            elif valorProcessoL == 9:
                
                print(advogado1.ordena_processos())

            elif valorProcessoL == 10:
                print('')
                print(advogado1.imprimir_processos())

            elif valorProcessoL == 9999:
                valorMenu = 9999

    elif valorMenu == 0 :
        print('\n\nFinalizando o sistema! Até mais')
        print('SysJurídico v12.00\n\n')
        valorMenu = 0
    else:
        print('Erro! O valor informado é inválido !!! Tente outra vez\n')

