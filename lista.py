tamanho = int(input("Digite o tamanho da lista: "))
numeros = [i for i in range (tamanho*2) if i % 2 == 0]
print("lista de numeros: " + str(numeros))
print("soma dos numeros: " + str(sum(numeros)))