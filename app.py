import streamlit as st
import joblib
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import importlib


# Configurando a página
st.set_page_config(
    page_title="SmartWeather",
    page_icon=":cloud:",
    layout= 'wide'
)
with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home","Dashboards"],
        icons=["file-text","bi bi-clipboard-data"],
        menu_icon="list",
        default_index=0
    )

if selected == "Home":
    home = importlib.import_module("home")
    home.run()
elif selected == "Dashboards":
    dashboard = importlib.import_module("dash01")
    dashboard.run()