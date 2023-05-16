file = open("RESULT_MATRICES.json", "r", encoding='utf8').read()
rajout = "var data = "

ss = rajout + file + ";"

sortie = open("data.js", "w", encoding="utf8")
sortie.write(ss)
sortie.close()