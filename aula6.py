# estrutura de repetição while

# um laço de repetição executa um bloco de código enquanto uma condição for verdadeira
# escreva um prograna que ultilize a estrutura while para somar todos os numeros pares de 1 ate um numero n informado pelo usuario
# ultilize o contador para percorre os numeros e verifique se cada  numero é par antes de somar ai final exiba a soma total


'''


contador = 1   
n = int(input('Digite um número: '))
soma = 0

while contador <= n:
    if contador % 2 == 0:
        soma += contador
        print(contador, 'é par')
    contador += 1

print('A soma dos números pares é:', soma)

'''

# estrutura de repetição while
# um laço de repetição executa um bloco de código enquanto uma condição for verdadeira

# break
'''
soma = 0
n = 1

while n != 0:
    n = int(input('Digite um número: '))
    soma += n
    print('A soma dos números é:', soma)



nota = int(input('Digite sua nota de 0 a 10: '))
while nota <= 0 or nota > 10:
    print('Nota inválida, digite novamente')
    nota = int(input('Digite sua nota de 0 a 10: '))

nome = input('Digite seu nome: ').lower()
senha = input('Digite sua senha: ').lower()
while senha == nome:
    print('Senha inválida, digite novamente')
    senha = input('Digite sua senha: ')
 

numero = 0

while numero < 100:
    numero += 1
    print(numero)


import random 


computador = random.randint(0, 20)
print(computador)
jogador = int(input('Digite um número entre 0 e 20: '))



while jogador != computador:
    if jogador > computador:
        print('Tente um número menor ')
    else:
        print('Tente um número maior ')
    print('Você errou, tente novamente')
    jogador = int(input('Digite um número entre 0 e 20: '))
    
print(f'Você acertou! O número sorteado é {computador}  e o numero que você jogou é {jogador}')


operação = print(int(input('Digite a opração desejada : 1 para somar, 2 para subitrair , 3 para multiplicar , 4 para dividir ou  5"sair" para encerrar: ')))

while operação != 5:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    if operação == 1:
        print(f'A soma de {n1} + {n2} é igual a {n1 + n2}')
    elif operação == 2:
        print(f'A subtração de {n1} - {n2} é igual a {n1 - n2}')
    elif operação == 3:
        print(f'A multiplicação de {n1} * {n2} é igual a {n1 * n2}')
    elif operação == 4:
        print(f'A divisão de {n1} / {n2} é igual a {n1 / n2}')
    else:
        print('Opção inválida, digite novamente')
    
    operação = print(int(input('Digite a opração desejada : 1 para somar, 2 para subitrair , 3 para multiplicar , 4 para dividir ou  5"sair" para encerrar: ')))
    
'''
# Inicialização dos contadores
flamengo = vasco = botafogo = fluminense = outros = 0
salario_botafogo = 0
qtd_botafogo = 0
rj_outros = 0
niteroi_fluminense = 0
idade_fem_vasco = 0
qtd_fem_vasco = 0

while True:
    print("\nDigite 0 no time para encerrar.")
    time = int(input("Qual seu time do coração?\n1 - Flamengo\n2 - Vasco\n3 - Botafogo\n4 - Fluminense\n5 - Outros\n"))
    if time == 0:
        break

    cidade = int(input("Onde você mora?\n1 - Rio de Janeiro\n2 - Niterói\n3 - Outros\n"))
    salario = float(input("Qual seu salário? "))
    idade = int(input("Qual sua idade? "))
    genero = input("Qual seu gênero? (M/F) ").strip().upper()

    # 1 - Número de torcedores por clube
    if time == 1:
        flamengo += 1
    elif time == 2:
        vasco += 1
    elif time == 3:
        botafogo += 1
        salario_botafogo += salario
        qtd_botafogo += 1
    elif time == 4:
        fluminense += 1
    elif time == 5:
        outros += 1

    # 3 - Moradores do RJ torcedores de outros clubes
    if cidade == 1 and time == 5:
        rj_outros += 1

    # 4 - Moradores de Niterói torcedores do Fluminense
    if cidade == 2 and time == 4:
        niteroi_fluminense += 1

    # 5 - Média de idade das torcedoras femininas do Vasco
    if time == 2 and genero == 'F':
        idade_fem_vasco += idade
        qtd_fem_vasco += 1

print("\nResultados da pesquisa:")
print("1 - Número de torcedores por clube:")
print(f"Flamengo: {flamengo}")
print(f"Vasco: {vasco}")
print(f"Botafogo: {botafogo}")
print(f"Fluminense: {fluminense}")
print(f"Outros: {outros}")

if qtd_botafogo > 0:
    print(f"2 - Média salarial dos torcedores do Botafogo: {salario_botafogo / qtd_botafogo:.2f}")
else:
    print("2 - Média salarial dos torcedores do Botafogo: Não há torcedores do Botafogo.")

print(f"3 - Número de pessoas moradoras do Rio de Janeiro e torcedoras de outros clubes: {rj_outros}")
print(f"4 - Número de pessoas de Niterói torcedoras do Fluminense: {niteroi_fluminense}")

if qtd_fem_vasco > 0:
    print(f"5 - Média de idade das torcedoras femininas do Vasco: {idade_fem_vasco / qtd_fem_vasco:.2f}")
else:
    print("5 - Média de idade das torcedoras femininas do Vasco: Não há torcedoras femininas do Vasco.")
