import os

restaurantes = []

#titulo
def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      ''')


#menu do usuario
def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurantes")
    print("4. Sair\n")

def finalizar_app():
    os.system("cls")
    print("Encerrando o app\n")

def opcao_invalida():
    print("Opção inválida\n")
    input("Digite uma tecla para voltar o menu principal: ")
    main()

def cadastrar_restaurante():
    os.system("cls")
    print("cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que quer cadastrar : ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso! ")
    input("Digite uma tecla para voltar o menu principal: ")
    main()
##usuario escolhe opções
def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))


        if opcao_escolhida == 1:
           cadastrar_restaurante()
        elif opcao_escolhida == 2:
            print("Listar restaurantes")
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()        

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == "__main__":
    main()