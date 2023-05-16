import json

arr = []
for a in range(0, 4, 1):
    for b in range(0, 4, 1):
        for c in range(0, 4, 1):
            for d in range(0, 4, 1):
                for e in range(0, 4, 1):
                    if((a-2) + (b-2) + (c-2) + (d-2) + (e-2) == 0):
                        arr.append([(a-2), (b-2), (c-2), (d-2), (e-2)])
print(arr)
print(len(arr))

file = open('oscillateurs', 'w', encoding='utf8')
file.write(json.dumps(arr))
file.close()