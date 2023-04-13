class Lampada():
    def __init__(self, status):
        self.ligada = status

    def liga(self):
        self.ligada = True
        return True

    def desliga(self):
        self.ligada = False
        return False

    def esta_ligada(self):
        status = self.ligada
        print(((False, True))[status])
        return status


lampada = Lampada(False)

lampada.liga()
print('A lâmpada está ligada?')
lampada.esta_ligada()
lampada.desliga()
print('A lâmpada ainda está ligada?')
lampada.esta_ligada()
