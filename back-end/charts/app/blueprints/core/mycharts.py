import pandas as pd
import matplotlib.pyplot as plt
#plt.rcParams['animation.ffmpeg_path'] = '/Users/alejandrosusillo/opt/anaconda3/lib/python3.7/site-packages/ffmpeg'
import seaborn as sns
import numpy as np
import io
import matplotlib.animation as animation


from pandas.plotting import register_matplotlib_converters
from sklearn.datasets import load_breast_cancer
from matplotlib.animation import FuncAnimation



def makePlot():

    # Loading
    data = load_breast_cancer()
    breast_cancer_df = pd.DataFrame(data['data'])
    breast_cancer_df.columns = data['feature_names']
    breast_cancer_df['target'] = data['target']
    breast_cancer_df['diagnosis'] = [data['target_names'][x] for x in data['target']]
    feature_names= data['feature_names']

    corr = breast_cancer_df[list(feature_names)].corr(method='pearson')

    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    # here is the trick save your figure into a bytes object and you can afterwards expose it via flas
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


def linePlot(x, y, fileName, todoNaN):

    #warehouse/serie_historica_acumulados.csv
    # be aware of the array fileName in case we have more than one file
    data_spain_ccaa = pd.read_csv('/Users/alejandrosusillo/Downloads/serie_historica_acumulados.csv', sep=',') 

    # ASK THE USER WHAT TO DO WITH CERTAIN RECORDS!!!!!!!!!!!!!!!!!!!!!!!!!!
    data_spain_ccaa = data_spain_ccaa.drop(len(data_spain_ccaa)-1)
    # ASK THE USER WHAT TO DO WITH THE NAN VALUES
    data_spain_ccaa['Casos '] = data_spain_ccaa['Casos '].fillna(0)

    # get andalucia cases
    aux = data_spain_ccaa[data_spain_ccaa['CCAA Codigo ISO'].str.contains('AN')]
    # get those days that are even
    even_days = (pd.to_datetime(aux['Fecha']).dt.day)%2==0
    # get those records that are AN and even days
    data_spain_ccaa_AN = aux[aux['CCAA Codigo ISO'].str.contains('AN')][even_days]


    fig, ax = plt.subplots()

    ax.plot_date(data_spain_ccaa_AN['Fecha'], data_spain_ccaa_AN['Casos '], marker='', linestyle='-')
    fig.autofmt_xdate()

    #plt.plot(data_spain_ccaa_AN['Fecha'], data_spain_ccaa_AN['Casos '])
    plt.ylabel('Cases')
    plt.xlabel('Date')
    plt.show()

#def animatedLineplot(x, y, headers, fileName, todoNaN):
def animatedLineplot():

    fig, ax = plt.subplots()
    ln1, = ax.plot([], [], 'b-')
    ln2, = ax.plot([], [], 'r-')

    data_spain_ccaa = pd.read_csv('/warehouse/serie_historica_acumulados.csv', sep=',')
    data_spain_ccaa = data_spain_ccaa.drop(len(data_spain_ccaa) - 1)
    data_spain_ccaa['Casos '] = data_spain_ccaa['Casos '].fillna(0)
    data_spain_ccaa['Fallecidos'] = data_spain_ccaa['Fallecidos'].fillna(0)
    data_MD = data_spain_ccaa[data_spain_ccaa['CCAA Codigo ISO'].isin(['MD'])][
        ['Casos ', 'Fallecidos']].to_numpy().transpose().astype(int)
    data_AN = data_spain_ccaa[data_spain_ccaa['CCAA Codigo ISO'].isin(['CT'])][
        ['Casos ', 'Fallecidos']].to_numpy().transpose().astype(int)

    # GET HEADERS FROM UI, X AND Y. GET THE MAXIMUM VALUE AMONG ALL THE GIVEN HEADERS. CREATE UNA LINE FOR EACH HEADER.

    def init():
        ax.set_xlim(0, 15000)
        ax.set_ylim(0, 2000)
        return ln1, ln2,

    def update(num, data_MD, data_AN, line1, line2):
        line1.set_data(data_MD[..., :num])
        line2.set_data(data_AN[..., :num])
        return ln1, ln2,

    #Writer = animation.writers['ffmpeg']
    #writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

    ani = FuncAnimation(fig, update, 50, fargs=(data_MD, data_AN, ln1, ln2), interval=100, init_func=init, blit=True)
    return ani.to_html5_video()


def scatterPlot(x, y, headers, fileName, todoNaN):

    #warehouse/serie_historica_acumulados.csv
    # be aware of the array fileName in case we have more than one file
    data_spain_ccaa = pd.read_csv('/Users/alejandrosusillo/Downloads/serie_historica_acumulados.csv', sep=',')

    data_spain_ccaa = data_spain_ccaa.drop(len(data_spain_ccaa)-1)

    data_spain_ccaa['Casos '] = data_spain_ccaa['Casos '].fillna(0)
    data_spain_ccaa['Fallecidos'] = data_spain_ccaa['Fallecidos'].fillna(0)

    fig, ax = plt.subplots()

    ax.yaxis.grid(True)
    ax.set_title('Casos VS Fallecidos',fontsize=10)
    ax.set_xlabel('Casos',fontsize=10)
    ax.set_ylabel('Fallecidos',fontsize=10)

    X = data_spain_ccaa['Casos ']
    Y = data_spain_ccaa['Fallecidos']

    ax.scatter(X, Y)
    plt.show()







