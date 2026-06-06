class Produto:
    def __init__(
        self,
        produto_id: int,
        produto_nome: str,
        produto_preco: float,
        produto_ativo: bool,
    ):
        self.produto_id = produto_id
        self.produto_nome = produto_nome
        self.produto_preco = produto_preco
        self.produto_ativo = produto_ativo