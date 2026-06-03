# exibir o menu
# capturar a opção do usuário
# controlar o fluxo principal
# chamar as funções do service
# encerrar o programa


from produtos_service import (
    Produtos,
    atualizar_preco,
    buscar_produto_por_id,
    cadastrar_produto,
    inativar_produto,
    mostrar_lista_produtos_console,
)


def main():

    produtos = Produtos()

    while True:
        print("========= Cadastro de Produtos ========")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Buscar produto por ID")
        print("4. Atualizar preço")
        print("5. Inativar produto")
        print("6. Finalizar")
        print("=======================================")

        opcao = input("Escolha uma opção: ")
        print("")

        match opcao:
            case "1":
                cadastrar_produto(produtos)
            case "2":
                mostrar_lista_produtos_console()
            case "3":
                buscar_produto_por_id()
            case "4":
                atualizar_preco()
            case "5":
                inativar_produto()
            case "6":
                print("Encerrando o programa...")
                break
            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
