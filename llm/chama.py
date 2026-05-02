from ollama import chat
import subprocess
import time

def chama(system_prompt:str, user_prompt:str):
    response = chat(
        model='llama3.1:8b',
        messages=[
            { 'role': 'system', 'content': system_prompt },
            { 'role': 'user', 'content': user_prompt }
        ],
    )
    return response

def resposta(texto_arquivo:str) -> str:
    '''
    Função que utiliza o Ollama localmente para gerar uma resposta de acordo com a entrada do usuário.
    '''
    system = '''Você é um assistente que cria documentações técnicas de arquivos de programação.
Leia todo o arquivo que é enviado a você e retorne apenas a documentação técnica, nada mais.
A documentação técnica deve seguir o seguinte formato:
**Nome do arquivo**
===============================
### Descrição sobre o que ela faz
### Funções
### Dependências
### Exemplos de uso
    '''
    prompt = 'Crie a documentação técnica do arquivo abaixo:\n' + texto_arquivo

    try:
        response = chama(system, prompt)
    except ConnectionError as e:
        subprocess.Popen(["ollama"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)
        response = chama(system, prompt)
    
    return str(response.message.content)