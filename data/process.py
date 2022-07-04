import pandas as pd


data = pd.read_csv("data/dataset_resumidos2.csv", sep=";", decimal=',', encoding='latin',low_memory=False)


def especies(cuencas):
    data2 = data.dropna(subset=['especies_pesca'])
    data2 = data2[["Cuenca","Arenca","bagre","Bagre_Rayado_Pintadillo","Blanquillo","Bocachico","Cachama","Capaz","Cucha o Cucho","Dientón_Comelón_Moino","Dorada_Mueluda","Madre bocachico_Pincho","Mojarra","Nicuro_Barbut","Pácora","Picuda","Tilapia","Vizcaina"]]

    data3 = data2[data2["Cuenca"].isin(cuencas)]

    data3 = data3.drop(["Cuenca"], axis=1).sum()*100/data2.drop(["Cuenca"], axis=1).count()
    data3 = data3.reset_index()
    data3.columns = ['Especie','Valor']
    data3['Especie'] = data3['Especie'].str.split('_').str[0]
    data3 = data3.sort_values(by=['Valor'], ascending=False)
    return data3 

def mapData(cuencas):
    data2 = data.dropna(subset=['lat'])
    data2 = data2[["Cuenca","lat","lon"]]

    data3 = data2[data2["Cuenca"].isin(cuencas)]

    data3 = data3.drop(["Cuenca"], axis=1)
    return data3

