print("Olá sejam bem vindos a Mauá na Chapa")
print("------------------------------------")
print("Pedidos acima de R$ 60 possuem 10% de desconto!")
print("Cardapio\n\n(1)Hamburguer:R$ 20,00\n(2)Batata Frita:R$ 10,00\n(3)Refrigerante:R$ 7,00\n(4)Sorvete:R$ 5,00\n")

pedido = int(input("Digite o código do produto, digite 0 para parar: "))
quantidade = int(input("Digite a quantidade: "))

carrinho = []

total_pedido = 0

while pedido != 0:
    match pedido:
        case 1:
            for x in range(quantidade):
                carrinho.append("Hamburguer")
            total = 20 * quantidade
            total_pedido = total_pedido + total
        case 2:
            for x in range(quantidade):
                carrinho.append("Batata Frita")
            total = 10 * quantidade
            total_pedido = total_pedido + total
        case 3:
            for x in range(quantidade):
                carrinho.append("Refrigerante")
            total = 7 * quantidade
            total_pedido = total_pedido + total
        case 4:
            for x in range(quantidade):
                carrinho.append("Sorvete")
            total = 5 * quantidade
            total_pedido = total_pedido + total

    pedido = int(input("Digite o código do produto, digite 0 para parar: "))

    if pedido == 0:
        break
    
    quantidade = int(input("Digite a quantidade: "))

if total_pedido > 60:
    total_pedido = total_pedido * 0.9

print(f'O total do pedido é R${total_pedido:.2f}')

for item in set(carrinho):
    quantidade = carrinho.count(item)
    if quantidade > 0:
        print(f"Você comprou {quantidade} {item}(s)")
 
# if carrinho.count("Hamburguer") > 0:
#     print(f"Você comprou {carrinho.count('Hamburguer')} hambúrguer(es)")

# if carrinho.count("Batata Frita") > 0:
#     print(f"Você comprou {carrinho.count('Batata Frita')} batata(s) frita(s)")

# if carrinho.count("Refrigerante") > 0:
#     print(f"Você comprou {carrinho.count('Refrigerante')} refrigerante(s)")

# if carrinho.count("Sorvete") > 0:
#     print(f"Você comprou {carrinho.count('Sorvete')} sorvete(s)")1
