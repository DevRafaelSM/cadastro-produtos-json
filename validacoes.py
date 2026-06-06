from typing import Any

from models import Produto


def validar_entrada_nome_produto(entrada: str, produtos: list) -> str:

    nomes_existentes = {produto.produto_nome.lower() for produto in produtos}

    while True:
        entrada = entrada.strip()

        if entrada.lower() in nomes_existentes:
            entrada = input("Esse nome já está em uso. Por favor, insira outro nome: ")
        elif entrada:
            return entrada
        else:
            entrada = input("Nome inválido. Por favor, insira um texto não vazio: ")


def validar_entrada_preco_produto(entrada: str) -> float:
    while True:
        try:
            entrada = entrada.replace(",", ".")
            valor = float(entrada)
            if valor > 0:
                return valor
            else:
                entrada = input("Preço inválido. Por favor, insira um valor positivo: ")

        except ValueError:
            entrada = input("Preço inválido. Por favor, insira um valor positivo: ")


def validar_entrada_inativar_produto(entrada: str) -> bool:
    while True:
        try:
            entrada = entrada.strip().lower()

            if entrada == "inativar":
                return False
            else:
                entrada = input(
                    "Status inválido. Por favor, insira 'Inativar' para inativar o produto: "
                )

        except ValueError:
            entrada = input(
                "Status inválido. Por favor, insira 'Inativar' para inativar o produto: "
            )


def validar_entrada_id_produto(entrada: str) -> int:
    while True:
        try:

            if entrada.strip():
                entrada_validada = int(entrada)

                if entrada_validada <= 0:
                    entrada = input(
                        "ID inválido. Por favor, insira um número inteiro maior que zero: "
                    )
                else:
                    return entrada_validada

            else:
                entrada = input(
                    "ID inválido. Por favor, insira um número inteiro, sem vírgulas e sem pontos: "
                )

        except ValueError:
            entrada = input(
                "ID inválido. Por favor, insira um número inteiro, sem vírgulas e sem pontos: "
            )


def validar_dado_bruto_json(dados: Any) -> list[Produto] | None:
    if not isinstance(dados, list):
        print(
            "Erro: o conteúdo do arquivo JSON deve ser uma lista de produtos, o arquivo atual é inválido!"
        )
        print("")
        return None

    produtos = []

    for produto in dados:
        if not isinstance(produto, dict):
            print(
                "Erro: o conteúdo do arquivo JSON deve ser uma lista de produtos, o arquivo atual é inválido!"
            )
            print("")
            return None

        if not (
            isinstance(produto.get("produto_id"), int)
            and isinstance(produto.get("produto_nome"), str)
            and isinstance(produto.get("produto_preco"), (int, float))
            and isinstance(produto.get("produto_ativo"), bool)
        ):
            print(
                f"Erro: o produto com id {produto.get('produto_id', 'desconhecido')} possui dados corrompidos ou faltando, o arquivo JSON é inválido!"
            )
            print(
                "Erro: o conteúdo do arquivo JSON é uma lista, porém um dos elementos possui dados corrompidos!"
            )
            print("")
            return None

        produtos.append(Produto(**produto))

    return produtos
