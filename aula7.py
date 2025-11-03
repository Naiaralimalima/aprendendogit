#Vetores

'''
vetor1 = np.array([1, 2, 3, 4, 5])
print(vetor1)
# Primeiro elelmento


vetor2 = np.zeros(5)
print(vetor2)

veror3 = np.ones(5) 
print(veror3)

vetor = 
print(vetor)

#modificar elemento
vetor1[1] = 10
print(vetor1)
#modificar um intervalo de um elementos
vetor1[0:2] = 20
print(vetor1)

import numpy as np




vetor =  np.random.randint(5, 100, 10)
print(vetor)

soma = 0
maior = 0
menor = 101
for num in vetor:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
print('Soma:', soma)
print('Maior:', maior)
print('Menor:', menor)
escolha = (print(int(input('jogo de adivinhação, digite um numero entre  5 e 100: '))))   
encontrado = False
for num in vetor:
    if num == escolha:
        encontrado = True
        break

if encontrado:
    print('Número encontrado no vetor!')
else:
    print('Número não encontrado no vetor!')

    

import numpy as np

#elabore um progarama que receba a nota de 5 alunos e armazene em um vetor.

notas = np.zeros(5)
soma = 0
for i in range(5):
    notas [1]=(input(f'Digite a nota do aluno : '))
    soma += notas
    media = soma / 5
print('A média da turma é :', m



import numpy as np
nomes = np.empty(5)

tamanho = 5
for i in range(2):
    nomes[1] = input(f'Digite o nome do aluno : ')
'''
import numpy as np
temperaturas_c = np.zeros(5)
f = 0
media = 0
for i in range(5):
    temperaturas_c[i] = float(input(f'Digite a temperatura do dia {i+1}: '))
    f = (temperaturas_c[i] * 9/5) + 32
    print(f'A temperatura em Fahrenheit é : {f}°F')
    media += f
    max = f.max(f)in(f)



   

