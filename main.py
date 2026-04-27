import argparse, sys

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
    
    

if __name__ == '__main__':
    main()