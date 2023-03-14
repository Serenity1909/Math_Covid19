"""
Creation des types de matrices de correllation différent
en gros toutes les matrices possible, tant que la ligne vaut 1
par exemple une ligne vaudrait 0, 0, 0, 0, 1, ou 0, 0, 0, 0.1, 9.9
"""

arr=[]
x = 10
for i in range(0, x, 1):
    for j in range(0, x, 1):
        for k in range(0, x, 1):
            for l in range(0, x, 1):
                for m in range(0, x, 1):
                    if i + j + k + l + m == x:
                        arr.append([i/10, j/10, k/10, l/10, m/10])

# Création direct dans les fichiers

# 1
file = open("MATRICE_SQUELETTE_1.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(0, int(len(arr)/12), 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 2
file = open("MATRICE_SQUELETTE_2.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12), int(len(arr)/12)*2, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 3
file = open("MATRICE_SQUELETTE_3.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12)*2, int(len(arr)/12)*3, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 4
file = open("MATRICE_SQUELETTE_4.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12)*3, int(len(arr)/12)*4, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 5
file = open("MATRICE_SQUELETTE_5.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12)*4, int(len(arr)/12)*5, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 6
file = open("MATRICE_SQUELETTE_6.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12)*5, int(len(arr)/12)*6, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 7
file = open("MATRICE_SQUELETTE_7.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12)*6, int(len(arr)/12)*7, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 8
file = open("MATRICE_SQUELETTE_8.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12)*7, int(len(arr)/12)*8, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 9
file = open("MATRICE_SQUELETTE_9.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12)*8, int(len(arr)/12)*9, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 10
file = open("MATRICE_SQUELETTE_10.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12)*9, int(len(arr)/12)*10, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 11
file = open("MATRICE_SQUELETTE_11.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12)*10, int(len(arr)/12)*11, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()

# 12
file = open("MATRICE_SQUELETTE_12.csv", "w", encoding='utf8')
file.write("")

index = 0
sep = ";"

for a in range(int(len(arr)/12)*11, int(len(arr)/12)*12, 1):
    for b in range(0, len(arr), 1):
        for c in range(0, len(arr), 1):
            for d in range(0, len(arr), 1):
                for e in range(0, len(arr), 1):
                    # matrice.append([arr[a], arr[b], arr[c], arr[d], arr[e]])
                    file.write(str(index) + sep)
                    file.write(str(arr[a][0]) + sep + str(arr[a][1]) + sep + str(arr[a][2]) + sep + str(arr[a][3]) + sep + str(arr[a][4]) + sep)
                    file.write(str(arr[b][0]) + sep + str(arr[b][1]) + sep + str(arr[b][2]) + sep + str(arr[b][3]) + sep + str(arr[b][4]) + sep)
                    file.write(str(arr[c][0]) + sep + str(arr[c][1]) + sep + str(arr[c][2]) + sep + str(arr[c][3]) + sep + str(arr[c][4]) + sep)
                    file.write(str(arr[d][0]) + sep + str(arr[d][1]) + sep + str(arr[d][2]) + sep + str(arr[d][3]) + sep + str(arr[d][4]) + sep)
                    file.write(str(arr[e][0]) + sep + str(arr[e][1]) + sep + str(arr[e][2]) + sep + str(arr[e][3]) + sep + str(arr[e][4]) + sep)
                    file.write('\n')
                    index = index + 1
file.close()