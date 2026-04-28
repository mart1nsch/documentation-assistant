from pathlib import Path
import os
from leitura.busca_arquivos import busca
from leitura.le_arquivos import le
from llm.chama import resposta
from escrita.escreve_arquivos import escreve

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
    
    print('*** Falha na busca de arquivos!')
    return 0

def testa_le_arquivos() -> int:
    '''
    Função que irá testar as funções de leitura de arquivos.
    '''
    arquivos_processados = le(busca((str(Path('.').absolute()) + r'\testes\arquivos')))
    
    if len(arquivos_processados) == 1:
        print('* Leitura de arquivos funcionando de acordo!')
        return 1

    print('*** Falha na leitura de arquivos!')
    return 0

def testa_llm() -> int:
    '''
    Função que testa o retorno da LLM via Ollama.
    '''
    arquivos = le(busca((str(Path('.').absolute()) + r'\testes\arquivos')))

    for i in arquivos:
        for _, j in i.items():
            ollama = resposta(j['content'])

    if ollama:
        print('* Resposta da LLM funcionando de acordo!')
        return 1

    print('*** Falha na resposta da LLM!')
    return 0

def testa_escrita() -> int:
    '''
    Função que testa a escrita de arquivos.
    '''
    p = Path('./testes/arquivos')

    try:
        os.remove('./testes/arquivos/teste.md')
    except FileNotFoundError as e:
        pass

    escreve(str(p.absolute()), 'teste.md', 'Teste 123456')

    arquivo_criado = Path('./testes/arquivos/teste.md')

    if arquivo_criado.is_file():
        print('* Escrita de arquivos funcionando de acordo!')
        return 1

    print('*** Falha na escrita de arquivos!')
    return 0

def testa_tudo() -> None:
    '''
    Função que irá testar todos os arquivos Python presentes neste projeto.
    '''
    num_testes = 0
    num_corretos = 0

    num_testes += 1
    num_corretos += testa_busca_arquivos()

    num_testes += 1
    num_corretos += testa_le_arquivos()

    num_testes += 1
    num_corretos += testa_llm()

    num_testes += 1
    num_corretos += testa_escrita()

    mostra_resultados(num_testes, num_corretos)

if __name__ == '__main__':
    testa_tudo()