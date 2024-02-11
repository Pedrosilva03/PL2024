def modalidades(lista_atletas):
    lista_modalidades = []

    for atleta in lista_atletas:
        modalidade = atleta.getModalidade()
        if modalidade not in lista_modalidades:
            lista_modalidades.append(modalidade)

    lista_modalidades.sort()
    return lista_modalidades

def aptos(lista_atletas):
    aptos = 0
    for atleta in lista_atletas:
        if atleta.getResultado() == "true":
            aptos = aptos + 1
    
    return (aptos / len(lista_atletas)) * 100

def inaptos(lista_atletas):
    inaptos = 0
    for atleta in lista_atletas:
        if atleta.getResultado() == 'false':
            inaptos = inaptos + 1
    
    return (inaptos / len(lista_atletas)) * 100

def escalao(lista_atletas):
    return