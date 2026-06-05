def formatar_moeda(valor: float) -> str:
    return f"R$ {round(valor, 2):.2f}".replace(".", ",")


def formatar_status(valor: bool) -> str:
    return "Ativo" if valor else "Inativo"
