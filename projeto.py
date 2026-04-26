Nome: Penelope Hinata Watanabe  
Turma: (B)

Atividades de lógica de programação
# Nome: Penelope Hinata Watanabe

import math
import random

print("===== ATIVIDADES LÓGICA DE PROGRAMAÇÃO =====")

while True:
    print("\nMENU:")
    print("1 - Tabuada do 1 ao 100")
    print("2 - Números primos até 100")
    print("3 - Hackathon (calculadora simples)")
    print("4 - RPG")
    print("5 - Juros simples")
    print("6 - Raiz quadrada")
    print("7 - Área do quadrado")
    print("8 - IMC")
    print("9 - Conversor de moedas")
    print("10 - Progressão Aritmética")
    print("11 - Fibonacci")
    print("0 - Sair")

    op = int(input("\nEscolha uma opção: "))

    # 1 TABUADA
    if op == 1:
        for i in range(1, 101):
            print(f"\nTabuada do {i}")
            for j in range(1, 11):
                print(f"{i} x {j} = {i*j}")

    # 2 PRIMOS
    elif op == 2:
        for num in range(2, 101):
            primo = True
            for i in range(2, num):
                if num % i == 0:
                    primo = False
                    break
            if primo:
                print(num)

    # 3 CALCULADORA
    elif op == 3:
        print("1-Soma 2-Subtração")
        c = int(input("Escolha: "))
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))

        if c == 1:
            print("Resultado:", a + b)
        elif c == 2:
            print("Resultado:", a - b)

    # 4 RPG
    elif op == 4:
        player = 100
        enemy = 100

        while player > 0 and enemy > 0:
            atk = random.randint(10, 30)
            enemy -= atk
            print("Você atacou:", atk)

            if enemy <= 0:
                break

            atk_e = random.randint(5, 25)
            player -= atk_e
            print("Inimigo atacou:", atk_e)

        print("Fim do jogo!")

    # 5 JUROS
    elif op == 5:
        c = float(input("Capital: "))
        t = float(input("Taxa: "))
        temp = float(input("Tempo: "))
        juros = (c * t * temp) / 100
        print("Juros:", juros)

    # 6 RAIZ
    elif op == 6:
        n = float(input("Número: "))
        print("Raiz:", math.sqrt(n))

    # 7 ÁREA
    elif op == 7:
        l = float(input("Lado: "))
        print("Área:", l * l)

    # 8 IMC
    elif op == 8:
        p = float(input("Peso: "))
        a = float(input("Altura: "))
        print("IMC:", p / (a ** 2))

    # 9 MOEDAS
    elif op == 9:
        r = float(input("Reais: "))
        print("Dólar:", r / 5)

    # 10 PA
    elif op == 10:
        a1 = int(input("Primeiro termo: "))
        r = int(input("Razão: "))
        for i in range(10):
            print(a1 + i * r)

    # 11 FIBONACCI
    elif op == 11:
        n = int(input("Quantidade: "))
        a, b = 0, 1
        for i in range(n):
            print(a)
            a, b = b, a + b

    # SAIR
    elif op == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
