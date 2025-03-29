import streamlit as st
import pandas as pd
import numpy as np
import polars as pl
from src.dataloader import unique_states, df
from src.plots import make_bar_plot, make_choropleth
from millify import millify
def main():
   
    st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

    with st.sidebar:
        st.title('Population Dummy Dashboard')
    
        selected_states = st.selectbox('Select a state', unique_states, index=len(unique_states)-1)

        color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
        selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    # Dashboard Main Panel
    col = st.columns((3.5, 3.5, 1), gap='medium')
    with col[0]:
        st.markdown("## Top States with most population")
        st.plotly_chart(make_bar_plot(input_color_theme=selected_color_theme))
    with col[1]:
        st.markdown("## Overview of all US states")
        st.plotly_chart(make_choropleth(input_color_theme=selected_color_theme))
    with col[2]:
        st.markdown("#### Adult persons statistics")
        st.metric(label=selected_states, value=millify(df.filter(pl.col("states")==selected_states).select("age(18+)").to_series().item()))
        st.metric(label=selected_states, value=f'{df.filter(pl.col("states")==selected_states).select("age(18+) in %").to_series().item()} %')

if __name__ == "__main__":
    main()
