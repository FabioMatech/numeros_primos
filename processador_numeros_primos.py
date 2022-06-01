# declarando as listas para receber todos os números temporariamente
inteiros = []
eh_primo = []
nao_primos = []

# Recebendo todos ps números do arquivo1.txt
recebe_numeros = open("arquivo1.txt")

# Montando a lista com números inteiros
for i in recebe_numeros:
    numero = i.rstrip("\n").split(" ")
    for cada_numero in numero:
        inteiro = int(cada_numero)
        inteiros.append(inteiro)
print(f'Todos os números recebidos: {inteiros}')

recebe_numeros.close()

# Separando os números primos
for n in inteiros:
    cont = 0
    for divisor in range(2, (n+1)):
        if (n % divisor == 0):
          cont += 1
    if cont <= 2:
        eh_primo.append(n)
    else:
        nao_primos.append(n)

print(f'São números primos: {eh_primo}')
print(f'Não são números primos: {nao_primos}')

# Enviando o resultado para o arquivo2.txt

saida = open("arquivo2,txt", "w")
saida.write(f'Todos os números recebidos: {inteiros}\n')
saida.write(f'São números primos: {eh_primo}\n')
saida.write(f'Não são números primos: {nao_primos}\n')
saida.close()

