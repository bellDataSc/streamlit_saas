import streamlit as st
from components.login import login
from components.case_pdf import case_pdf_app

st.set_page_config(page_title="SaaS BI Platform", layout="wide")
if login():
    st.sidebar.title("Navegação")
    page = st.sidebar.radio("Ir para", ["Case de Extração PDF", "Simulação de Proposta"])
    if page == "Case de Extração PDF":
        case_pdf_app()
    elif page == "Simulação de Proposta":
        st.title("Simulador de Proposta")
        preco_base = st.slider("Número de usuários", 1, 100, 10)
        features = st.multiselect("Funcionalidades desejadas", ["Dashboards", "API personalizada", "Suporte 24/7"])
        valor_total = 500 + preco_base * 80 + len(features) * 300
        st.success(f"Valor estimado mensal: R$ {valor_total:,.2f}")
else:
    st.warning("Faça login para acessar o conteúdo.")