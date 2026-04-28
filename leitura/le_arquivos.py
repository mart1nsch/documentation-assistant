from pathlib import Path

def le(arquivos:list) -> list[dict]:
    '''
    Função que recebe uma lista de arquivos, retira o texto deles e retorna um dicionário com o texto.
    O dicionário criado segue este padrão:
    {
        Nome Arquivo: {
            path: Caminho do diretório que o arquivo está salvo,
            content: Texto dentro do arquivo
        }
    }
    '''
    arquivos_processados = []

    for i in arquivos:
        try:
            p = Path(str(i))
            with p.open(encoding='utf-8') as f:
                arquivos_processados.append({ p.name: { 'path': str(p.parent), 'content': f.read() } })
        except Exception as e:
            print('Falha ao ler o arquivo. ', str(e))

    return arquivos_processados