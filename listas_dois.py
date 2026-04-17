quantidade_notas = int(input("Quantas notas serão inseridas? "))
notas = []
cont = 1
while cont <= quantidade_notas:
    
    #digite = float(input("Digite as notas: "))
    notas.append(float(input(f"Digite a {cont}a nota: ")))
    cont = cont + 1

print("Lista de notas: " + str(notas))
print("Maior nota da lista: " + str(max(notas)))
print("Menor nota da lista: " + str(min(notas)))
print(f"Média das notas: {sum(notas)/len(notas):.2f}" )