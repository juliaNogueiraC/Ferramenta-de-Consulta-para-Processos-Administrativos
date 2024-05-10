# Código para auxiliar em processos administrativos, para realizar consultas em uma grande quantidade de dados
def comparar_listas(arquivo1, arquivo2, encontrado_file, nao_encontrado_file):
    with open(arquivo1, 'r') as f1, open(arquivo2, 'r') as f2:
        # Ler os nomes do primeiro arquivo e converter para letras minúsculas
        nomes1 = {nome.strip().lower() for nome in f1.readlines()}

        # Ler os nomes do segundo arquivo e converter para letras minúsculas
        nomes2 = [nome.strip().lower() for nome in f2.readlines()]

    # Inicializar listas para nomes encontrados e não encontrados
    encontrados = []
    nao_encontrados = []

    # Comparar os nomes
    for nome in nomes2:
        if nome in nomes1:
            encontrados.append(nome)
        else:
            nao_encontrados.append(nome)

    # Salvar nomes encontrados em um arquivo
    with open(encontrado_file, 'w') as f:
        for nome in encontrados:
            f.write(nome + '\n')

    # Salvar nomes não encontrados em um arquivo
    with open(nao_encontrado_file, 'w') as f:
        for nome in nao_encontrados:
            f.write(nome + '\n')

# Arquivos de texto com os nomes
arquivo1 = 'lista1.txt'
arquivo2 = 'lista2.txt'
encontrado_file = 'nomes_encontrados.txt'
nao_encontrado_file = 'nomes_nao_encontrados.txt'

# Comparar as listas e salvar em arquivos
comparar_listas(arquivo1, arquivo2, encontrado_file, nao_encontrado_file)
