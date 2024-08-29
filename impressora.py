num1 = 18
bin_str1 = format(num1, '08b') # Converte para binário, 8 bits de comprimento
print(f"O número {num1} em 8 bits é: {bin_str1}") # Saída: '10010

# String de bits
bin_str2 = '00010010'
# Converte a string de bits para um número inteiro
num2 = int(bin_str2, 2)
print(num2) # Saída: 18