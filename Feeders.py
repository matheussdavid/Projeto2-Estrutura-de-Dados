from Advogado import Advogado
from Processo import Processo
from Fila import Fila
from Lista import Lista
from Pilha import Pilha


advogado1 = Advogado('1234-000')


# (self, descricao, custo, decisao, status, cod):

#Processos Pilhas
processoP1 = Processo('Penal', 1000, 'Deferido', 'Transitado em Julgado', '001')
processoP2 = Processo('Penal', 2000, 'Indeferido', 'Prazo para Recurso', '002')
processoP3 = Processo('Penal', 3000, 'Deferido', 'Embargos declaratórios','003')
processoP4 = Processo('Penal', 4000, 'Indeferido', 'Arquivado', '004')
processoP5 = Processo('Penal', 5000, 'Deferido', 'Em execução', '005')
processoP6 = Processo('Penal', 6000, 'Indeferido', 'Prazo para Recurso', '006')
processoP7 = Processo('Penal', 7000, 'Deferido', 'Em execução', '007')
processoP8 = Processo('Penal', 8000, 'Indeferido', 'Transitado em Julgado', '008')
processoP9 = Processo('Penal', 9000, 'Deferido', 'Arquivado', '009')
processoP0 = Processo('Penal', 1500, 'Indeferido', 'Arquivado', '010')

#Processos Fila
processoF1 = Processo('Trabalhista', 1000, 'Deferido', 'Transitado em Julgado', '011')
processoF2 = Processo('Trabalhista', 2000, 'Indeferido', 'Prazo para Recurso', '012')
processoF3 = Processo('Trabalhista', 3000, 'Deferido', 'Embargos declaratórios','013')
processoF4 = Processo('Trabalhista', 4000, 'Indeferido', 'Arquivado', '014')
processoF5 = Processo('Trabalhista', 5000, 'Deferido', 'Em execução', '015')
processoF6 = Processo('Trabalhista', 6000, 'Indeferido', 'Prazo para Recurso', '016')
processoF7 = Processo('Trabalhista', 7000, 'Deferido', 'Em execução', '017')
processoF8 = Processo('Trabalhista', 8000, 'Indeferido', 'Transitado em Julgado', '018')
processoF9 = Processo('Trabalhista', 9000, 'Deferido', 'Arquivado', '019')
processoF0 = Processo('Trabalhista', 1500, 'Indeferido', 'Arquivado', '020')


#Processos Lista

processoL1 = Processo('Civíl', 1000, 'Deferido', 'Transitado em Julgado', '021')
processoL2 = Processo('Civíl', 2000, 'Indeferido', 'Prazo para Recurso', '022')
processoL3 = Processo('Civíl', 3000, 'Deferido', 'Embargos declaratórios','023')
processoL4 = Processo('Civíl', 4000, 'Indeferido', 'Arquivado', '024')
processoL5 = Processo('Civíl', 5000, 'Deferido', 'Em execução', '025')
processoL6 = Processo('Civíl', 6000, 'Indeferido', 'Prazo para Recurso', '026')
processoL7 = Processo('Civíl', 7000, 'Deferido', 'Em execução', '027')
processoL8 = Processo('Civíl', 8000, 'Indeferido', 'Transitado em Julgado', '028')
processoL9 = Processo('Civíl', 9000, 'Deferido', 'Arquivado', '029')
processoL0 = Processo('Civíl', 1500, 'Indeferido', 'Arquivado', '030')


#Adicionando processo na Pilha
advogado1.adicionar_processo_P(processoP1)
advogado1.adicionar_processo_P(processoP2)
advogado1.adicionar_processo_P(processoP3)
advogado1.adicionar_processo_P(processoP4)
advogado1.adicionar_processo_P(processoP5)


#Adicionando processo na Fila
advogado1.adicionar_processo_F(processoF1)
advogado1.adicionar_processo_F(processoF2)
advogado1.adicionar_processo_F(processoF3)
advogado1.adicionar_processo_F(processoF4)
advogado1.adicionar_processo_F(processoF5)

#Adicionando processo na Lista
advogado1.adicionar_processo_L(processoL5, 1)
advogado1.adicionar_processo_L(processoL4, 2)
advogado1.adicionar_processo_L(processoL3, 3)
advogado1.adicionar_processo_L(processoL2, 4)
advogado1.adicionar_processo_L(processoL1, 5)
