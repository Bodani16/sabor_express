import os
#lista de restaurantes
restaurantes = [{'nome':'Japinha', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

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

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

#menu do usuario
def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurantes")
    print("4. Sair\n")

#Pra encerrar o aplicativo
def finalizar_app():
    exibir_subtitulo("Encerrando o programa.. ")

def voltar_ao_menu_principal():
     input("\nDigite uma tecla para voltar o menu principal: ")
     main()

def opcao_invalida():
    print("Opção inválida\n")
    voltar_ao_menu_principal()

def cadastrar_restaurante():
    exibir_subtitulo("cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que quer cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante{nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante,
                          "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso! ")
    voltar_ao_menu_principal()

def listar_restaurantes():
   exibir_subtitulo("Listando Restaurantes! ")
    
   for restaurante in restaurantes:
     nome_restaurante = restaurante["nome"] 
     categoria = restaurante['categoria']    
     ativo = restaurante['ativo']            
     print(f'-> {nome_restaurante} | {categoria} | {ativo}')
   voltar_ao_menu_principal()

##usuario escolhe opções
def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))


        if opcao_escolhida == 1:
           cadastrar_restaurante()
        elif opcao_escolhida == 2:
           listar_restaurantes()
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
