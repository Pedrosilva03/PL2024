class Atleta:
    def __init__(self, idAtleta, index, dataEMD, primeiroNome, ultimoNome, idade, genero, morada, modalidade, clube, email, federado, resultado):
        self.idAtleta = idAtleta
        self.index = index
        self.dataEMD = dataEMD
        self.primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome
        self.idade = idade
        self.genero = genero
        self.morada = morada
        self.modalidade = modalidade
        self.clube = clube
        self.email = email
        self.federado = federado
        self.resultado = resultado

    def getIdAtleta(self):
        return self._idAtleta

    def setIdAtleta(self, idAtleta):
        self._idAtleta = idAtleta

    def getIndex(self):
        return self._index

    def setIndex(self, index):
        self._index = index

    def getDataEMD(self):
        return self._dataEMD
    
    def setDataEMD(self, dataEMD):
        self._dataEMD = dataEMD

    def getPrimeiroNome(self):
        return self._primeiroNome

    def setPrimeiroNome(self, primeiroNome):
        self._primeiroNome = primeiroNome

    def getUltimoNome(self):
        return self._ultimoNome
    
    def setUltimoNome(self, ultimoNome):
        self._ultimoNome = ultimoNome

    def getIdade(self):
        return self._idade

    def setIdade(self, idade):
        self._idade = idade

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getMorada(self):
        return self._morada

    def setMorada(self, morada):
        self._morada = morada

    def getModalidade(self):
        return self._modalidade

    def setModalidade(self, modalidade):
        self._modalidade = modalidade

    def getClube(self):
        return self._clube

    def setClube(self, clube):
        self._clube = clube

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getFederado(self):
        return self._federado

    def setFederado(self, federado):
        self._federado = federado

    def getResultado(self):
        return self._resultado

    def setResultado(self, resultado):
        self._resultado = resultado
