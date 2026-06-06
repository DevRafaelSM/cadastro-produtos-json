import json
import os
from typing import Any


def inicializar_sistema():
    if not os.path.exists("data"):
        os.makedirs("data")

    caminho_arquivo = "data/produtos.json"
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "w", encoding="utf-8") as file:
            file.write("[]")


def listar() -> list[dict[str, Any]] | None:
    with open("data/produtos.json", "r", encoding="utf-8") as file:
        conteudo = file.read().strip()
        if not conteudo:
            return []

        try:
            return json.loads(conteudo)

        except json.JSONDecodeError:
            return None


def salvar(produtos: list[Any]):
    produtos_dict = [produto.__dict__ for produto in produtos]
    with open("data/produtos.json", "w", encoding="utf-8") as file:
        json.dump(produtos_dict, file, indent=4)
