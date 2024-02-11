import reader
import stats

filepath = '../data/emd.csv'
res_path = '../res/resultado.txt'

def printer(modalidades, aptos, inaptos, escalao):
    res_file = open(res_path, 'w')
    
    res_file.write('Modalidades: ' + str(modalidades) + '\n\n')
    res_file.write('Atletas aptos: ' + str(aptos) + '%\n')
    res_file.write('Atletas inaptos: ' + str(inaptos) + '%\n\n')
    res_file.write('Escaloes etarios: ' + '\n')
    for escalao, atletas in escalao.items():
        res_file.write('Escalao ' + str(escalao) + ': ' + str(atletas) + '\n')

def main():
    lista_atletas = reader.reader(filepath)

    modalidades = stats.modalidades(lista_atletas)
    aptos = stats.aptos(lista_atletas)
    inaptos = stats.inaptos(lista_atletas)
    escalao = stats.escalao(lista_atletas)

    printer(modalidades, aptos, inaptos, escalao)

if __name__ == "__main__":
    main()