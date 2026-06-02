import os
opcao = 0
cod = []
nome = []
preco = []
quantidade = []
venda = []

while opcao != 5:
    print("==================== MENU -GUGA MERCADINHOS =======================")
    print("1 - Cadastre o produto;")
    print("2 - Veja os produtos já cadastrados;")
    print("3 - Exclua produtos registrados;")
    print (" 4-VENDA DE PRODUTO")
    print("5 - Sair.")
    opcao = int(input("Informe sua escolha: "))

    if opcao == 1:
        print("\n----------------- CADASTRE SEU PRODUTO -----------------")
        codigo_produto = input("Informe o código do seu produto: ")
        nome_produto = input("Informe o nome do produto: ")
        preco_produto = float(input("Informe o preço do produto: "))
        quantidade_produto = int(input("Informe a quantidade de produtos disponíveis: "))

        cod.append(codigo_produto)
        nome.append(nome_produto)
        preco.append(preco_produto)
        quantidade.append(quantidade_produto)

        arquivo = open("produtoss.txt", "a")
        arquivo.write(f"{codigo_produto}, {nome_produto}, {preco_produto}, {quantidade_produto}\n")
        arquivo.close()


        print("Seu produto foi cadastrado com sucesso!")
        print("Aperte qualquer tecla para voltar ao menu")
        print("GUGA MERCADINHOS")

        input()
        os.system("cls")

    elif opcao == 2:
        print("\n-------------------------- PRODUTOS CADASTRADOS ------------------------")
        print("Veja os produtos que já foram cadastrados no nosso site:")

        for codigin, nominal, takaro, cantidad in zip (cod, nome, preco, quantidade):
            print("_________________________________________________________________\n")
            print(f"{codigo_produto}, {nome_produto}, {preco_produto}, {quantidade_produto}")

    elif opcao == 3:
        print("------------------------------ EXCLUIR ---------------------------------")

        arquivo = open("produtoss.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()

        remover = int(input("Digite a linha que deseja remover: "))
        remover = remover - 1
        linhas.pop(remover)

        arquivo = open("produtoss.txt", "w")
        for linha in linhas:
            arquivo.write(linha)
        arquivo.close()

        print("Produto removido com sucesso!")
        print("Aperte qualquer tecla para voltar ao menu")
        print("GUGA MERCADINHOS")

        input()
        os.system("cls")


    
    

    elif opcao == 4:
        print("***************************VENDA DE PRODUTOS**********************************")
        arquivo = open("produtoss.txt","r")
        linhas = arquivo.readlines()
        arquivo.close()

        venda = int(input("ME FALE O PRODUTO QUE VOCE DESEJA VENDER: "))
        venda = venda - 1

        produto, codigo, preco, quantidade = linhas[venda].strip().split(",")

        vendas = int(input("QUAL A QUANTIDADE VENDIDA?: "))

        nova_quantidade = int(quantidade) - vendas

        linhas[venda] = (f"{produto},{codigo},{preco},{nova_quantidade}\n")

    try:
        resultado = quantidade >= venda 
    
        arquivo = open("produtoss.txt", "w")
        for linha in linhas:
            arquivo.write(linha)
        arquivo.close()

        print("VENDA REALIZADA COM SUCESSO!")

    except Exception:
        print("PRODUTO NÃO DISPONIVEL NO ESTOQUE!") 

    
    if opcao == 5:
        print("Saindo do programa...")

        print("Obrigado por confiar no GUGA MERCADINHOS!\n")
 
