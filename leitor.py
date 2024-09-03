def ler_inst(arquivo_entrada):
    arquivo_in = open(arquivo_entrada, 'r')
    execucoes = arquivo_in.readlines()
    return execucoes

def conv_bin(execucao):
    execucao = execucao.replace('O', '0').replace('X', '1').replace(' ', '')
    return execucao