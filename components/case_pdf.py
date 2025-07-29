import streamlit as st
import pandas as pd

def case_pdf_app():
    st.title("Case: Extração de PDFs")
    st.write("Demonstração de extração automatizada de dados de documentos PDF de investidores.")

    data = {
        "Empresa": ["Invest Corp", "Capital X", "Alpha Ventures"],
        "E-mail Principal": ["contato@investcorp.com", "relacoes@capitalx.com", "alpha@ventures.com"],
        "Executivo": ["João Silva", "Maria Oliveira", "Carlos Souza"],
        "Cargo": ["Diretor", "CEO", "Analista"],
        "Email Gerado": ["joao@investcorp.com", "maria@capitalx.com", "carlos@ventures.com"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.download_button("Baixar Excel", df.to_csv(index=False), file_name="empresas_extraidas.csv")