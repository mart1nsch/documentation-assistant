
---------------------------------------------------------------------

**le_arquivos.py**
===============================
### Descrição sobre o que ela faz
Essa função recebe uma lista de arquivos, lê o texto deles e retorna um dicionário com o texto.

### Funções
- `le(arquivos:list) -> list[dict]`: Recebe uma lista de arquivos e retorna um dicionário com o conteúdo dos arquivos.

### Dependências
- `pathlib`: Módulo para manipulação de caminhos e arquivos

### Exemplos de uso
```python
arquivos = [Path('arquivo1.txt'), Path('arquivo2.txt')]
resultados = le(arquivos)
print(resultados)
```
Essa função utiliza a biblioteca `pathlib` para manipular os caminhos dos arquivos e ler o conteúdo deles. A função lê cada arquivo na lista, adicionando-o ao dicionário com o nome do arquivo, caminho e conteúdo do arquivo. Se houver alguma falha durante a leitura de um arquivo, uma mensagem de erro será impressa.