import pandas as pd
import numpy as np

data = pd.read_csv("data/dataset_resumidos2.csv", sep=";", decimal=',', encoding='latin',low_memory=False)
data['age'] = pd.Timestamp('now') - pd.to_datetime(data['fecha_nac'])
data['age'] = data['age'] /  np.timedelta64(1, 'Y')

def especies(cuencas,edad):
    data2 = data.dropna(subset=['especies_pesca'])
    data2 = data2[["age","Cuenca","Arenca","bagre","Bagre_Rayado_Pintadillo","Blanquillo","Bocachico","Cachama","Capaz","Cucha o Cucho","Dientón_Comelón_Moino","Dorada_Mueluda","Madre bocachico_Pincho","Mojarra","Nicuro_Barbut","Pácora","Picuda","Tilapia","Vizcaina"]]

    data3 = data2[(data2["Cuenca"].isin(cuencas)) & (data2["age"] >= edad[0]) & (data2["age"] <= edad[1])]

    data3 = data3.drop(["Cuenca","age"], axis=1).sum()*100/data2.drop(["Cuenca"], axis=1).count()
    data3 = data3.reset_index()
    data3.columns = ['Especie','Valor']
    data3['Especie'] = data3['Especie'].str.split('_').str[0]
    data3 = data3.sort_values(by=['Valor'], ascending=False)
    return data3 

def mapData(cuencas,edad):
    data2 = data.dropna(subset=['lat'])
    data2 = data2[["age","Cuenca","lat","lon"]]

    data3 = data2[(data2["Cuenca"].isin(cuencas)) & (data2["age"] >= edad[0]) & (data2["age"] <= edad[1])]


    data3 = data3.drop(["Cuenca"], axis=1)
    return data3

