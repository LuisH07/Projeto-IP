def ler_instrucoes(arquivo_entrada):
    with open(arquivo_entrada, 'r') as arquivo:
        instrucoes = arquivo.readlines()
    return instrucoes

def converter_binario(instrucao):
    return instrucao.replace('X', '1').replace('O', '0').replace(' ', '')