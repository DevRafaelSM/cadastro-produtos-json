import json
from typing import Any


def listar() -> list[dict[str, Any]]:
    with open("data/produtos.json", "r", encoding="utf-8") as file:
        conteudo = file.read().strip()

        if not conteudo:
            return []

        return json.loads(conteudo)


def salvar(produtos: list[Any]):
    produtos_dict = [produto.__dict__ for produto in produtos]
    with open("data/produtos.json", "w", encoding="utf-8") as file:
        json.dump(produtos_dict, file, indent=4)
