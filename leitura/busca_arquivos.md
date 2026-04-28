
---------------------------------------------------------------------

**Busca Arquivos**
================

### Arquivo: `busca_arquivos.py`

#### Conteúdo

```python
from pathlib import Path
from config.filtro import ARQUIVOS_PERMITIDOS, PASTAS_PROIBIDAS
```

### Função `busca`

Encontra todos os arquivos permitidos dentro do diretório enviado.

**Parâmetros**

* `diretorio`: Caminho absoluto para o diretório a ser procurado.
* Tipo: `str`
* Retorno: Lista de caminhos absolutos para os arquivos encontrados.

**Exemplo de Uso**
```python
arquivos_encontrados = busca('/path/ao/diretorio')
print(arquivos_encontrados)
```

### Implementação

```python
def busca(diretorio:str) -> list[str | None]:
    '''
    Função responsável por encontrar todos os arquivos permitidos dentro do diretório enviado.
    '''
    p = Path(diretorio)

    arquivos = []

    for i in ARQUIVOS_PERMITIDOS:
        arquivos_encontrados = [
            arquivo for arquivo in p.rglob(('*' + i))
            if not any(pasta in arquivo.parts for pasta in PASTAS_PROIBIDAS)
        ]
        arquivos += arquivos_encontrados

    return arquivos
```

### Descrição da Implementação

1. O parâmetro `diretorio` é convertido para um objeto `Path` usando a biblioteca `pathlib`.
2. Uma lista vazia `arquivos` é criada para armazenar os caminhos dos arquivos encontrados.
3. Para cada arquivo permitido (`ARQUIVOS_PERMITIDOS`), uma lista de arquivos é gerada procurando por esse nome no diretório e subdiretórios usando o método `rglob`.
4. A list comprehension filtra os arquivos para excluir aqueles que estão em pastas proibidas (`PASTAS_PROIBIDAS`).
5. Os arquivos encontrados são adicionados à lista `arquivos`.
6. A função retorna a lista de caminhos dos arquivos encontrados.

### Considerações Finais

A função `busca` é projetada para encontrar arquivos permitidos dentro de um diretório específico, seguindo as regras definidas em `ARQUIVOS_PERMITIDOS` e `PASTAS_PROIBIDAS`. O uso dessa função deve ser feito com cautela, garantindo que os parâmetros sejam válidos e os resultados sejam interpretados corretamente.