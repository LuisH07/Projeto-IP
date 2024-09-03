operandos = [0, 0]
resultados = [0]

def diferenca():
        resultado = operandos[-2] - operandos[-1]
        if resultado < 0:
            resultado = 0
        resultados.append(resultado)
        return resultado

def receber_resultado():
    return resultados[-1]
    
def coletar_numero(valor):
    operandos.append(valor)
    
def adicao():
    resultado = operandos[-2] + operandos[-1]
    resultados.append(resultado)
    return resultado

def produto():
    resultado = operandos[-2] * operandos[-1]
    resultados.append(resultado)
    return resultado