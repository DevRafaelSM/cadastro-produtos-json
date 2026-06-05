from produtos_service import (
    Produtos,
    atualizar_preco,
    buscar_produtos,
    inativar_produto,
    listar_produtos,
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
                produtos.adicionar_produto()
            case "2":
                listar_produtos()
            case "3":
                buscar_produtos()
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
