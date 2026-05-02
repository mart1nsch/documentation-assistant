
---------------------------------------------------------------------

**chama.py**
===============================
### Arquivo responsável por criar documentações técnicas de arquivos de programação.
### Chamada da função `resposta` para gerar a documentação técnica.

### Funções
*   `chama(system_prompt:str, user_prompt:str)`: Função que utiliza o modelo Llama 3.1 para gerar uma resposta baseada em um prompt do usuário.
*   `resposta(texto_arquivo:str) -> str`: Função responsável por criar a documentação técnica de acordo com o conteúdo do arquivo recebido.

### Dependências
*   Ollama (biblioteca necessária para o funcionamento das funções)
*   Subprocess (para reexecução da aplicação caso haja um erro de conexão)

### Exemplos de uso
```python
texto_arquivo = "Crie a documentação técnica do arquivo abaixo:\n Nome Arquivo: exemplo.py, Conteúdo: print('Olá Mundo')\n"
documento_tecnica = resposta(texto_arquivo)
print(documento_tecnica)
```
Esse exemplo usa o arquivo `exemplo.py` como entrada para a função `resposta`, gerando uma documentação técnica correspondente.