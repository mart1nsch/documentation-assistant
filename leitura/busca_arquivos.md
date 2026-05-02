
---------------------------------------------------------------------

**busca_arquivos.py**
===============================
### Função responsável por encontrar todos os arquivos permitidos dentro do diretório enviado.
### Busca por arquivos com extensões permitidas e ignora pastas proibidas.

### Funções
- `busca(diretorio: str) -> list[str | None]`: Encontra todos os arquivos permitidos em um diretório específico.

### Dependências
- `pathlib`: Biblioteca para manipulação de caminhos e pastas.
- `config.filtro.ARQUIVOS_PERMITIDOS` e `config.filtro.PASTAS_PROIBIDAS`: Listas de configurações que definem os arquivos permitidos e as pastas proibidas.

### Exemplos de uso
```python
# Buscar arquivos .txt no diretório atual
arquivos = busca('./')
for arquivo in arquivos:
    print(arquivo)

# Buscar arquivos .pdf em uma pasta específica, excluindo a pasta 'proibida'
arquivos = busca('/caminho/pasta')
for arquivo in arquivos:
    print(arquivo)
```