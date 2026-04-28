
---------------------------------------------------------------------

**Documentação Técnica do Arquivo chama.py**
=====================================

### Função resposta(texto_arquivo: str) -> str

#### Descrição
A função `resposta` utiliza o Ollama localmente para gerar uma resposta de acordo com a entrada do usuário.

#### Parâmetros
* `texto_arquivo`: A entrada do usuário que será utilizada para gerar a resposta. Deve ser um string.

#### Retorno
* Uma string contendo a resposta gerada pelo Ollama.

#### Função Interna chat(model: str, messages: list)
A função `chat` é chamada internamente e utiliza o modelo `llama3.1:8b`. Ela envia as seguintes mensagens:
+ Um prompt de sistema que descreve a tarefa a ser realizada.
+ O conteúdo do parâmetro `prompt`, que contém o texto do arquivo enviado para criar a documentação técnica.

#### Formato de Saída
A resposta gerada pelo Ollama é retornada em formato de string, representando a documentação técnica do arquivo original.