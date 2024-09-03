import leitor
import armazem
import moinho
import impressora

def configurar():
    arquivo_entrada = 'cartao.in'
    arquivo_saida = 'cartao.out'
    return arquivo_entrada, arquivo_saida

def ligar_maquina():
    execucoes = leitor.ler_inst(configurar()[0])
    impressoes = []
    for execucao in execucoes:
        execucao_bin = leitor.conv_bin(execucao)
        endereco = int(execucao_bin[4:8], 2)
        codigo = execucao_bin[:4]
        if codigo == '0001':
            valor = int(execucao_bin[8:], 2)
            armazem.salvar_valor(endereco, valor)
        elif codigo == '0010':
            moinho.coletar_numero(armazem.coletar_valor(endereco))
        elif codigo == '0011':
            moinho.adicao()          
        elif codigo == '0100':
            moinho.diferenca()           
        elif codigo == '0101':
            moinho.produto()
        elif codigo == '0110':
            armazem.salvar_valor(endereco, moinho.receber_resultado())
        elif codigo == '0111':
            valor = armazem.coletar_valor(endereco)
            impressoes.append(impressora.conv_int(valor))
        else:
            print(f'O código {codigo} é inválido')
    if impressoes != []:
        impressora.gravar(configurar()[1], impressoes)

ligar_maquina()