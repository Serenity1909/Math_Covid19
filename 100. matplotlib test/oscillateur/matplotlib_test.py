from oscillateur import oscillation
import matplotlib.pyplot as plt
import json

osc = json.loads(open("oscillateurs", 'r').read())
mtx = [0.2, 0.2, 0.2, 0.2, 0.2]

x = [1, 2, 3, 4, 5]

# plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.grid(False)

for i in range(len(osc)):
    mtx2 = mtx.copy()

    ax.plot(x, oscillation(mtx2, osc[i], divide=100), alpha=0.3)


ax.plot(x, [0.2, 0.2, 0.2, 0.2, 0.2], linewidth=3, color="k")

plt.show()