# cadastrar produto
# listar produtos
# buscar produto
# atualizar preço
# inativar produto
# verificar duplicidade de nome
# montar os dados de um novo produto


import random
import string

from formatadores import formatar_moeda, formatar_status
from produtos_repository import listar, salvar
from validacoes import (
    validar_entrada_ativar_desativar_produto,
    validar_entrada_id_produto,
    validar_entrada_nome_produto,
    validar_entrada_preco_produto,
)


class Produto:
    def __init__(
        self,
        id: int,
        nome: str,
        preco: float,
        ativo: bool,
    ):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.ativo = ativo


class Produtos:
    def __init__(
        self,
        itens: list[Produto] | None = None,
    ):
        self.itens = itens if itens is not None else []

    def adicionar_produto(self):
        data = listar()
        produtos = [Produto(**produto) for produto in data]

        produto_id = gerar_id_valido()
        produto_nome = validar_entrada_nome_produto(input("Nome: "))
        produto_preco = validar_entrada_preco_produto(input("Preço unitário: "))
        produto_ativo = True

        produto = Produto(
            id=produto_id, nome=produto_nome, preco=produto_preco, ativo=produto_ativo
        )

        produtos.append(produto)
        salvar(produtos)

        print("")


def listar_produtos():
    data = listar()
    produtos = [Produto(**produto) for produto in data]

    print("=============== Produtos ==============")

    if not produtos:
        print("Nenhum produto cadastrado...")
        print("")

        return

    for index, produto in enumerate(produtos):

        print(f"{index + 1}.  ", end="")

        print(f"ID: {produto.id}")
        print(f"    Nome: {produto.nome}")
        print(f"    Preço: {formatar_moeda(produto.preco)}")
        print(f"    Status: {formatar_status(produto.ativo)}")

        if index < len(produtos) - 1:
            print("---------------------------------------")

    print("")


def buscar_produtos():
    data = listar()
    produtos = [Produto(**produto) for produto in data]

    print("====== Busca de produtos por id =======")

    if not produtos:
        print("Nenhum produto cadastrado...")
        print("")

        return

    id_busca = validar_entrada_id_produto(
        input("Digite o ID do produto que deseja buscar: ")
    )

    produto_encontrado = next(
        (produto for produto in produtos if produto.id == id_busca), None
    )

    if produto_encontrado is not None:
        print("")
        print("========= Produto encontrado ==========")
        print("---------------------------------------")
        print(f"ID: {produto_encontrado.id}")
        print(f"Nome: {produto_encontrado.nome}")
        print(f"Preço: {formatar_moeda(produto_encontrado.preco)}")
        print(f"Status: {formatar_status(produto_encontrado.ativo)}")
        print("---------------------------------------")
        print("")
    else:
        print("Produto não encontrado.")
        print("")


def atualizar_preco():
    data = listar()
    produtos = [Produto(**produto) for produto in data]

    print("======== Atualização de preço =========")

    if not produtos:
        print("Nenhum produto cadastrado...")
        print("")

        return

    id_busca = validar_entrada_id_produto(
        input("Digite o ID do produto que deseja atualizar: ")
    )

    produto_encontrado = next(
        (produto for produto in produtos if produto.id == id_busca), None
    )

    if produto_encontrado is not None:
        print("")
        print("========= Produto encontrado ==========")
        print("---------------------------------------")
        print(f"ID: {produto_encontrado.id}")
        print(f"Nome: {produto_encontrado.nome}")
        print(f"Preço: {formatar_moeda(produto_encontrado.preco)}")
        print(f"Status: {formatar_status(produto_encontrado.ativo)}")
        print("---------------------------------------")

        produto_encontrado.preco = validar_entrada_preco_produto(
            input("Novo preço unitário: ")
        )

        salvar(produtos)

        print("Preço atualizado com sucesso!")
        print("")

    else:
        print("Produto não encontrado.")
        print("")


def inativar_produto():
    data = listar()
    produtos = [Produto(**produto) for produto in data]

    print("======= Inativação de produto =========")

    if not produtos:
        print("Nenhum produto cadastrado...")
        print("")

        return

    id_busca = validar_entrada_id_produto(
        input("Digite o ID do produto que deseja inativar: ")
    )

    produto_encontrado = next(
        (produto for produto in produtos if produto.id == id_busca), None
    )

    if produto_encontrado is not None:
        print("")
        print("========= Produto encontrado ==========")
        print("---------------------------------------")
        print(f"ID: {produto_encontrado.id}")
        print(f"Nome: {produto_encontrado.nome}")
        print(f"Preço: {formatar_moeda(produto_encontrado.preco)}")
        print(f"Status: {formatar_status(produto_encontrado.ativo)}")
        print("---------------------------------------")

        produto_encontrado.ativo = validar_entrada_ativar_desativar_produto(
            input("Novo status (Digite 'Inativar' ou 'Ativar'): ")
        )

        salvar(produtos)

        print("Status atualizado com sucesso!")
        print("")

    else:
        print("Produto não encontrado.")
        print("")


def gerar_id_valido():
    random_id = "".join(random.choices(string.digits, k=10))
    return int(random_id)
