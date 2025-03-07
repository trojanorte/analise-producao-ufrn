import streamlit as st

def criar_filtros(df):
    if df is None or df.empty:
        st.error("⚠️ O DataFrame está vazio! Verifique o carregamento dos dados.")
        return "Todos", "Todos", "Todos"

    aluno_selecionado = st.selectbox("🔍 Selecione um Aluno:", ["Todos"] + sorted(df["Aluno"].dropna().unique()))
    orientador_selecionado = st.selectbox("👨‍🏫 Selecione um Orientador:", ["Todos"] + sorted(df["Orientador"].dropna().unique()))
    ano_selecionado = st.selectbox("📆 Selecione um Ano de Ingresso:", ["Todos"] + sorted(df["Ano de Ingresso"].dropna().astype(str).unique()))

    return aluno_selecionado, orientador_selecionado, ano_selecionado

def aplicar_filtros(df, aluno, orientador, ano):
    """Filtra os dados conforme os filtros selecionados."""
    df_filtrado = df.copy()

    if aluno != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Aluno"] == aluno]

    if orientador != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Orientador"] == orientador]

    if ano != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Ano de Ingresso"].astype(str) == ano]

    return df_filtrado
