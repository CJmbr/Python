menu="""
    ########Menu########

    [1] Deposito
    [2] Saque
    [3] Extrato
    [0] Sair
    
    #####

    Qual a opição deseja:"""

saldo=float(0)

extrato="### Extrato ###\n"

numero_saque=0

LIMITE=500

LIMITE_SAQUE=3

while True:
    
    operacao=int(input(menu))

    if operacao==1:
        deposito=float(input("""\n### Depósito ###
              
                Digite o valor a ser depositado:"""))
        if deposito<0:
            print("""
                    Não é posivel depositar, valor invalido. 
                        
                        ### Falha ###""")
            
        else:
            saldo+=(deposito)
            print('\n### Valor depositado ###')
            extrato+=(f"\nDeposito   +R${deposito:.2f}")

    elif operacao==2:
        saque=float(input("""\n### Saque ###
                        
                        Digite o valor que deseja retirar:"""))

        if numero_saque==LIMITE_SAQUE:
            print("""
                     Não é possivel fazer mais saques.
                         Limite diario atingido!!!
                            
                        ### Falha ###""")

        elif saque>=saldo:
            print("""
                     Não é possivel fazer o saque.
                         Saldo insuficiente!!!
                            
                        ### Falha ###""")
        
        elif saque>LIMITE:
            print("""
                     Não é possivel fazer o saque.
                    Saque ultrapasa o valor limite!!!
                            
                        ### Falha ###""")
            
        elif saque<0:
            print("""
            Não é posivel fazer a retirada, valor invalido. 
                        
                        ### Falha ###""")

        else:
            saldo-=saque
            extrato+=(f"\nSaques     -R${saque:.2f}")
            numero_saque+=1
            print('\n### Valor Retirato ###')
    
    elif operacao==3:
        print(extrato)
        print (f"""
     ____________________
     Saldo       R${saldo:.2f}
        ##########""")

    elif operacao==0:
        print("""
              Obrigado por usar nosso sistema Bancario.
                        Finalizando Sistema.
              #########################################
              """)
        break

    else:
        print("""\nOpção indisponivel, por favor escolha novamente!
                ##########""" )

        