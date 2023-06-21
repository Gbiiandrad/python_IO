try:
    arquivo_contatos = open('dados/contatos.csv', encoding='latin_1'mode='w+')

    for linha in arquivo_contatos:
        print(linha, end='')

except FileNotFoundError:
    print('Arquivo não encontrado!')

except PermissionError:
    print('Você não tem permissão de escrita!')

finally:
    arquivo_contatos.close()
