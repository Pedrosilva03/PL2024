import reader
import stats

filepath = '../data/emd.csv'

def printer(modalidades, aptos, inaptos, escalao):
    for a in modalidades:
        print(a)

    print(aptos)
    print(inaptos)

def main():
    lista_atletas = reader.reader(filepath)

    modalidades = stats.modalidades(lista_atletas)
    aptos = stats.aptos(lista_atletas)
    inaptos = stats.inaptos(lista_atletas)
    escalao = stats.escalao(lista_atletas)

    printer(modalidades, aptos, inaptos, escalao)

if __name__ == "__main__":
    main()