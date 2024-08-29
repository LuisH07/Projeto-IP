instrucoes = []

def ler_instrucoes(cartao_entrada):
    cartao_entrada = 'cartao.in'
    with open(cartao_entrada, 'r') as arquivo:
        for instrucao in arquivo:
            instrucao_binario = instrucao.strip().replace('X', '1').replace('O', '0')
            instrucoes.append(instrucao_binario)

def proxima_instrucao():
    if not instrucoes == []:
        instrucoes = instrucoes.pop(0)
    return None