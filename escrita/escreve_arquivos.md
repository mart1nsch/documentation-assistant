
---------------------------------------------------------------------

**Documentação Técnica do Arquivo: escreve_arquivos.py**

### Função `escreve`

#### Descrição

A função `escreve` é responsável por concatenar um texto aos dados já existentes em um arquivo. O arquivo deve estar localizado no diretório especificado e ter a extensão `.md`.

#### Parâmetros

*   `diretorio_escrita`: Diretório onde o arquivo será escrito.
    *   Tipo: `str`
    *   Obrigatório: Sim
*   `nome_arquivo`: Nome do arquivo sem a extensão (será adicionada automaticamente).
    *   Tipo: `str`
    *   Obrigatório: Sim
*   `documentacao`: Texto que será concatenado aos dados existentes no arquivo.
    *   Tipo: `str`
    *   Obrigatório: Sim

#### Retorno

A função não retorna nada (`None`).

### Exemplo de Uso

```python
escreve('C:\\diretorio\\', 'nome_arquivo', 'Este é um exemplo de texto.')
```

### Observações Importantes

*   A extensão do arquivo será automaticamente adicionada se o nome não incluir a extensão.
*   O diretório deve terminar com uma barra invertida (`\`) para garantir que o caminho seja correto.

**Requisitos**

*   Python 3.x (com o módulo `pathlib` habilitado)
*   Permissões de escrita no diretório especificado

**Limitações**

*   O arquivo deve ter a extensão `.md` para que possa ser editado.
*   Não é possível sobreescrever o conteúdo do arquivo, apenas concatenar novos dados.