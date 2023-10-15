import matplotlib.pyplot as plt
import numpy as np

vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

xpoints = np.array(meses)
ypoints = np.array(vendas_meses)

plt.plot(xpoints, ypoints)
plt.show()