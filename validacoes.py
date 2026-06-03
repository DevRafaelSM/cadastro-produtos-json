# nome não vazio
# preço positivo
# ID válido
# opção de menu válida, se desejar


from typing import Any


def validar_entrada_nome_produto(entrada: str) -> str:
    while True:
        if entrada.strip():
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
