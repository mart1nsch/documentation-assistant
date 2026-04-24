from pathlib import Path
from leitura.busca_arquivos import busca

def mostra_resultados(numero_total_testes:int, numero_corretos:int) -> None:
    print('\n---------- Resultado dos Testes ----------\n')
    print('Total de Testes:', numero_total_testes)
    print('Número de Testes Corretos:', numero_corretos)
    print('Percentual de Acertividade:', f'{round(((numero_corretos / numero_total_testes) * 100))}%')
    print('')

def testa_busca_arquivos() -> int:
    '''
    Função que irá testar as funções de busca de arquivos.
    '''
    p = Path('.')
    arquivos = busca((str(p.absolute()) + r'\testes\arquivos'))

    if len(arquivos) == 1:
        print('* Busca de arquivos funcionando de acordo!')
        return 1
    else:
        print('*** Falha na busca de arquivos!')
        return 0

def testa_tudo() -> None:
    '''
    Função que irá testar todos os arquivos Python presentes neste projeto.
    '''
    num_testes = 0
    num_corretos = 0

    num_testes += 1
    num_corretos += testa_busca_arquivos()

    mostra_resultados(num_testes, num_corretos)

testa_tudo()