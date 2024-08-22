# home.py

from funcoes import *

def exibir_menu():
   
    print("\n===========================")
    print("        Menu da Pizzaria    ")
    print("===========================")
    print("1. Adicionar Pedido")
    print("2. Listar Pedidos")
    print("3. Calcular Total")
    print("4. Remover Pedido")
    print("5. Listar Pizzas Disponíveis")
    print("6. Sair")
    print("===========================")
    escolha = input("Escolha uma opção (1-6): ")
    return escolha

def programa():
    pedidos = []
    preco_por_pizza = {
        'Margherita': 25.00,
        'Pepperoni': 30.00,
        'Quatro Queijos': 35.00,
        'Frango com Catupiry': 32.00
    }

    while True:
        escolha = exibir_menu()

        if escolha == '1':
            pizza = input("Digite o nome da pizza: ")
            quantidade = int(input("Digite a quantidade: "))
            adicionar_pedido(pedidos, pizza, quantidade)
            print(f"Pedido de {quantidade} {pizza}(s) adicionado.")

        elif escolha == '2':
            pedidos_lista = listar_pedidos(pedidos)
            print("\nPedidos Atuais:")
            print(pedidos_lista)

        elif escolha == '3':
            total = calcular_total(pedidos, preco_por_pizza)
            print(f"\nO total dos pedidos é R${total:.2f}")

        elif escolha == '4':
            pizza = input("Digite o nome da pizza a ser removida: ")
            mensagem = remover_pedido(pedidos, pizza)
            print(mensagem)

        elif escolha == '5':
            pizzas_disponiveis = listar_pizzas_disponiveis(preco_por_pizza)
            print("\nPizzas Disponíveis:")
            print(pizzas_disponiveis)

        elif escolha == '6':
            print("\nSaindo do sistema. Até mais!")
            break

        else:
            print("\nOpção inválida. Por favor, escolha uma opção entre 1 e 6.")

if __name__ == "__main__":
    programa()
