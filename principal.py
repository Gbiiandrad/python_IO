arquivo_contatos = open('dados/contatos.csv', encoding='latin_1')

conteudo = arquivo_contatos.readlines()
print(conteudo)

for linha in conteudo:
    print(linha, end='')