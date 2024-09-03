memoria = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def salvar_valor(endereco, valor):
    memoria[endereco] = valor
    
def coletar_valor(endereco):
    valor_coletado = memoria[endereco]
    return valor_coletado