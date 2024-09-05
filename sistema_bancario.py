menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

## print(menu)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    ## Operação Depositar (d)
    if opcao == "d":

        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")
            #print("Deposito")
    
    ## Operação Sacar (s)
    elif opcao == "s":

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES ## O limite diário é de 3 saques, então deveria ser 'numero_saques > LIMITES_SAQUES'
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        #print("Saque")

    ## Operação Extrato (e)
    elif opcao == "e":
        print("\n================== EXTRATO ==================") # \n = quebra de linha
        print("Não foram realizadas movimentações." if not extrato else extrato) #if ternário
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================")

        #print("Extrato")

    ## Operação Sair (q)
    elif opcao == "q":

        print("Sair")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.\n")
