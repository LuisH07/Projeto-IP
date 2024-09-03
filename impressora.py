def conv_int(valor):
    valor_int = format(valor, '016b')
    execucao_cod = valor_int.replace('0', 'O').replace('1', 'X')
    execucao_espacada = execucao_cod[:4] + ' ' + execucao_cod[4:8] + ' ' + execucao_cod[8:12] + ' ' + execucao_cod[12:]
    return execucao_espacada

def gravar(arquivo_saida, textos):
    arquivo_out = open(arquivo_saida, 'w')
    for texto in textos:
        arquivo_out.write(texto + '\n')