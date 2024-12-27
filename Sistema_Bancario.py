#                                  DESAFIO - SISTEMA BANCÁRIO                                     
#--------------------------------------------------------------------------------------------------
#                                             REGRAS                                                 
#                                   --------------------------
# 1   - Sistema simples gerido apenas para um usuário;
# 2   - Deverá inplementar 3 operações: Depósito, Saque e Extrato;
# 3   - Depósito: Deverá depositar valores positivos;
# 3.1 - Todos os depósitos deverão ser armazenados em uma variável e exibidos na operação extrato;
# 4   - Saque: Permite realizar 3 saques diários com limite de R$ 500,00 por saque;
# 4.1 - Caso o usuário não tenha saldo em conta deverá exibir uma mensagem informando que por falta_
#       _de saldo não será possível sacar o dinheiro;
# 4.2 - Saques deverão estar armazenados em uma variável e exibidos na operação de extrato;
# 5   - Extrato: Listar todos os depósitos e saques realizados na conta;
# 5.1 - No fim da listagem deve ser exibido o saldo atual da conta;
# 5.2 - Os valores devem ser exibidos no formato R$ xxx.xx.
#--------------------------------------------------------------------------------------------------
#                                        DESAFIOS PESSOAIS                                         
# 1 - Desenvolver sistema interativo e transparente com o cliente;
# 2 - Possibilitar que o sistema só seja encerrado quando o usuário solicitar;
# 3 - Informar uma opção de saldo para que o usuário não precise ler muitas informações do extrato;
# 4 - Valor da operação de depósito não poderá ser manor ou igual a zero.
#--------------------------------------------------------------------------------------------------

menu = """

                 MENU
---------------------------------------
Gentileza informar a operação desejada:

[1] - Depósito
[2] - Saque
[3] - Saldo
[4] - Extrato
[5] - Sair

----------------------------------------
"""

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIA = 3

while True:

    opcao = int(input(menu))

    if opcao == 1: #Operação Depósito
        deposito = float(input(f"Você selecionou a opção Deposito.\nFavor informar o valor de depósito: R$ "))
        saldo += deposito
        extrato += str(f"Depósito: + R$ {deposito:.2f}\n")
        print(f"Você depositou R$ {deposito:.2f}, seu saldo é de R$ {saldo:.2f} ")
        
    elif opcao == 2: #Operação Saque
        if numero_saques >= LIMITE_SAQUES_DIA:
            print("Numero de saques diários excedidos.")
            break
        saque = float(input(f"Você selecionou a opção Saque.\nFavor informar valor de saque: R$ -"))
        if saque > limite_valor_saque:
            print(f"Valor de saque superior ao limite atribuído. Favor realizar operação com valor inferior à R$ {limite_valor_saque:.2f}.")
        elif saque > saldo:
            print(f"Saque não realizado, valor solicitado é superior ao saldo de R$ {saldo:.2f}.")
        else:
            saldo -= saque
            numero_saques += 1
            extrato += str(f"Saque: - R$ {saque:.2f}\n")
            print(f"Você sacou R$ {saque:.2f}.\nSeu saldo atual é de: R$ {saldo:.2f} ")

    elif opcao == 3: #Operação Saldo
        print(f"Você selecionou a opção Saldo.\nSeu saldo é de R$ {saldo:.2f}")

    elif opcao == 4: #Operação Extrato
        print("Você selecionou a opção Extrato.\n\n-----------------EXTRATO----------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("----------------------------------------")
    
    elif opcao == 5: #Operação Sair
        print("Operação Finalizada.")
        break

    else:
        print("Opção Inválida, favor selecionar uma das opções a segur.")