import json

arr = []
# for a in range(0, 4, 1):
#     for b in range(0, 4, 1):
#         for c in range(0, 4, 1):
#             for d in range(0, 4, 1):
#                 for e in range(0, 4, 1):
#                     if((a-2) + (b-2) + (c-2) + (d-2) + (e-2) == 0):
#                         arr.append([(a-2), (b-2), (c-2), (d-2), (e-2)])

# Nouveaux oscillateurs car l'autre, plus précis... Génère encore trop de data
# avant à (0, 3, 1), j'ai du passer à (0, 2, 1) avec les 19 communes, sinon il y a trop de résultats
for a in range(0, 2, 1):
    for b in range(0, 2, 1):
        for c in range(0, 2, 1):
            for d in range(0, 2, 1):
                for e in range(0, 2, 1):
                    for f in range(0, 2, 1):
                        for g in range(0, 2, 1):
                            for h in range(0, 2, 1):
                                for i in range(0, 2, 1):
                                    for j in range(0, 2, 1):
                                        for k in range(0, 2, 1):
                                            for l in range(0, 2, 1):
                                                for m in range(0, 2, 1):
                                                    for n in range(0, 2, 1):
                                                        for o in range(0, 2, 1):
                                                            for p in range(0, 2, 1):
                                                                for q in range(0, 2, 1):
                                                                    for r in range(0, 2, 1):
                                                                        for s in range(0, 2, 1):
                                                                            if((a-1) + (b-1) + (c-1) + (d-1) + (e-1) + (f-1) + (g-1) + (h-1) + (i-1) + (j-1) + (k-1) + (l-1) + (m-1) + (n-1) + (o-1) + (p-1) + (q-1) + (r-1) + (s-1) == 0):
                                                                                arr.append([(a-1), (b-1), (c-1), (d-1), (e-1), (f-1), (g-1), (h-1), (i-1), (j-1), (k-1), (l-1), (m-1), (n-1), (o-1), (p-1), (q-1), (r-1), (s-1)])

print(arr)
print(len(arr))

file = open('oscillateurs', 'w', encoding='utf8')
file.write(json.dumps(arr))
file.close()

print("fin enregristrement")
