
---------------------------------------------------------------------

# Documentação Técnica do Arquivo: `escreve_arquivos.py`

## Sumário
1. [Introdução](#introducao)
2. [Função `escreve`](#funcaoescreve)
3. [Exceções e Erros](#excecoes-e-erros)

## Introdução
A função `escreve_arquivos.py` é um script que permite escrever arquivos com extensão `.md` em um diretório específico.

## Função `escreve`
### Descrição
A função `escreve` recebe três parâmetros:

*   `diretorio_escrita`: o diretório onde será criado ou atualizado o arquivo.
*   `nome_arquivo`: o nome do arquivo que será criado, sem extensão. A extensão `.md` é adicionada automaticamente.
*   `documentacao`: a documentação a ser escrita no arquivo.

### Parâmetros
| Parâmetro | Tipo    | Descrição                                                                                                                                                 |
| :-------- | :------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| diretorio_escrita | str     | O diretório onde será criado ou atualizado o arquivo. O caractere de escape invertido (`\`) é acrescentado automaticamente ao final do caminho, se não estiver presente. |
| nome_arquivo   | str     | O nome do arquivo que será criado, sem extensão. A extensão `.md` é adicionada automaticamente.                                                                |
| documentacao  | str     | A documentação a ser escrita no arquivo.                                                                                                                         |

### Retorno
A função `escreve` não retorna nenhum valor (tipo `None`).

## Exceções e Erros
Em caso de erro ao abrir ou escrever no arquivo, a função imprimirá uma mensagem de erro contendo a descrição do problema.

**Observação:** O script utiliza a biblioteca `pathlib` para lidar com caminhos e arquivos.