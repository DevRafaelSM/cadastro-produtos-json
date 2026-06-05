from typing import Any


def validar_entrada_nome_produto(entrada: str, produtos: list) -> str:

    nomes_existentes = {produto.nome.lower() for produto in produtos}

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
                return int(entrada)
            else:
                entrada = input("ID inválido. Por favor, insira um texto não vazio: ")

        except ValueError:
            entrada = input(
                "ID inválido. Por favor, insira um número inteiro, sem vírgulas e sem pontos: "
            )
