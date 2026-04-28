import argparse, sys
from leitura.busca_arquivos import busca
from leitura.le_arquivos import le
from llm.chama import resposta
from escrita.escreve_arquivos import escreve

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('diretorio_leitura', help=r'Diretório onde os arquivos para documentação estão localizados. Ex: C:\Users\martin\Documents\llm')
    parser.add_argument('diretorio_escrita', help=r'Diretório onde as documentações serão salvas. Ex: C:\Users\martin\Documents\llm')
    args = parser.parse_args()

    if not args.diretorio_leitura:
        print('Diretório de leitura não informado.')
        sys.exit(1)
    if not args.diretorio_escrita:
        print('Diretório de escrita não informado.')
        sys.exit(1)

    arquivos_processados = le(busca(args.diretorio_leitura))
    
    for i in arquivos_processados:
        for key, value in i.items():
            prompt = 'Nome Arquivo: ' + key + ', Conteúdo: ' + value['content']
            resposta_llm = resposta(prompt)

            if args.diretorio_escrita == 'None':
                diretorio_escrita = i['path']
            else:
                diretorio_escrita = args.diretorio_escrita

            escreve(diretorio_escrita, key, resposta_llm)
        
if __name__ == '__main__':
    main()