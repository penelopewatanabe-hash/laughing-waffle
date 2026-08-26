import math
import random

print("===== ATIVIDADES DE LÓGICA DE PROGRAMAÇÃO =====")
print("Nome: Penelope Hinata Watanabe")
print("Turma: B")

while True:
    print("\n===== MENU =====")
    print("1 - Tabuada do 1 ao 100")
    print("2 - Números primos até 100")
    print("3 - Calculadora simples")
    print("4 - RPG")
    print("5 - Juros simples")
    print("6 - Raiz quadrada")
    print("7 - Área do quadrado")
    print("8 - IMC")
    print("9 - Conversor de moedas")
    print("10 - Progressão Aritmética")
    print("11 - Fibonacci")
    print("0 - Sair")

    try:
        op = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    # 1 - TABUADA
    if op == 1:
        print("\n===== TABUADA DO 1 AO 100 =====")

        for i in range(1, 101):
            print(f"\nTabuada do {i}")

            for j in range(1, 11):
                print(f"{i} x {j} = {i * j}")

    # 2 - NÚMEROS PRIMOS
    elif op == 2:
        print("\n===== NÚMEROS PRIMOS ATÉ 100 =====")

        for num in range(2, 101):
            primo = True

            for i in range(2, num):
                if num % i == 0:
                    primo = False
                    break

            if primo:
                print(num)

    # 3 - CALCULADORA
    elif op == 3:
        print("\n===== CALCULADORA =====")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        c = int(input("Escolha uma operação: "))

        a = float(input("Número 1: "))
        b = float(input("Número 2: "))

        if c == 1:
            print("Resultado:", a + b)

        elif c == 2:
            print("Resultado:", a - b)

        elif c == 3:
            print("Resultado:", a * b)

        elif c == 4:
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("Não é possível dividir por zero!")

        else:
            print("Operação inválida!")

    # 4 - RPG
    elif op == 4:
        print("\n===== RPG =====")

        player = 100
        enemy = 100

        while player > 0 and enemy > 0:

            atk = random.randint(10, 30)
            enemy -= atk

            print("\nVocê atacou o inimigo!")
            print("Dano causado:", atk)
            print("Vida do inimigo:", max(enemy, 0))

            if enemy <= 0:
                break

            atk_e = random.randint(5, 25)
            player -= atk_e

            print("\nO inimigo atacou você!")
            print("Dano recebido:", atk_e)
            print("Sua vida:", max(player, 0))

        if player <= 0:
            print("\nVocê perdeu a batalha!")

        elif enemy <= 0:
            print("\nVocê venceu a batalha!")

    # 5 - JUROS SIMPLES
    elif op == 5:
        print("\n===== JUROS SIMPLES =====")

        capital = float(input("Capital: "))
        taxa = float(input("Taxa (%): "))
        tempo = float(input("Tempo: "))

        juros = (capital * taxa * tempo) / 100
        montante = capital + juros

        print("Juros:", juros)
        print("Montante:", montante)

    # 6 - RAIZ QUADRADA
    elif op == 6:
        print("\n===== RAIZ QUADRADA =====")

        n = float(input("Digite um número: "))

        if n >= 0:
            raiz = math.sqrt(n)
            print("Raiz quadrada:", raiz)
        else:
            print("Não é possível calcular a raiz de um número negativo.")

    # 7 - ÁREA DO QUADRADO
    elif op == 7:
        print("\n===== ÁREA DO QUADRADO =====")

        lado = float(input("Digite o lado do quadrado: "))

        area = lado * lado

        print("Área do quadrado:", area)

    # 8 - IMC
    elif op == 8:
        print("\n===== IMC =====")

        peso = float(input("Peso em kg: "))
        altura = float(input("Altura em metros: "))

        if altura > 0:
            imc = peso / (altura ** 2)

            print(f"Seu IMC é: {imc:.2f}")

            if imc < 18.5:
                print("Classificação: abaixo do peso")
            elif imc < 25:
                print("Classificação: peso normal")
            elif imc < 30:
                print("Classificação: sobrepeso")
            else:
                print("Classificação: obesidade")
        else:
            print("A altura deve ser maior que zero.")

    # 9 - CONVERSOR DE MOEDAS
    elif op == 9:
        print("\n===== CONVERSOR DE MOEDAS =====")

        reais = float(input("Digite o valor em reais: "))

        # Cotação utilizada apenas para fins de exercício.
        cotacao_dolar = 5.00

        dolares = reais / cotacao_dolar

        print(f"Valor em dólares: US$ {dolares:.2f}")
        print("Cotação utilizada no exercício: R$ 5,00")

    # 10 - PROGRESSÃO ARITMÉTICA
    elif op == 10:
        print("\n===== PROGRESSÃO ARITMÉTICA =====")

        primeiro_termo = int(input("Primeiro termo: "))
        razao = int(input("Razão: "))

        print("Os 10 primeiros termos são:")

        for i in range(10):
            termo = primeiro_termo + i * razao
            print(termo)

    # 11 - FIBONACCI
    elif op == 11:
        print("\n===== FIBONACCI =====")

        quantidade = int(input("Quantidade de números: "))

        if quantidade <= 0:
            print("Digite uma quantidade maior que zero.")

        else:
            a = 0
            b = 1

            print("Sequência:")

            for i in range(quantidade):
                print(a)

                a, b = b, a + b

    # 0 - SAIR
    elif op == 0:
        print("\nSaindo do programa...")
        print("Até a próxima! 👋")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("\nOpção inválida! Escolha uma opção do menu.")
