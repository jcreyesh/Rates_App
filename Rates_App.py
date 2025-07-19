
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as sl
import altair as alt

# wide_mode
sl.set_page_config(layout="wide")

try:
    file = sl.file_uploader("Cargar la base de datos.")
    if file is not None:
        data = pd.read_csv(file, encoding="latin-1")
        # df["Contrato"].fillna("", inplace = True)
        # sl.write(data)
    
    # Sidebar
    sl.title("Producción por Pozo Basada en datos de la CNH")
    # lista_cuencas = list(data.Cuenca.unique())
    # select_cuenca = sl.selectbox("Seleccion la Cuenca", lista_cuencas)
    
    # data_cuencas = data[data["Cuenca"] == select_cuenca]
    lista_campos = list(data.Contrato.unique())
    select_campo = sl.selectbox("Seleccione el Contrato o Asignación", lista_campos)
    
    data_pozos = data[data["Contrato"] == select_campo]
    lista_pozos = list(data_pozos.Pozo.unique())
    select_pozo = sl.selectbox("Seleccione el pozo", lista_pozos)
    
    df_pozo = data_pozos[data_pozos["Pozo"] == select_pozo]

    sl.write(df_pozo)
    
    # Plots
    def plot_oil(df, x, y, pozo):
        fig = px.line(df, x=x, y=y, markers=True, title="\t"*22 + f"{pozo} <br><sup>{df['Cuenca'].iloc[0]} - {df['Contrato'].iloc[0]}</sup>")
        fig.update_layout(title_x=0.4, title_y=0.85)
        fig.update_traces(line_color="#1F8A70")
        return sl.plotly_chart(fig)
    
    def plot_gas(df, x, y, pozo):
        fig = px.line(df, x=x, y=y, markers=True, title="\t"*22 + f"{pozo} <br><sup>{df['Cuenca'].iloc[0]} - {df['Contrato'].iloc[0]}</sup>")
        fig.update_layout(title_x=0.4, title_y=0.85)
        fig.update_traces(line_color="red")
        return sl.plotly_chart(fig)
    
    def plot_water(df, x, y, pozo):
        fig = px.line(df, x=x, y=y, markers=True, title="\t"*22 + f"{pozo} <br><sup>{df['Cuenca'].iloc[0]} - {df['Contrato'].iloc[0]}</sup>")
        fig.update_layout(title_x=0.4, title_y=0.85)
        fig.update_traces(line_color="blue")
        return sl.plotly_chart(fig)
    
    # Oil
    plot_oil(df_pozo, df_pozo["Fecha"], df_pozo["Qo_(Mbd)"], select_pozo)
    plot_oil(df_pozo, df_pozo["Fecha"], df_pozo["Qo_ac(Mbd)"], select_pozo)
    
    # Gas
    plot_gas(df_pozo, df_pozo["Fecha"], df_pozo["Qga_(MMpcd)"], select_pozo)
    # plot_gas(df_pozo, df_pozo["Fecha"], df_pozo["Qga_ac(MMpcd)"], select_pozo)
    
    # Water
    plot_water(df_pozo, df_pozo["Fecha"], df_pozo["Qw_(Mbd)"], select_pozo)
    # plot_water(df_pozo, df_pozo["Fecha"], df_pozo["Qw_ac(Mbd)"], select_pozo)
    
    # Non-associated Gas
    plot_gas(df_pozo, df_pozo["Fecha"], df_pozo["Qgna_(MMpcd)"], select_pozo)
    # plot_gas(df_pozo, df_pozo["Fecha"], df_pozo["Qgna_ac(MMpcd)"], select_pozo)
    
    # Condensed oil
    plot_gas(df_pozo, df_pozo["Fecha"], df_pozo["Cond_(Mbd)"], select_pozo)
    # plot_gas(df_pozo, df_pozo["Fecha"], df_pozo["Cond_ac(Mbd)"], select_pozo)

except:
    sl.write("Aún no se ha cargado la Base de Datos.")
