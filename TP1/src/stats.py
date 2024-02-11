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
    escalao = {}

    min = 100
    max = 0

    for atleta in lista_atletas:
        idade = atleta.getIdade()
        if idade >= max:
            max = idade
        elif idade <= min:
            min = idade

    i = min
    while i <= max:
        intervalo = str(i) + '-' + str(i + 3)
        escalao[intervalo] = None
        i = i + 4

    for atleta in lista_atletas:
        idade = atleta.getIdade()

        for intervalo, _ in escalao.items():
            intervalo_int = intervalo.split("-")
            if int(intervalo_int[0]) <= idade <= int(intervalo_int[1]):
                if escalao[intervalo] == None:
                    escalao[intervalo] = [atleta.getPrimeiroNome() + ' ' + atleta.getUltimoNome()]
                else:
                    escalao[intervalo].append(atleta.getPrimeiroNome() + ' ' + atleta.getUltimoNome())
    
    return escalao