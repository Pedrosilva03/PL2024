class Atleta:
    def __init__(self, idAtleta, index, dataEMD, primeiroNome, ultimoNome, idade, genero, morada, modalidade, clube, email, federado, resultado):
        self.idAtleta = idAtleta
        self.index = int(index)
        self.dataEMD = dataEMD
        self.primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome
        self.idade = int(idade) 
        self.genero = genero
        self.morada = morada
        self.modalidade = modalidade
        self.clube = clube
        self.email = email
        self.federado = federado
        self.resultado = resultado

    def getIdAtleta(self):
        return self.idAtleta

    def setIdAtleta(self, idAtleta):
        self.idAtleta = idAtleta

    def getIndex(self):
        return self.index

    def setIndex(self, index):
        self.index = index

    def getDataEMD(self):
        return self.dataEMD
    
    def setDataEMD(self, dataEMD):
        self.dataEMD = dataEMD

    def getPrimeiroNome(self):
        return self.primeiroNome

    def setPrimeiroNome(self, primeiroNome):
        self.primeiroNome = primeiroNome

    def getUltimoNome(self):
        return self.ultimoNome
    
    def setUltimoNome(self, ultimoNome):
        self.ultimoNome = ultimoNome

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getMorada(self):
        return self.morada

    def setMorada(self, morada):
        self.morada = morada

    def getModalidade(self):
        return self.modalidade

    def setModalidade(self, modalidade):
        self.modalidade = modalidade

    def getClube(self):
        return self.clube

    def setClube(self, clube):
        self.clube = clube

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getFederado(self):
        return self.federado

    def setFederado(self, federado):
        self.federado = federado

    def getResultado(self):
        return self.resultado

    def setResultado(self, resultado):
        self.resultado = resultado
