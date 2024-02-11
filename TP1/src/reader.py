from Atleta import Atleta

def reader(filepath):
    lista_atletas = []

    file = open(filepath, 'r')

    linhas = file.readlines()
    for linha in linhas[1:]:
        linha_splitted = linha.strip().split(',')
        atleta = Atleta(*linha_splitted)
        
        lista_atletas.append(atleta)

    return lista_atletas
