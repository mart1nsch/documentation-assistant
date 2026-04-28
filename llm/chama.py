from ollama import chat

def resposta(texto_arquivo:str) -> str:
    '''
    Função que utiliza o Ollama localmente para gerar uma resposta de acordo com a entrada do usuário.
    '''
    prompt = 'Crie a documentação técnica do arquivo abaixo:\n' + texto_arquivo

    response = chat(
        model='llama3.1:8b',
        messages=[
            { 'role': 'system', 'content': 'Você é um assistente que cria documentações técnicas de arquivos de programação. Leia todo o arquivo que é enviado a você e retorne apenas a documentação técnica, nada mais. Escrava em formato para arquivos .md.' },
            { 'role': 'user', 'content': prompt }
        ],
    )
    
    return str(response.message.content)