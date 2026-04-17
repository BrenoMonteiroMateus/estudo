print("Agenda de Contatos")
nomes = []
opcao = 0
while True:
    print("1-Cadastrar nome\n2-Remover nome\n3-Alterar nome\n4-Buscar nome\n5-Mostrar Agenda\n6-Ordenar(A - Z)\n7-Ordenar(Z - A)\n0-Sair")
    opcao = int(input("Digite a opcao: "))
    match opcao:
        case 1: 
            adicionar_nome = input("Digite um nome: ")
            nomes.append(adicionar_nome)
            print(f'nome {adicionar_nome} inserido com sucesso')
        case 2:
            nome_a_ser_removido = input("Digite o nome a ser removido: ")
            if nome_a_ser_removido in nomes:
                nomes.remove(nome_a_ser_removido)
                print("nome removido com sucesso!")
            else:
                print("o nome digitado não está na lista")
        case 3:
            nome_a_ser_alterado = input("Digite o nome a ser alterado: ")
            if nome_a_ser_alterado in nomes:
                posicao = nomes.index(nome_a_ser_alterado)
                nome_novo = input("Digite um novo nome: ")
                nomes[posicao] = nome_novo
                print(f'{nome_a_ser_alterado} alterado para {nome_novo}')
            else:
                print("nome antigo não está na agenda!")
        case 4:
            verificar = input("Digite o nome para ver se ele está na lista: ")
            if verificar in nomes:
                posicao = nomes.index[verificar]
                print(f"{verificar} está na lista e na posição: {posicao}")
            else:
                print("o nome digitado não está na agenda... se quiser adicionar digite 1")
        case 5:
            if len(nomes == 0):
                print('lista vazia, voce nao tem amigos!')
            else:
                print(f"Agenda com nomes {nomes}")
        case 6:
            nomes.sort()
            print(f"Agenda de A - Z: {nomes}")
        case 7:
            nomes.sort(reverse=True)
            print(f"Agenda de Z - A: {nomes}")
        case 0:
            print("Obrigado volte sempre!")
            break #quebrando o laco infinito
        case _: #quando nenhuma opcao dentro do case é usada
            print("Opção invalida!")
