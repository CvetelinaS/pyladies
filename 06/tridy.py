class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutna!".format(self.jmeno, jidlo))

class Kotatko(Zviratko):
    
    def zamnoukej(self):
        print ("{}: Mnau!".format(self.jmeno))

    def snez(self, jidlo):
        print("{} na {} chvili kouka!".format(self.jmeno, jidlo))
        super().snez(jidlo)

class Stenatko(Zviratko):

    def zastekej(self):
        print ("{}: Haf!".format(self.jmeno))

kotatko = Kotatko('Micka')
kotatko.snez('ryba')
kotatko.zamnoukej()

stenatko = Stenatko('Jessie')
stenatko.snez('kost')
stenatko.zastekej()
