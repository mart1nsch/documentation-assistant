from pathlib import Path
from config.filtro import ARQUIVOS_PERMITIDOS, PASTAS_PROIBIDAS

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