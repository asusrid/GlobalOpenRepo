"""
=========================
Simple animation examples
=========================

This example contains two animations. The first is a random walk plot. The
second is an image animation.
"""

# ---------- FUNCIONAAAAAAAAAAAAAAAA


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

fig1 = plt.figure()

data_spain_ccaa = pd.read_csv('/Users/alejandrosusillo/Downloads/serie_historica_acumulados.csv', sep=',')

data_spain_ccaa = data_spain_ccaa.drop(len(data_spain_ccaa)-1)

data_spain_ccaa['Casos '] = data_spain_ccaa['Casos '].fillna(0)
data_spain_ccaa['Fallecidos'] = data_spain_ccaa['Fallecidos'].fillna(0)

data = data_spain_ccaa[data_spain_ccaa['CCAA Codigo ISO'].isin(['MD'])][['Casos ','Fallecidos']].to_numpy().transpose().astype(int)
#data = np.random.rand(2, 25)

l, = plt.plot([], [], 'r-')
plt.xlim(0, 10000)
plt.ylim(0, 2000)
plt.xlabel('Casos')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 50, fargs=(data, l),
                                   interval=100, blit=True)
plt.show()
