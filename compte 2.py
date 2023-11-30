class GestionComptesBancaires:
    def __init__(self):
        # Initialisation des dictionnaires
        self.comptes = {}  # Associe à chaque numéro de compte son solde
        self.clients = {}  # Associe à chaque numéro de client son code secret
        self.clients_comptes = {}  # Associe à chaque numéro de client son numéro de compte

    def creer_compte(self, titulaire, numero_compte, solde_initial=0, code_secret=''):
        # Crée un nouveau compte et associe le client à ce compte
        self.comptes[numero_compte] = solde_initial
        self.clients_comptes[titulaire] = numero_compte
        self.clients[titulaire] = code_secret

    def modifier_mot_de_passe(self, titulaire, nouveau_mot_de_passe):
        # Modifie le mot de passe d'un client
        if titulaire in self.clients:
            self.clients[titulaire] = nouveau_mot_de_passe
            print("Mot de passe modifié avec succès.")
        else:
            print("Client non trouvé.")

    def afficher_solde(self, titulaire):
        # Affiche le solde d'un compte
        if titulaire in self.clients_comptes:
            numero_compte = self.clients_comptes[titulaire]
            solde = self.comptes[numero_compte]
            print(f"Solde du compte de {titulaire}: {solde}€.")
        else:
            print("Client non trouvé.")

    def deposer_argent(self, titulaire, montant):
        # Dépose de l'argent sur un compte
        if titulaire in self.clients_comptes:
            numero_compte = self.clients_comptes[titulaire]
            self.comptes[numero_compte] += montant
            print(f"{montant}€ déposés avec succès. Nouveau solde : {self.comptes[numero_compte]}€.")
        else:
            print("Client non trouvé.")

    def retirer_argent(self, titulaire, montant):
        # Retire de l'argent d'un compte
        if titulaire in self.clients_comptes:
            numero_compte = self.clients_comptes[titulaire]
            if self.comptes[numero_compte] >= montant:
                self.comptes[numero_compte] -= montant
                print(f"{montant}€ retirés avec succès. Nouveau solde : {self.comptes[numero_compte]}€.")
            else:
                print("Solde insuffisant.")
        else:
            print("Client non trouvé.")


# Exemple d'utilisation
gestionnaire = GestionComptesBancaires()

# Création de comptes
gestionnaire.creer_compte(titulaire="John Doe", numero_compte=1, solde_initial=1000, code_secret='566')
gestionnaire.creer_compte(titulaire="Jane Doe", numero_compte=2, solde_initial=500, code_secret='836')

# Menu de choix
while True:
    print("\nMenu:")
    print("1. Modifier son mot de passe")
    print("2. Afficher son solde")
    print("3. Déposer une somme d'argent")
    print("4. Retirer une somme d'argent")
    print("0. Quitter")

    choix = input("Choisissez une option (0-4): ")

    if choix == '1':
        titulaire = input("Entrez votre nom: ")
        nouveau_mot_de_passe = input("Entrez votre nouveau mot de passe: ")
        gestionnaire.modifier_mot_de_passe(titulaire, nouveau_mot_de_passe)

    elif choix == '2':
        titulaire = input("Entrez votre nom: ")
        gestionnaire.afficher_solde(titulaire)

    elif choix == '3':
        titulaire = input("Entrez votre nom: ")
        montant = float(input("Entrez la somme à déposer: "))
        gestionnaire.deposer_argent(titulaire, montant)

    elif choix == '4':
        titulaire = input("Entrez votre nom: ")
        montant = float(input("Entrez la somme à retirer: "))
        gestionnaire.retirer_argent(titulaire, montant)

    elif choix == '0':
        print("Merci d'avoir utilisé notre application. Au revoir!")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")
