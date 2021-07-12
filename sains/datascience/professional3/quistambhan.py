class Mamalia:
    def __init__(self, nama):
        self.__nama = nama
    def interaksi(self):
        print('Bersuara')

class Anjing(Mamalia):
    def interaksi(self):
        print('Guk')

class Manusia(Mamalia):
    pass

blacky = Anjing('Blacky')
toni = Manusia('Toni')
toni.interaksi()
blacky.interaksi()