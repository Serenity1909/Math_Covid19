"""
Test d'ouverture du fichier JSON issu de Sciensano concernant le covid 19
"""

import json

file = open("COVID19BE_CASES_MUNI.json", "r", encoding='utf8').read()
data = json.loads(file)

"""
Data (fichier JSON) est constitué comme suit:
C'est une list qui contient des dictionnaires.
Dans ces dictionnaires on sait accèder aux valeurs grace à ces clés :

NIS5
DATE
TX_DESCR_NL
TX_DESCR_FR
TX_ADM_DSTR_DESCR_NL
TX_ADM_DSTR_DESCR_FR
PROVINCE
REGION
CASES

"""

print(len(data))
print(type(data[2354]))
print(data[2354]["NIS5"])

