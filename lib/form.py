import dash_bootstrap_components as dbc
from dash import html

titulo = dbc.Row(
    [
        html.H3("Formulario de evaluación del arraigo", className="tituloarraigo")
    ],
    className="mb-3 inputform",
)

edad_input = dbc.Row(
    [
        dbc.Label("Edad", html_for="edad-row", width=6),
        dbc.Col(
            dbc.Input(
                type="number", id="edad-row", placeholder="Escriba la edad", min=18, max=120
            ),
            width=6,
        ),
    ],
    className="mb-3 inputform",
)

ingresos_input = dbc.Row(
    [dbc.Label("Porcentaje de sus ingresos que dependen de la actividad pesquera", html_for="ingresos-row", width=6),
        dbc.Col(
            dbc.Input(
                type="number", id="ingresos-row", placeholder="Escriba un valor entre 1 y 100 %", min=1, max=100
            ),
            width=6,
        ),
    ],
   className="mb-3 inputform",
)
faenas_input = dbc.Row(
    [dbc.Label("Cuantas faenas de pesca realiza por mes", html_for="faenas-row", width=6),
        dbc.Col(
            dbc.Input(
                type="number", id="faenas-row", placeholder="Escriba elnúmero de faenas", min=1, max=60
            ),
            width=6,
        ),
    ],
   className="mb-3 inputform",
)
kg_input = dbc.Row(
    [dbc.Label("Promedio de kilogramos capturados por faena de pesca", html_for="kg-row", width=6),
        dbc.Col(
            dbc.Input(
                type="number", id="kg-row", placeholder="Escriba el valor en kilogramos", min=1, max=1000
            ),
            width=6,
        ),
    ],
   className="mb-3 inputform",
)

ArtesChecklist = dbc.Row(
    [dbc.Label("Seleccione las artes de pesca que utiliza", width=6),
        dbc.Col(
        dbc.Checklist(
            options=[
                {"label": "arpon", "value": 1},
                {"label": "atarraya", "value": 2},
                {"label": "boliche", "value": 3},
                {"label": "chinchorra", "value": 4},
                {"label": "chinchorro", "value": 5},
                {"label": "congolo_canasta", "value": 6},
                {"label": "linea_mano", "value": 7},
                {"label": "palangre", "value": 8},
                {"label": "redes_enmalle", "value": 9},
                {"label": "trasmallo", "value": 10},
            ],
            value=[],
            id="artes-checklist-input",
            inline=True,
            
        ),
          width=6,
          
        ),
    ],
    className="mb-3 inputform",
)

EspeciesChecklist = dbc.Row(
    [dbc.Label("Seleccione las especies que captura el pescador", width=6),
        dbc.Col(
        dbc.Checklist(
            options=[
                {"label": "Arenca", "value": 1},
                {"label": "bagre", "value": 2},
                {"label": "Bagre_Rayado_Pintadillo", "value": 3},
                {"label": "Blanquillo", "value": 4},
                {"label": "Bocachico", "value": 5},
                {"label": "Cachama", "value": 6},
                {"label": "Capaz", "value": 7},
                {"label": "Cucha_o_Cucho", "value": 8},
                {"label": "Dientón_Comelón_Moino", "value": 9},
                {"label": "Dorada_Mueluda", "value": 10},
                {"label": "Madre_bocachico_Pincho", "value": 11},
                {"label": "Mojarra", "value": 12},
                {"label": "Nicuro_Barbut", "value": 13},
                {"label": "Pácora", "value": 14},
                {"label": "Picuda", "value": 15},
                {"label": "Tilapia", "value": 16},
                {"label": "Vizcaina", "value": 17},
            ],
            value=[],
            id="especies-checklist-input",
            inline=True,
            
        ),
          width=6,
          
        ),
    ],
    className="mb-3 inputform",
)

MesesChecklist = dbc.Row(
    [dbc.Label("Seleccione los meses de mayor captura de recurso pesquero", width=6),
        dbc.Col(
        dbc.Checklist(
            options=[
                {"label": "Enero", "value": 1},
                {"label": "Febrero", "value": 2},
                {"label": "Marzo", "value": 3},
                {"label": "Abril", "value": 4},
                {"label": "Mayo", "value": 5},
                {"label": "Junio", "value": 6},
                {"label": "Julio", "value": 7},
                {"label": "Agosto", "value": 8},
                {"label": "Septiembre", "value": 9},
                {"label": "Octubre", "value": 10},
                {"label": "Noviembre", "value": 11},
                {"label": "Diciembre", "value": 12},

            ],
            value=[],
            id="meses-checklist-input",
            inline=True,
            
        ),
          width=6,
          
        ),
    ],
    className="mb-3 inputform",
)

precio_input = dbc.Row(
    [dbc.Label("Precio promedio de venta de Kilogramo de pescado", html_for="precio-row", width=6),
        dbc.Col(
            dbc.Input(
                type="number", id="precio-row", placeholder="Escriba el valor en pesos", min=1000, max=30000
            ),
            width=6,
            
        ),
       
    ],
    className="mb-3 inputform",
)

ingresoprom_input = dbc.Row(
    [dbc.Label("Ingreso promedio mensual producto de la actividad pesquera", html_for="ingresoprom-row", width=6),
        dbc.Col(
            dbc.RadioItems(
            options=[
                {"label": "Menos de $ 500.000", "value": "Menos de $ 500.000"},
                {"label": "Entre $ 500.000 - $ 1'000.000", "value": "Entre $ 500.000 - $ 1'000.000"},
                {"label": "Entre $ 1'000.001 - $ 1'500.000", "value": "Entre $ 1'000.001 - $ 1'500.000"},
                {"label": "Entre $ 1'500.001 - $ 2'000.000", "value": "Entre $ 1'500.001 - $ 2'000.000"},
                {"label": "Entre $ 2'000.001 - $ 2'500.000", "value": "Entre $ 2'000.001 - $ 2'500.000"},
                {"label": "Entre $ 2'500.001 - $ 3'000.000", "value": "Entre $ 2'500.001 - $ 3'000.000"},
                {"label": "Entre $ 3'000.001 - $ 3'500.000", "value": "Entre $ 3'000.001 - $ 3'500.000"},
                {"label": "Entre $ 3'500.001 - $ 4'000.000", "value": "Entre $ 3'500.001 - $ 4'000.000"},
                {"label": "Más de $ 4'000.000", "value": "Más de $ 4'000.000"},

            ],
            value=1,
            id="ingresoprom-row",
            inline=True,
            ),
            width=6,
            
        ),
    ],
    className="mb-3 inputform",
)

gastoprom_input = dbc.Row(
    [dbc.Label("Gasto promedio mensual para realizar la actividad pesquera", html_for="gastoprom-row", width=6),
        dbc.Col(
            dbc.RadioItems(
            options=[
                {"label": "Menos de $ 500.000", "value": "Menos de $ 500.000"},
                {"label": "Entre $ 500.000 - $ 1'000.000", "value": "Entre $ 500.000 - $ 1'000.000"},
                {"label": "Entre $ 1'000.001 - $ 1'500.000", "value": "Entre $ 1'000.001 - $ 1'500.000"},
                {"label": "Entre $ 1'500.001 - $ 2'000.000", "value": "Entre $ 1'500.001 - $ 2'000.000"},
                {"label": "Entre $ 2'000.001 - $ 2'500.000", "value": "Entre $ 2'000.001 - $ 2'500.000"},
                {"label": "Entre $ 2'500.001 - $ 3'000.000", "value": "Entre $ 2'500.001 - $ 3'000.000"},
                {"label": "Entre $ 3'000.001 - $ 3'500.000", "value": "Entre $ 3'000.001 - $ 3'500.000"},
                {"label": "Entre $ 3'500.001 - $ 4'000.000", "value": "Entre $ 3'500.001 - $ 4'000.000"},
                {"label": "Más de $ 4'000.000", "value": "Más de $ 4'000.000"},

            ],
            value=1,
            id="gastoprom-row",
            inline=True,
            ),
            width=6,
            
        ),
    ],
    className="mb-3 inputform",
)

cuenca_input = dbc.Row(
    [dbc.Label("Cuenca en la que realiza su actividad pesquera", html_for="cuenca-row", width=6),
        dbc.Col(
            dbc.RadioItems(
            options=[
                {"label": "RÍO MAGDALENA", "value": "RÍO MAGDALENA"},
                {"label": "RÍO SAN JORGE", "value": "RÍO SAN JORGE"},
                {"label": "RÍO CAUCA", "value": "RÍO CAUCA"},
                {"label": "RÍO SINÚ", "value": "RÍO SINÚ"},
            ],
            value=1,
            id="cuenca-row",
            inline=True,
            ),
            width=6,
        ),
    ],
    className="mb-3 inputform",
)

submit_input  = dbc.Row(
    [dbc.Col(dbc.Button("Evaluar", color="primary", id="submit-button"), width="auto"),],
    className="mb-3",
)
form = dbc.Form([titulo,edad_input, ingresos_input,faenas_input, kg_input, ArtesChecklist,EspeciesChecklist, MesesChecklist, precio_input, ingresoprom_input, gastoprom_input, cuenca_input,submit_input])