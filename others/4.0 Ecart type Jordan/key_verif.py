from rsc.loadmatrix2 import loadmatrice


donnees = loadmatrice("COVID_5BXL.json")

for key in donnees:
    print(key)