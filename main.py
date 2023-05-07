from Conversion_Sciensano.script import jsonfilecreation
from Espérance_de_maximisation.EM import esperanceMaximisation

if __name__ == "__main__":
    # Création du fichier json avec les 5 communes
    jsonfilecreation()

    # Création de l'espérance de maximisation
    esperanceMaximisation()


