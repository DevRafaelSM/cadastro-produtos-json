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
        produto_id = gerar_id_valido()
        produto_nome = validar_entrada_nome_produto(input("Nome: "))
        produto_preco = validar_entrada_preco_produto(input("Preço unitário: "))
        produto_ativo = True

        produto = Produto(
            id=produto_id, nome=produto_nome, preco=produto_preco, ativo=produto_ativo
        )

        self.itens.append(produto)
        salvar(self.itens)

        print("")


def cadastrar_produto(produtos: Produtos):
    produtos.adicionar_produto()


def mostrar_lista_produtos_console():
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


def buscar_produto_por_id():
    buscar_produtos()


def atualizar_preco():
    print("Atualizando preço do produto...")


def inativar_produto():
    print("Inativando produto...")


def gerar_id_valido():
    random_id = "".join(random.choices(string.digits, k=10))
    return int(random_id)
