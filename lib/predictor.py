from data.process import scale
import numpy as np
from kmodes.kprototypes import KPrototypes
import pickle
from dash import html

 


# It is important to use binary access
with open('lib/kproto6.pickle', 'rb') as f:
    km = pickle.load(f)


def predictor(array):

    cats = list(range(4,47))
    data = np.array([['0.9373207470646803', '0.5578861300061824', '0.6775102514642114',
        '-0.17361004280264897', '0.0', '1.0', '0.0', '0.0', '0.0', '0.0',
        '0.0', '0.0', '0.0', '1.0', '0.0', '0.0', '0.0', '0.0', '1.0',
        '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '1.0', '0.0', '0.0',
        '0.0', '0.0', '0.0', '1.0', '0.0', '0.0', '0.0', '0.0', '0.0',
        '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '6000.0',
        'Menos de $ 500.000', 'Menos de $ 500.000', 'RÍO MAGDALENA']])

   
    array2 = []
##  scaling variables
    array2 += [scale(array[0],"age")]
    array2 += [scale(array[1],"porcentaje_ingresos")]
    array2 += [scale(array[2],"faenas_por_mes")]
    array2 += [scale(array[3],"kg_por_faena")]

## Converting arrays in to dummies arrays
    array2 += getdummies(array[4],10)
    array2 += getdummies(array[5],17)
    array2 += getdummies(array[6],12)

## pasting last columns
    array2 += [array[7]]
    array2 += [array[8]]
    array2 += [array[9]]
    array2 += [array[10]]

    array2 = np.array([array2])

    predicts = km.predict(array2, categorical=cats)

    answer = ""

    if(predicts[0] == 0):
        answer = [html.H3("Resultado", className="tituloarraigo"),
                    html.Ul(
                    [html.Li("Sus pescadores tienen una edad minima de 43.0 y una edad maxima de 101.0."),
                    html.Li("Obtienen unos ingresos minimos de 15.0% y unos ingresos maximos de 100.0%."),
                    html.Li("Estos pescadores hacen un minimo de 4.0 faena(s) por mes y como maximo 31.0 al mes."),
                    html.Li("Pescando un minimo de 1.0 kg por faena y un maximo de 170.0. Logrando conseguir"), 
                    html.Li("un precio promedio minimo por kg de $1001.0 y un maximo de $30000.0.")])]

    elif(predicts[0] == 1):
        answer = [html.H3("Resultado", className="tituloarraigo"),
                    html.Ul(
                    [html.Li("Sus pescadores tienen una edad minima de 18.0 y una edad maxima de 93.0."),
                    html.Li("Obtienen unos ingresos minimos de 1.0% y unos ingresos maximos de 80.0%."),
                    html.Li("Estos pescadores hacen un minimo de 1.0 faena(s) por mes y como maximo 31.0 al mes."),
                    html.Li("Pescando un minimo de 1.0 kg por faena y un maximo de 180.0. Logrando conseguir"), 
                    html.Li("un precio promedio minimo por kg de $1001.0 y un maximo de $30000.0.")])]


    elif(predicts[0] == 2):
      answer = [html.H3("Resultado", className="tituloarraigo"),
                    html.Ul(
                    [html.Li("Sus pescadores tienen una edad minima de 18.0 y una edad maxima de 82.0."),
                    html.Li("Obtienen unos ingresos minimos de 2.0% y unos ingresos maximos de 100.0%."),
                    html.Li("Estos pescadores hacen un minimo de 1.0 faena(s) por mes y como maximo 31.0 al mes."),
                    html.Li("Pescando un minimo de 1.0 kg por faena y un maximo de 180.0. Logrando conseguir"), 
                    html.Li("un precio promedio minimo por kg de $1001.0 y un maximo de $30000.0.")])]

    elif(predicts[0] == 3):
        answer = [html.H3("Resultado", className="tituloarraigo"),
                    html.Ul(
                    [html.Li("Sus pescadores tienen una edad minima de 18.0 y una edad maxima de 51.0."),
                    html.Li("Obtienen unos ingresos minimos de 20.0% y unos ingresos maximos de 100.0%."),
                    html.Li("Estos pescadores hacen un minimo de 6.0 faena(s) por mes y como maximo 31.0 al mes."),
                    html.Li("Pescando un minimo de 1.0 kg por faena y un maximo de 168.0. Logrando conseguir"), 
                    html.Li("un precio promedio minimo por kg de $1001.0 y un maximo de $30000.0.")])]

    elif(predicts[0] == 4):
        answer = [html.H3("Resultado", className="tituloarraigo"),
                    html.Ul(
                    [html.Li("Sus pescadores tienen una edad minima de 18.0 y una edad maxima de 91.0."),
                    html.Li("Obtienen unos ingresos minimos de 3.0% y unos ingresos maximos de 100.0%."),
                    html.Li("Estos pescadores hacen un minimo de 1.0 faena(s) por mes y como maximo 30.0 al mes."),
                    html.Li("Pescando un minimo de 160.0 kg por faena y un maximo de 999.0. Logrando conseguir"), 
                    html.Li("un precio promedio minimo por kg de $1020.0 y un maximo de $30000.0.")])]

    elif(predicts[0] == 5):
        answer = [html.H3("Resultado", className="tituloarraigo"),
                    html.Ul(
                    [html.Li("Sus pescadores tienen una edad minima de 18.0 y una edad maxima de 94.0."),
                    html.Li("Obtienen unos ingresos minimos de 15.0% y unos ingresos maximos de 100.0%."),
                    html.Li("Estos pescadores hacen un minimo de 1.0 faena(s) por mes y como maximo 22.0 al mes."),
                    html.Li("Pescando un minimo de 1.0 kg por faena y un maximo de 180.0. Logrando conseguir"), 
                    html.Li("un precio promedio minimo por kg de $1001.0 y un maximo de $30000.0.")])]

    

    return answer

def getdummies(arr,lon):
    rango = list(range(1,lon+1,+1))
    respuesta = []
    for n in rango:
        if n in arr:
            respuesta += [1]
        else:
            respuesta += [0]
    return respuesta