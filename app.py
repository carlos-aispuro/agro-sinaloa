import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Agricultura de Sinaloa", layout="wide")
st.title("Producción agrícola de Sinaloa, 2011-2013")
st.caption("Fuente: SIAP. Valores en pesos corrientes.")


@st.cache_data
def cargar():
    return pd.read_csv("data/sinaloa_2011_2013.csv")


df = cargar()
anios_all = sorted(df["anio"].unique().tolist())
ciclos_all = sorted(df["ciclo"].unique().tolist())
mpios_all = sorted(df["municipio"].unique().tolist())

st.sidebar.header("Filtros")
anios = st.sidebar.multiselect("Año", anios_all, default=anios_all)
ciclos = st.sidebar.multiselect("Ciclo", ciclos_all, default=ciclos_all)
mpios = st.sidebar.multiselect("Municipio", mpios_all, default=mpios_all)

datos = df[df["anio"].isin(anios) & df["ciclo"].isin(ciclos) & df["municipio"].isin(mpios)]

if datos.empty:
    st.warning("No hay datos con esos filtros.")
    st.stop()

c1, c2, c3 = st.columns(3)
c1.metric("Valor (miles de millones de pesos)", f"{datos['valor'].sum() / 1e9:,.1f}")
c2.metric("Hectáreas sembradas", f"{datos['sembrada'].sum():,.0f}")
c3.metric("% siniestrado", f"{datos['siniestrada'].sum() / datos['sembrada'].sum() * 100:.1f}%")

top = (
    datos.groupby("cultivo")["valor"].sum().sort_values(ascending=False).head(10) / 1e9
).reset_index()
fig1 = px.bar(top, x="valor", y="cultivo", orientation="h",
              labels={"valor": "Miles de millones de pesos", "cultivo": ""},
              title="Top 10 cultivos por valor")
fig1.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig1)

perd = datos.groupby(["anio", "ciclo"])[["sembrada", "siniestrada"]].sum().reset_index()
perd["pct_siniestrada"] = perd["siniestrada"] / perd["sembrada"] * 100
fig2 = px.bar(perd, x="anio", y="pct_siniestrada", color="ciclo", barmode="group",
              labels={"anio": "Año", "pct_siniestrada": "% siniestrado"},
              title="Superficie siniestrada por año y ciclo")
fig2.update_xaxes(type="category")
st.plotly_chart(fig2)
