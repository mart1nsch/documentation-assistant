
---------------------------------------------------------------------

**escreve_arquivos.py**
===============================
### Função que escreve dados em um arquivo Markdown.
### Permite criar o arquivo caso ele não exista, adicionando a documentação passada como parâmetro aos dados já existentes.

### Funções
* `escreve(diretorio_escrita: str, nome_arquivo: str, documentacao: str) -> None`: escreve documentação em um arquivo Markdown.

### Dependências
* `pathlib`

### Exemplos de uso
```python
escreve('C:\\Documentos', 'meu_documento', 'Aqui vai a minha documentação')
```
Esse exemplo irá criar ou abrir o arquivo 'meu_documento.md' no diretório especificado e adicionar a documentação passada como parâmetro.