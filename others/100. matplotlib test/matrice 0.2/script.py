import json
import matplotlib.pyplot as plt

file = open("RESULT_MATRICES.json", 'r', encoding='utf8').read()
data = json.loads(file)


x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []


for i in range(len(data)):
    # print(data[i][0][0])
    y1.append(data[i][0][0])
    y2.append(data[i][1][0])
    y3.append(data[i][2][0])
    y4.append(data[i][3][0])
    y5.append(data[i][4][0])
    x.append(i)


plt.style.use('_mpl-gallery')

fig, ax = plt.subplots()

ax.grid(False)

ax.scatter(x, y1, color="blue", alpha=0.3)
ax.scatter(x, y2, color="green", alpha=0.3)
ax.scatter(x, y3, color="red", alpha=0.3)
ax.scatter(x, y4, color="purple", alpha=0.3)
ax.scatter(x, y5, color="yellow", alpha=0.3)

plt.show()