class Impulso(object):
    def __init__(self, grau, modulo):
        self.angnum = grau
        self.angrad = 0
        self.forca = modulo
        self.impulsovx = 0
        self.impulsovy = 0

    def veloc(self):
        self.angrad = converterGrausParaRad(self.angnum)
        self.impulsovx = -self.forca*coseno(self.angrad)
        self.impulsovy = -self.forca*seno(self.angnum)