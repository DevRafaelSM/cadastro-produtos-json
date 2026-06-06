import random
import string

from formatadores import formatar_moeda, formatar_status
from models import Produto
from produtos_repository import listar, salvar
from validacoes import (
    validar_dado_bruto_json,
    validar_entrada_id_produto,
    validar_entrada_inativar_produto,
    validar_entrada_nome_produto,
    validar_entrada_preco_produto,
)


def adicionar_produto():
    data = listar()
    produtos = validar_dado_bruto_json(data)
    if produtos is None:
        return

    produto_id = gerar_id_valido(produtos)
    produto_nome = validar_entrada_nome_produto(input("Nome: "), produtos)
    produto_preco = validar_entrada_preco_produto(input("Preço unitário: "))
    produto_ativo = True

    produto = Produto(
        produto_id=produto_id,
        produto_nome=produto_nome,
        produto_preco=produto_preco,
        produto_ativo=produto_ativo,
    )

    produtos.append(produto)
    salvar(produtos)

    print("")


def listar_produtos():
    data = listar()
    produtos = validar_dado_bruto_json(data)
    if produtos is None:
        return

    print("=============== Produtos ==============")

    if not produtos:
        print("Nenhum produto cadastrado...")
        print("")

        return

    for index, produto in enumerate(produtos):

        print(f"{index + 1}.  ", end="")

        print(f"ID: {produto.produto_id}")
        print(f"    Nome: {produto.produto_nome}")
        print(f"    Preço: {formatar_moeda(produto.produto_preco)}")
        print(f"    Status: {formatar_status(produto.produto_ativo)}")

        if index < len(produtos) - 1:
            print("---------------------------------------")

    print("")


def buscar_produtos():
    data = listar()
    produtos = validar_dado_bruto_json(data)
    if produtos is None:
        return

    print("====== Busca de produtos por id =======")

    if not produtos:
        print("Nenhum produto cadastrado...")
        print("")

        return

    id_busca = validar_entrada_id_produto(
        input("Digite o ID do produto que deseja buscar: ")
    )

    produto_encontrado = next(
        (produto for produto in produtos if produto.produto_id == id_busca), None
    )

    if produto_encontrado is not None:
        print("")
        print("========= Produto encontrado ==========")
        print("---------------------------------------")
        print(f"ID: {produto_encontrado.produto_id}")
        print(f"Nome: {produto_encontrado.produto_nome}")
        print(f"Preço: {formatar_moeda(produto_encontrado.produto_preco)}")
        print(f"Status: {formatar_status(produto_encontrado.produto_ativo)}")
        print("---------------------------------------")
        print("")
    else:
        print("Produto não encontrado.")
        print("")


def atualizar_preco():
    data = listar()
    produtos = validar_dado_bruto_json(data)
    if produtos is None:
        return

    print("======== Atualização de preço =========")

    if not produtos:
        print("Nenhum produto cadastrado...")
        print("")

        return

    id_busca = validar_entrada_id_produto(
        input("Digite o ID do produto que deseja atualizar: ")
    )

    produto_encontrado = next(
        (produto for produto in produtos if produto.produto_id == id_busca),
        None,
    )

    if produto_encontrado is not None and produto_encontrado.produto_ativo == False:
        print("")
        print("O produto informado está inativo, não é possível atualizar o preço.")
        print("")

    elif produto_encontrado is not None:
        print("")
        print("========= Produto encontrado ==========")
        print("---------------------------------------")
        print(f"ID: {produto_encontrado.produto_id}")
        print(f"Nome: {produto_encontrado.produto_nome}")
        print(f"Preço: {formatar_moeda(produto_encontrado.produto_preco)}")
        print(f"Status: {formatar_status(produto_encontrado.produto_ativo)}")
        print("---------------------------------------")

        produto_encontrado.produto_preco = validar_entrada_preco_produto(
            input("Novo preço unitário: ")
        )

        salvar(produtos)

        print("Preço atualizado com sucesso!")
        print("")

    else:
        print("Produto não encontrado ou inativo.")
        print("")


def inativar_produto():
    data = listar()
    produtos = validar_dado_bruto_json(data)
    if produtos is None:
        return

    print("======= Inativação de produto =========")

    if not produtos:
        print("Nenhum produto cadastrado...")
        print("")

        return

    id_busca = validar_entrada_id_produto(
        input("Digite o ID do produto que deseja inativar: ")
    )

    produto_encontrado = next(
        (
            produto
            for produto in produtos
            if produto.produto_id == id_busca and produto.produto_ativo == True
        ),
        None,
    )

    if produto_encontrado is not None:
        print("")
        print("========= Produto encontrado ==========")
        print("---------------------------------------")
        print(f"ID: {produto_encontrado.produto_id}")
        print(f"Nome: {produto_encontrado.produto_nome}")
        print(f"Preço: {formatar_moeda(produto_encontrado.produto_preco)}")
        print(f"Status: {formatar_status(produto_encontrado.produto_ativo)}")
        print("---------------------------------------")

        produto_encontrado.produto_ativo = validar_entrada_inativar_produto(
            input("Novo status (Digite 'Inativar' para inativar o produto): ")
        )

        salvar(produtos)

        print("Status atualizado com sucesso!")
        print("")

    else:
        print("Produto não encontrado ou já inativo.")
        print("")


def gerar_id_valido(produtos: list[Produto]) -> int:
    lista_ids_existente = {produto.produto_id for produto in produtos}

    while True:
        random_id = int("".join(random.choices(string.digits, k=10)))

        if random_id not in lista_ids_existente:
            return random_id
