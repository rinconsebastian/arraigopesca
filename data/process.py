import pandas as pd
import numpy as np
import copy

data = pd.read_csv("data/dataset_resumidos2.csv", sep=";", decimal=',', encoding='latin',low_memory=False)
data['age'] = pd.Timestamp('now') - pd.to_datetime(data['fecha_nac'])
data['age'] = data['age'] /  np.timedelta64(1, 'Y')

def especies(cuencas,edad):
    data2 = copy.deepcopy(data)
    data2 = data2.dropna(subset=['especies_pesca'])
    data2 = data2[["age","Cuenca","Arenca","bagre","Bagre_Rayado_Pintadillo","Blanquillo","Bocachico","Cachama","Capaz","Cucha_o_Cucho","Dientón_Comelón_Moino","Dorada_Mueluda","Madre_bocachico_Pincho","Mojarra","Nicuro_Barbut","Pácora","Picuda","Tilapia","Vizcaina"]]

    data3 = data2[(data2["Cuenca"].isin(cuencas)) & (data2["age"] >= edad[0]) & (data2["age"] <= edad[1])]

    data3 = data3.drop(["Cuenca","age"], axis=1).sum()/data3.drop(["Cuenca","age"], axis=1).count()
    data3 = data3.reset_index()
    data3.columns = ['Especie','Valor']
    data3['Especie'] = data3['Especie'].str.split('_').str[0]
    data3 = data3.sort_values(by=['Valor'], ascending=False)
    return data3 

def mapData(cuencas,edad):
    data22 = copy.deepcopy(data)
    data22 = data22.dropna(subset=['lat'])
    data22 = data22[["age","Cuenca","lat","lon"]]

    data23 = data22[(data22["Cuenca"].isin(cuencas)) & (data22["age"] >= edad[0]) & (data22["age"] <= edad[1])]

    data23= data23[(data23["lat"] < 11.5) & (data23["lat"] > 2) & (data23["lon"] < -72)  & (data23["lon"] > -77) ]

    data23 = data23.drop(["Cuenca"], axis=1)
    return data23


def artes (cuencas, edad):
    data32 = data.dropna(subset=['lat'])
    data32 = data32[['_id',"age","Cuenca",'arpon', 'atarraya', 'boliche', 'chinchorra', 'chinchorro', 'congolo_canasta', 'linea_mano',
           'palangre', 'redes_enmalle', 'trampas_nasas', 'trasmallo']]
 
    data32 = data32[(data32["Cuenca"].isin(cuencas)) & (data32["age"] >= edad[0]) & (data32["age"] <= edad[1])]

    data33 = data32.drop(["Cuenca","age"], axis=1)

    artes_metodos3 = pd.melt(data33, id_vars=['_id'], value_vars=['arpon', 'atarraya', 'boliche', 'chinchorra', 'chinchorro', 'congolo_canasta', 'linea_mano', 'palangre', 'redes_enmalle', 'trampas_nasas', 'trasmallo'],
                      var_name='artes_metodos', value_name='artes_conteo')
    artes_metodos_gr = artes_metodos3.groupby(by=['artes_metodos']).sum()/artes_metodos3.groupby(by=['artes_metodos']).count()

    artes_metodos_gr = artes_metodos_gr.reset_index()
    artes_metodos_gr = artes_metodos_gr.sort_values(by=['artes_conteo'], ascending=False)
    return artes_metodos_gr

def months(cuencas,edad):
    meses  = data[["_id","Cuenca","age","meses_mayor_captura"]].dropna()

    meses = meses[(meses["Cuenca"].isin(cuencas)) & (meses["age"] >= edad[0]) & (meses["age"] <= edad[1])]

    meses = meses.drop(["age",'Cuenca'], axis=1)

    meses2 = meses["meses_mayor_captura"].str.split(' ', expand=True, n=11)
    meses = meses.join(meses2)
    meses = meses.drop("meses_mayor_captura",axis="columns")
    meses2 = meses.melt(id_vars=['_id']).dropna()

    meses2 = meses2.drop("variable",axis="columns")

    cat_dtype = pd.api.types.CategoricalDtype(categories=['Enero','Febrero','Marzo','Abril', 'Mayo', 'Junio', 'Julio','Agosto','Septiembre', 'Octubre', 'Noviembre', 'Diciembre'], ordered=True)
    meses2.value = meses2.value.astype(cat_dtype)

    cross = pd.crosstab([meses2["_id"]],meses2["value"])
    cross2 = cross.sum() /cross.count()
    cross2 = cross2.reset_index()
    cross2.columns = ["Mes","Valor"]


    return cross2

def ingresos(cuencas,edad):
    data5 = data.dropna(subset=['lat'])
    data5 = data5[["Cuenca","age", "porcentaje_ingresos"]]
    
    data5 = data5[(data5["Cuenca"].isin(cuencas)) & (data5["age"] >= edad[0]) & (data5["age"] <= edad[1])]
    
    data5 = data5.drop(["Cuenca","age"], axis=1)

    porcentaje_ingresos_str=data5['porcentaje_ingresos'].dropna(how='all')
    porcentaje_ingresos=porcentaje_ingresos_str.astype('int64')
    grupos_porcentaje_ingresos=porcentaje_ingresos.value_counts(bins=4)
    bins = [0, 25, 50, 75, 100]
    names = ["0-25", "25-50", "50-75", "75-100"]
    data5['porcentaje'] = pd.cut(porcentaje_ingresos, bins, labels = names)
    grupos_porcentaje_ingresos2=data5['porcentaje'].value_counts()

    gp = grupos_porcentaje_ingresos2.to_frame()
    gp = gp.reset_index()
    gp.columns = ["Rango", "Porcentaje"]
    gp["Porcentaje"] = (gp['Porcentaje'] / gp['Porcentaje'].sum())
    return gp


def scale(value,column):
    data2 = data.dropna(subset=[column])
    m = data2[column].mean()
    s= data2[column].std()
    return (value - m)/s
