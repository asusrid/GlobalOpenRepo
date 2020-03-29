import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata, xmydata, ymydata = [], [], [], []
ln1, = ax.plot([], [], 'b-')
ln2, = ax.plot([], [], 'r-')

data_spain_ccaa = pd.read_csv('/Users/alejandrosusillo/Downloads/serie_historica_acumulados.csv', sep=',')
data_spain_ccaa = data_spain_ccaa.drop(len(data_spain_ccaa) - 1)
data_spain_ccaa['Casos '] = data_spain_ccaa['Casos '].fillna(0)
data_spain_ccaa['Fallecidos'] = data_spain_ccaa['Fallecidos'].fillna(0)
data_MD = data_spain_ccaa[data_spain_ccaa['CCAA Codigo ISO'].isin(['MD'])][['Casos ', 'Fallecidos']].to_numpy().transpose().astype(int)
data_AN = data_spain_ccaa[data_spain_ccaa['CCAA Codigo ISO'].isin(['CT'])][['Casos ', 'Fallecidos']].to_numpy().transpose().astype(int)


# GET HEADERS FROM UI, X AND Y. GET THE MAXIMUM VALUE AMONG ALL THE GIVEN HEADERS. CREATE UNA LINE FOR EACH HEADER.


def init():

    ax.set_xlim(0, 15000)
    ax.set_ylim(0, 2000)
    return ln1,ln2,

def update(num, data_MD, data_AN, line1, line2):

    line1.set_data(data_MD[..., :num])
    line2.set_data(data_AN[..., :num])
    return ln1,ln2,

ani = FuncAnimation(fig, update , 50, fargs=(data_MD, data_AN, ln1, ln2), interval=100, init_func=init, blit=True)
plt.show()