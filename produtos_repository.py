# ler produtos do arquivo
# salvar produtos no arquivo
# garantir que o arquivo exista
# garantir que a pasta data exista, se necessário

# json.load(): Lê
# json.dump(): Salva

import json
from typing import Any

# from produtos_service import Produto


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
