import numpy as np

nomes = np.empty(10, dtype=object)
quantidade = np.zeros(10, dtype=object)

print("Cadastro de Produtos")
while True:
    print("\n1 - inclusão de novo produto")
    print("2 - alteração de quantidade")
    print("3 - exclusão de produto")
    print("4 - impressão dos produtos cadastrados")
    print("5 - consulta por nome de produto")
    print("6 - sair do programa")
    opcao = int(input("Digite a opção desejada: "))

    if opcao < 1 or opcao > 6:
        print("Opção inválida, digite novamente")
        continue

    elif opcao == 1:
        nome = input("Digite o nome do produto: ").lower()
        qtd = int(input("Digite a quantidade desejada: "))
        
        # encontra posição livre
        for i in range(len(nomes)):
            if nomes[i] is None:
                nomes[i] = nome
                quantidade[i] = qtd
                break
        print(f"Produto {nome} adicionado com {qtd} unidades.")

    elif opcao == 2:
        nome = input("Digite o nome do produto que deseja alterar a quantidade: ").lower()
        nova_quantidade = int(input("Digite a nova quantidade: "))

        encontrado = False
        for i in range(len(nomes)):
            if nomes[i] == nome:
                quantidade[i] = nova_quantidade
                print(f"\nQuantidade de {nomes[i]} atualizada para {quantidade[i]}")
                encontrado = True
                break

        if not encontrado:
            print("Produto não encontrado!")


    elif opcao == 3:
        nome = input(f"\n Digite o nome do produto que deseja excluir: ")
        encontrado = False 
        for i in range (len(nomes)):
            if nomes [i] == nome:
                nomes [i] = ""
                quantidade [i] = 0
                print(f"Produto '{nome}' excluído com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado!")
    elif opcao == 4:
        encontrado = False 
        print(f"\nProdutos cadastrados ")  
        for i in range(len(nomes)):
            if nomes[i] is None: 
                print(nomes)
        if not encontrado:
            print("Produto não encontrado!")

