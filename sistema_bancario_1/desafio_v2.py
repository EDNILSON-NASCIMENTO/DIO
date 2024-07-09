import textwrap
import os
import time



def menu():
    
    menu = """
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair


=> """

    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    subtitulo = "DEPOSITO"
    print(subtitulo.center(80))
    if valor < 0.:
        print("Impossivel realizar, informado valor negativo!!!")
    elif valor == 0.:
        print("Impossivel realizar, informado um valor zerado!!!")
    else:
        saldo += valor
        extrato += f"Depósito : + R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:5.2f} realizado com sucesso.")
        print(f"Saldo atual: R$ {saldo:5.2f}.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, saques, LIMITE_SAQUES):
    subtitulo = "SAQUE"
    print(subtitulo.center(80))
    if saques >= LIMITE_SAQUES:
        print("Impossivel realizar, limite de saques diário atingido")
    else:
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
            print(f'Saques disponiveis {LIMITE_SAQUES-saques} - limite por saque R$ 500.00 - Saldo atual R$ {saldo:.2f}')
            
    return saldo, extrato, saques

def mostra_extrato(saldo, /, *, extrato):
    subtitulo = "EXTRATO"
    print(subtitulo.center(80,"-"))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:5.2f}")


#Funcções de conta e usuario

def criar_usuario(usuarios):
    cpf = input("Informe o  CPF [APENAS NÚMEROS]: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Ja existe este cpf...")
        return
    
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa) : ")
    endereco = input("Informe o endereço [logradouro/nro/bairro/cidade/UF]: ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})
    
    print("Usuario cadastrado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso...")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não existe, impossivel realizar!!!")
    
    
def listar_contas(contas):
    subtitulo = "RELATÓRIO DE CONTAS"
    print(subtitulo.center(80,"─"))
    print("AGÊNCIA\tCONTA\tCLIENTE")
    print("─"*80)
    
    for conta in contas:
        print(f"{conta['agencia']}\t{conta['numero_conta']}\t{conta['usuario']['nome']}")
 
def main():
   
    saldo = 0.
    limite = 500.00
    extrato = ""
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    titulo = "DESAFIO BANCÁRIO"
    valor = 0.
    saques = 0
    usuarios = []
    contas = []
    
    while True:
        time.sleep(3)
        os.system("cls")
        print(titulo.center(80,"─"))
        opcao = menu().lower()
        # opcao = opcao.lower()
        
        if opcao == "q":
            print("Até breve")
            break
        elif opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo,valor, extrato)
        elif opcao == 's':
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, saques = sacar(saldo=saldo,valor=valor,extrato=extrato, limite=limite, saques=saques,LIMITE_SAQUES=LIMITE_SAQUES)
        elif opcao == "e":
            mostra_extrato(saldo, extrato=extrato)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nu":
            criar_usuario(usuarios)
        else:
            print("Opção invalida...")

main()
