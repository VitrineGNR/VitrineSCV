import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="VitrineSCV - Sistema de Vendas",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("VitrineSCV - Sistema Completo de Vendas")
st.markdown("**Interface moderna para gestão comercial**")

# Menu lateral
st.sidebar.title("Menu Principal")
st.sidebar.markdown("---")

opcao = st.sidebar.selectbox(
    "Navegação:",
    ["🏠 Dashboard", "📋 Propostas", "👥 Client
