import streamlit as st
import pandas as pd

st.set_page_config(page_title="Olympics Analysis", layout="wide")
st.title("Olympic Medals Visualizations")

st.image("fig_gen.png", caption="Male and Female Won Medals over the Years")
col1, col2 = st.columns(2)
with col1:
    st.image("fig_top10.png", caption="Top 10 Countries with the Most Gold Medals")
with col2:
    st.image("fig_SVK.png", caption="Medals in Each Sport")