"""
Creation des matrices de transition de bases.

Ces matrices servent lors du premier round afin de sortir tout les écarts-type.
Elles remplacent la matrice médiane [0.2,..] et ses oscillations.

"""

import json

arr = []

for a in range(0,2,1):
    for b in range(0,2,1):
        for c in range(0, 2, 1):
            for d in range(0, 2, 1):
                for e in range(0, 2, 1):
                    r1 = a/2
                    r2 = b/2
                    r3 = c/2
                    r4 = d/2
                    r5 = e/2
                    if (r1 + r2 + r3 + r4 + r5 == 1):
                        arr.append([r1, r2, r3, r4, r5])

hsh = []
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            for l in range(len(arr)):
                for m in range(len(arr)):
                    hsh.append([arr[i], arr[j], arr[k], arr[l], arr[m]])
print(len(hsh))

hsh = json.dumps(hsh)
file = open('mtx_base', 'w', encoding='utf8')
file.write(hsh)
file.close()