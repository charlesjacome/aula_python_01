import streamlit as st
import pandas as pd
from datetime import date

def fn_gravar_dados(p_st_nome, p_dt_nascimento, p_tipo_cliente):
    if p_dt_nascimento <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{p_st_nome},{p_dt_nascimento},{p_tipo_cliente}\n")
        st.session_state["fl_sucesso"] = True
    else:
        st.session_state["fl_sucesso"] = False

st.set_page_config( 
    page_title= "cadastro de clientes",
    page_icon="📗")

st.title("cadastro de clientes")

st.divider()

st_nome= st.text_input("Digite o nome do cliente",
                    key="nome_cliente")

dt_nascimento = st.date_input("Data Nascimento", format="DD/MM/YYYY")

tipo_cliente = st.selectbox(label="Pessoa", options=["Juridica", "Fisica"])

btn_cadastrar = st.button("cadastrar", on_click=fn_gravar_dados,
                          args=[st_nome, dt_nascimento, tipo_cliente])

if btn_cadastrar:
    if st.session_state["fl_sucesso"]:
        st.success("Gravado ok", icon="✅")
    else:
        st.error("Erro no cadastro", icon="❌")