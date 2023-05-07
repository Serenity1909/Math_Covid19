import json

# Chargement des données contenues dans les .json calculés
path = ["result_MTX_P1.json", "result_MTX_P2.json", "result_MTX_P3.json", "result_MTX_P4.json"]
# Synthèse sur un seul dico :
data = {}
for dir in path:
    file = open(dir, "r", encoding='utf8').read()
    file = json.loads(file)
    for jour in file:
        # Condition si écart type pas trop grand (defaut 1000):
        if file[jour]['r'] < 1000:
            data[jour] = file[jour]['mtx']

sortie = open('excel_jordan.csv', 'w', encoding='utf8')
sep =";"
for jour in data:
    sortie.write(
        str(str(data[jour][0][0])) + sep +
        str(str(data[jour][0][1])) + sep +
        str(str(data[jour][0][2])) + sep +
        str(str(data[jour][0][3])) + sep +
        str(str(data[jour][0][4])) + sep +
        str(str(data[jour][1][0])) + sep +
        str(str(data[jour][1][1])) + sep +
        str(str(data[jour][1][2])) + sep +
        str(str(data[jour][1][3])) + sep +
        str(str(data[jour][1][4])) + sep +
        str(str(data[jour][2][0])) + sep +
        str(str(data[jour][2][1])) + sep +
        str(str(data[jour][2][2])) + sep +
        str(str(data[jour][2][3])) + sep +
        str(str(data[jour][2][4])) + sep +
        str(str(data[jour][3][0])) + sep +
        str(str(data[jour][3][1])) + sep +
        str(str(data[jour][3][2])) + sep +
        str(str(data[jour][3][3])) + sep +
        str(str(data[jour][3][4])) + sep +
        str(str(data[jour][4][0])) + sep +
        str(str(data[jour][4][1])) + sep +
        str(str(data[jour][4][2])) + sep +
        str(str(data[jour][4][3])) + sep +
        str(str(data[jour][4][4])) + sep +
        str("\n")
    )
sortie.close()
