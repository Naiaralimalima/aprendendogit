'''
print('Bem vindo à Pesquisa de hábitos alimentares:')
FastFood = 0
Caseira = 0
Vegetariana = 0
sono = 0

for i in range(5):  # Pergunta para 5 pessoas
    resposta = int(input('Qual o seu hábito alimentar? \n 1 - FastFood \n 2 - Caseira \n 3 - Vegetariana \n'))
    if resposta == 1:
        FastFood += 1
    elif resposta == 2:
        Caseira += 1
    elif resposta == 3:
        Vegetariana += 1
    else:
        print('Opção inválida')

print('Total de respostas:')
print('FastFood:', FastFood)
print('Caseira:', Caseira)
print('Vegetariana:', Vegetariana)

print(int(input('quantidades de sono por noite em horas: ')))
sono += sono
print('Total de sono por noite em horas:', sono)
'''


