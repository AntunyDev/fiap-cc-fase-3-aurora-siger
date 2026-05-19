import plotly.express as px
import pandas as pd
import time

from data.dados_colonia import colonia

def gerar_grafico():
    ##Coleta de dados
    hist_e_eolica = colonia['historico']['eolica']['energia']
    hist_e_solar = colonia['historico']['solar']['energia']
    hist_e_total = [
        solar + eolica
        for solar, eolica in zip(hist_e_solar, hist_e_eolica)
    ]
    dias = list(range(1,len(hist_e_total) +1))

    ##Dataframe
    df = pd.DataFrame(
        {
            "Energia Solar": hist_e_solar,
            "Energia Eólica": hist_e_eolica,
            "Energia Total": hist_e_total
        },
        index=dias
    )
    df.index.name = "Dia"

    ##Geraçao de grafico
    fig = px.line(df, x = df.index, y = df.columns, markers=True, labels={
    "x":"Dias",
    "value":"Energia",
    "variable":"Tipo"
    })

    #Update geral
    fig.update_layout(
        title={
            "text": "⚡ Evolução da Produção Energética da Colônia Aurora",
            "font": {
                "size": 24
            },
            "x": 0.5,  # centraliza
            "xanchor": "center"
        },

        xaxis_title="Dias na colônia",
        yaxis_title="Energia Produzida",

        xaxis={
            "title_font": {"size": 18},
            "tickfont": {"size": 14}
        },

        yaxis={
            "title_font": {"size": 18},
            "tickfont": {"size": 14}
        },

        legend={
            "title": "Fontes",
            "font": {"size": 14}
        },

        width=1200,
        height=600,

        hovermode="x unified"
    )

    #Update dos eixos
    fig.update_xaxes(
        dtick=1,
        tickprefix = 'Dia '
    )
    fig.update_yaxes(
        ticksuffix = ' kWh'
    )

    #Update dos marcadores de legenda
    fig.update_traces(mode="markers+lines", hovertemplate=
    "<b>%{fullData.name}</b>"
    "<b>📅 Dia:</b> %{x}"
    "<br><b>⚡ Energia produzida: </b> %{y}"
    "<extra></extra>")
    fig.update_layout(hovermode="x unified")  # para exibir o resumo de todos os dados no período

    time.sleep(3)
    fig.show()
    return df
