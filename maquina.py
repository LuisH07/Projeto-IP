import leitor
import armazem
import moinho
import impressora

def configurar(nome_arquivo_entrada = 'C:/Users/Luís Henrique/Documents/workspace/Estudos/Faculdade/Introdução a programação/Projeto/cartao.in', nome_arquivo_saida = 'cartao.out'):
    global arquivo_entrada, arquivo_saida
    arquivo_entrada = nome_arquivo_entrada
    arquivo_saida = nome_arquivo_saida
    print('configurar funcionou')
    
def ligar_maquina():
    instrucoes = leitor.ler_instrucoes(arquivo_entrada)
    print('maquina funcionou')
    for instrucao in instrucoes:
        instrucao_binaria = leitor.converter_binario(instrucao)
        codigo = instrucao_binaria[:4]
        print('instrucao funcionou')
        if codigo == '0001': #STOREIM
            endereco = int(instrucao_binaria[4:8], 2)
            valor = int(instrucao_binaria[8:], 2)
            armazem.salvar_valor(endereco, valor)
            print(armazem.memoria)
        elif codigo == '0010': #LOADOP
             endereco = int(instrucao_binaria[4:8], 2)
        '''elif codigo == '0011': #ADD
            
        elif codigo == '0100': #SUB
            
        elif codigo == '0101': #MUL
            
        elif codigo == '0110': #STORE
            
        elif codigo == '0111': #PRINT
            
        else:
            print('codigo invalido')'''
            
configurar()
ligar_maquina()