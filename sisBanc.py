menu = """
[d] depositar
[s] sacar 
[e] extrato
[o] sair 
=> """ 

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3 

while True: 
    opcao = input(menu)

    if opcao == "d": 
        valor = float(input("Digite o valor do deposito: "))

        if valor > 0: 
         saldo += valor 
         extrato += f"Depósito: R$ {valor:.2f}\n"
         print(f"O valor de R$: {valor: .2f} \n foi depositado com sucesso!")

        else: 
          print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        print(f"O valor de R$: {valor: .2f} \n foi sacado com sucesso!")

        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques  >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! A conta não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou!O valor de saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque:  R$ {valor:.2f}\n"
            numero_saques += 3

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "e":
        print("\n *************** EXTRATO ****************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print( f"\nSaldo: R$ {saldo:.2f}")
        print("*****************************************")

    elif opcao == "o":
        break 

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")
        opcao = input(menu)