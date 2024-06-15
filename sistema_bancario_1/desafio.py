"""
Desafio de criação de um mini-sistema bancário
Autor : Ednilson Nascimento
"""

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0.
limite = 500.00
extrato = ""
LIMITE_SAQUES = 3
titulo = "DESAFIO BANCÁRIO"
subtitulo=""
valor = 0.
saques = 0
while True:
    
    print(titulo.center(80,"─"))
    opcao = input(menu)
    opcao = opcao.lower()
    
    if opcao == 'd':
        subtitulo = "DEPOSITO"
        print(titulo.center(80,"─"))
        print(subtitulo.center(80))
        valor = float(input("Digite o valor do depósito: "))
        if valor < 0.:
            print("Impossivel realizar, informado valor negativo!!!")
        elif valor == 0.:
            print("Impossivel realizar, informado um valor zerado!!!")
        else:
            saldo += valor
            extrato += f"Depósito : + R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:5.2f} realizado com sucesso.")
            print(f"Saldo atual: R$ {saldo:5.2f}.")
    elif opcao == 's':
        subtitulo = "SAQUE"
        print(titulo.center(80,"─"))
        print(subtitulo.center(80))
        if saques >= LIMITE_SAQUES:
            print("Impossivel realizar, limite de saques diário atingido")
        else:
            print(f'Saques disponiveis {LIMITE_SAQUES-saques} - limite por saque R$ 500.00 - Saldo atual R$ {saldo:.2f}')
            valor = float(input("Digite o valor do saque: "))
            if valor < 0:
                print("Impossivel realizar, informado valor negativo!!!")
            elif valor == 0:
                print("Impossivel realizar, informado um valor zerado!!!")
            elif valor > limite:
                 print(f"Impossivel realizar, informado um valor maior que limite R$ {limite:.2f}!!!")
            elif valor > saldo:
                print("Saldo insuficiente!!!")
            else:
                saldo -= valor
                saques += 1
                extrato += f"Saque    : - R$ {valor:.2f}\n"
                print(f"Saque de R$ {valor:5.2f} realizado com sucesso.")
                print(f"Saldo atual: R$ {saldo:5.2f}")
                
    elif opcao == 'e':
        subtitulo = "EXTRATO"
        print(titulo.center(80,"─"))
        print(subtitulo.center(80))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:5.2f}")
    elif opcao == 'q':
        break
    else:
        print("Opção invalida, tente novamente com uma das teclas informadas!!!")