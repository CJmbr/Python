import textwrap

def menu():
    menu="""
    ########Menu########

    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Nova conta
    [5] Novo usuário
    [6] Listar contas
    [0] Sair

    Qual a opição deseja:"""
    return input(textwrap.dedent(menu))
    
def depositar(saldo, valor, extrato,/):
    if valor<0:
         print("""
                    Não é posivel depositar, valor invalido. 
                        
                        ### Falha ###""")
            
    else:
        saldo+=(valor)
        print('\n### Valor depositado ###')
        extrato+=(f"\nDeposito   +R${valor:.2f}")
    return saldo, extrato

def saque(*, saldo, valor, extrato, LIMITE, numero_saque, LIMITE_SAQUE):
    if numero_saque==LIMITE_SAQUE:
            print("""
                     Não é possivel fazer mais saques.
                         Limite diario atingido!!!
                            
                        ### Falha ###""")

    elif valor>=saldo:
            print("""
                     Não é possivel fazer o saque.
                         Saldo insuficiente!!!
                            
                        ### Falha ###""")
        
    elif valor>LIMITE:
            print("""
                     Não é possivel fazer o saque.
                    Saque ultrapasa o valor limite!!!
                            
                        ### Falha ###""")
            
    elif valor<0:
            print("""
            Não é posivel fazer a retirada, valor invalido. 
                        
                        ### Falha ###""")

    else:
        saldo-=valor
        extrato+=(f"\nSaque      -R${valor:.2f}")
        numero_saque+=1
        print('\n### Valor Retirato ###')
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print(extrato)
    print (f"____________________\nSaldo       R${saldo:.2f}")
    
def criar_usuario(usuarios):
    cpf= input("informe o CPF (somente número):")
    usuario=filtrar_usuario(cpf, usuarios)

    if usuario:
        print("""CPF já conta.
              ### Falha ###
             """)
        return
        
    nome= input("Informe nome completo:")
    data_nascimento=input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco=input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf,"endereco": endereco})

    print("\tUsuario criado.\n\t### Sucesso ###")

def filtrar_usuario(cpf, usuarios):
      usuarios_filtrados= [usuario for usuario in usuarios if usuario["cpf"] == cpf]
      return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf=input("Informe o CPF do usuário: ")
    usuario=filtrar_usuario(cpf, usuarios)
    if usuarios:
            print("""
                   Conta criada.
                  ### Sucesso ###
                """)
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
      
    print("\n\tUsuário não encontrado, fluxo de criação encerrado.\n\t### Falha ###")
      
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    LIMITE = 500
    saldo = 0
    extrato = "### Extrato ###\n"
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = int(menu())

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                LIMITE=LIMITE,
                numero_saque=numero_saques,
                LIMITE_SAQUE=LIMITE_SAQUES,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                 contas.append(conta)

        elif opcao == 5:
            criar_usuario(usuarios)
           

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
           print("""
              Obrigado por usar nosso sistema Bancario.
                        Finalizando Sistema.
              #########################################
              """)
           break

        else:
            print("""\nOpção indisponivel, por favor escolha novamente!
                ##########""" )

main()