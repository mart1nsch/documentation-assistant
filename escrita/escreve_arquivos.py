from pathlib import Path

def escreve(diretorio_escrita:str, nome_arquivo:str, documentacao:str) -> None:
    '''
    Função cujo objetivo é receber um texto e concatenar ele aos dados já existentes no arquivo.
    '''
    nome_arquivo = nome_arquivo.split('.')[0] + '.md'

    if not diretorio_escrita.endswith(r'\\'):
        diretorio_escrita += r'\\'

    p = Path((diretorio_escrita + nome_arquivo))

    try:
        with p.open(mode='a', encoding='utf-8') as f:
            texto = '\n---------------------------------------------------------------------\n\n' + documentacao
            f.write(texto)
    except Exception as e:
        print('Erro ao abrir ou escrever no arquivo.', str(e))