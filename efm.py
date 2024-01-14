from datetime import datetime

class IR:
    _tranches = [28000, 40000, 50000, 60000, 150000]
    _tauxIR = [0, 12, 24, 34, 38, 40]

    @staticmethod
    def getIR(salaire):
        for i in range(len(IR._tranches)):
            if salaire <= IR._tranches[i]:
                return IR._tauxIR[i] / 100

class IEmploye:
    def Age(self):
        pass

    def Anciennete(self):
        pass

    def DateRetraite(self, ageRetraite):
        pass

class Employe(IEmploye):
    _mtle_auto_increment = 0

    def _init_(self, nom, date_naissance, date_embauche, salaire_base):
        self._mtle = Employe._mtle_auto_increment
        Employe._mtle_auto_increment += 1
        self._nom = nom
        self._dateNaissance = datetime.strptime(date_naissance, "%Y-%m-%d")
        self._dateEmbauche = datetime.strptime(date_embauche, "%Y-%m-%d")
        self._salaireBase = salaire_base

        
        if self.Age() < 16:
            raise ValueError("L'employé ne peut pas être recruté avant l'âge de 16 ans.")

    def DateEmbauche(self):
        return self._dateEmbauche

    def DateNaissance(self):
        return self._dateNaissance

    def Age(self):
        today = datetime.now()
        return today.year - self._dateNaissance.year - ((today.month, today.day) < (self._dateNaissance.month, self._dateNaissance.day))

    def Anciennete(self):
        today = datetime.now()
        return today.year - self._dateEmbauche.year - ((today.month, today.day) < (self._dateEmbauche.month, self._dateEmbauche.day))

    def DateRetraite(self, ageRetraite):
        return self._dateNaissance.year + ageRetraite

    def SalaireAPayer(self):
        pass

    def _eq_(self, other):
        return self._mtle == other._mtle

    def _lt_(self, other):
        return self._nom < other._nom

    def _str_(self):
        return f"{self._mtle}-{self._nom}-{self._dateNaissance.strftime('%Y-%m-%d')}-{self._dateEmbauche.strftime('%Y-%m-%d')}-{self._salaireBase}"

class Formateur(Employe):
    def _init_(self, nom, date_naissance, date_embauche, salaire_base, heure_sup=0, remuneration_hsup=70.00):
        super()._init_(nom, date_naissance, date_embauche, salaire_base)
        self._heureSup = heure_sup
        self._remunerationHSup = remuneration_hsup

    def SalaireAPayer(self):
        taux_ir = IR.getIR(self._salaireBase + self._heureSup * self._remunerationHSup)
        salaire_net = (self._salaireBase + self._heureSup * self._remunerationHSup) * (1 - taux_ir)
        return salaire_net

    def _str_(self):
        return f"{super()._str_()}-{self._heureSup}-{self._remunerationHSup}"

class Agent(Employe):
    def _init_(self, nom, date_naissance, date_embauche, salaire_base, prime_responsabilite):
        super()._init_(nom, date_naissance, date_embauche, salaire_base)
        self._primeResponsabilite = prime_responsabilite

    def SalaireAPayer(self):
        taux_ir = IR.getIR(self._salaireBase + self._primeResponsabilite)
        salaire_net = (self._salaireBase + self._primeResponsabilite) * (1 - taux_ir)
        return salaire_net

    def _str_(self):
        return f"{super()._str_()}-{self._primeResponsabilite}"
