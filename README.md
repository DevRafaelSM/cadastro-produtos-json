# Cadastro de Produtos

## Objetivo

Criar uma aplicação de linha de comando para cadastrar produtos com base em um arquivo JSON, permitindo ao usuário adicionar produtos, listar produtos existentes, buscar produtos por ID, alterar o preço de produtos cadastrados, inativar produtos e finalizar a sessão.

## Como executar

Abra o terminal, certifique-se de que está na raiz do projeto e rode o comando:

```bash
py main.py
```

## Funcionalidades

- Adicionar produtos no arquivo JSON;
- Listar todos os produtos presentes no arquivo JSON;
- Buscar produtos por ID;
- Alterar o preço de produtos ativos por ID;
- Inativar produtos por ID;
- Manter os dados salvos mesmo após o programa ser finalizado;
- Finalizar a execução do programa.

## Regras de validação

- **JSON:** caso a pasta ou o arquivo não existam, eles são criados automaticamente quando o programa é inicializado. Caso o arquivo exista, seu conteúdo precisa ser compatível com a estrutura esperada de `Produto`;
- **ID:** deve ser um número aleatório de 10 dígitos que não seja igual a nenhum ID já presente nos produtos do arquivo JSON;
- **Nome:** deve ser um texto não vazio e não pode ser igual ao nome de um produto já cadastrado;
- **Preço:** deve ser um número positivo;
- **Ativo:** deve ser um valor booleano, nascendo sempre como `true` no cadastro de um novo produto;
- **Atualização de preço:** só pode ser feita em produtos existentes e ativos;
- **Inativação:** não remove o produto do arquivo JSON, apenas altera seu status para inativo.

## Observações gerais

- O programa utiliza um arquivo JSON para manter os dados mesmo após a finalização da execução;
- O programa utiliza funções de formatação e validação para exibir valores de forma coerente;
- A inativação de produtos é lógica, ou seja, o produto permanece salvo no JSON.
