class Calculatrice:
    def __init__(self):
        self.historique = []

    def addition(self, a, b):
        resultat = a + b
        self.ajouter_historique(f"{a} + {b} = {resultat}")
        return resultat

    def soustraction(self, a, b):
        resultat = a - b
        self.ajouter_historique(f"{a} - {b} = {resultat}")
        return resultat

    def multiplication(self, a, b):
        resultat = a * b
        self.ajouter_historique(f"{a} * {b} = {resultat}")
        return resultat

    def division(self, a, b):
        if b != 0:
            resultat = a / b
            self.ajouter_historique(f"{a} / {b} = {resultat}")
            return resultat
        else:
            print("Division par zéro impossible.")
            return None

    def ajouter_historique(self, operation):
        self.historique.append(operation)

    def afficher_historique(self):
        print("\nHistorique des opérations :")
        for operation in self.historique:
            print(operation)


calc = Calculatrice()

while True:
    print("\nOpérations disponibles:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Afficher l'historique")
    print("6. Quitter")

    choix = input("Choisissez une opération : ")

    if choix == '6':
        break
    elif choix in ('1', '2', '3', '4'):
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))

        if choix == '1':
            resultat = calc.addition(a, b)
        elif choix == '2':
            resultat = calc.soustraction(a, b)
        elif choix == '3':
            resultat = calc.multiplication(a, b)
        elif choix == '4':
            resultat = calc.division(a, b)

        print(f"Résultat : {resultat}")
    elif choix == '5':
        calc.afficher_historique()
    else:
        print("Choix invalide. Veuillez choisir une opération valide")