instrucoes = []
nome_arquivo_entrada = 'cartao.in'

def configurar_entrada(nome_arquivo_entrada):
    arquivo_entrada = open(nome_arquivo_entrada, 'r')
    return arquivo_entrada

def ler_instrucao(nome_arquivo_entrada):
    with open(nome_arquivo_entrada, 'r') as arquivo:
        for instrucao in arquivo:
            instrucao_binario = instrucao.strip().replace('O', '0').replace('X', '1')
            instrucoes.append(instrucao_binario)

def proxima_instrucao():
    if instrucoes == []:
        ler_instrucao(nome_arquivo_entrada)
    else:
        instrucoes = instrucoes.pop(0)
        return instrucoes