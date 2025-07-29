import streamlit as st
import os

def login():
    st.sidebar.title("Login")
    user = st.sidebar.text_input("Usuário")
    password = st.sidebar.text_input("Senha", type="password")
    return user == os.getenv("APP_USER", "admin") and password == os.getenv("APP_PASS", "123")