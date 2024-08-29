memoria = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def armazenar_valor(endereco, valor):
    memoria[endereco] = valor
    
def carregar_valor(endereco):
    valor_carregado = memoria[endereco]
    return valor_carregado