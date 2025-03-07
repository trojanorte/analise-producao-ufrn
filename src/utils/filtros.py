import streamlit as st

def criar_filtros(df):
    if df is None or df.empty:
        st.error("⚠️ O DataFrame está vazio! Verifique o carregamento dos dados.")
        return "Todos", "Todos", "Todos", "Todos", "Todos"

    aluno_selecionado = st.selectbox("🔍 Selecione um Aluno:", ["Todos"] + sorted(df["Aluno"].dropna().unique()))
    orientador_selecionado = st.selectbox("👨‍🏫 Selecione um Orientador:", ["Todos"] + sorted(df["Orientador"].dropna().unique()))
    ano_selecionado = st.selectbox("📆 Selecione um Ano de Ingresso:", ["Todos"] + sorted(df["Ano de Ingresso"].dropna().astype(str).unique()))
    tipo_producao_selecionado = st.selectbox("📄 Selecione o Tipo de Produção:", ["Todos"] + sorted(df["Tipo de Produção"].dropna().unique()))
    evento_selecionado = st.selectbox("🎭 Selecione o Evento:", ["Todos"] + sorted(df["Evento"].dropna().unique()))

    return aluno_selecionado, orientador_selecionado, ano_selecionado, tipo_producao_selecionado, evento_selecionado

def aplicar_filtros(df, aluno, orientador, ano, tipo_producao, evento):
    """Filtra os dados conforme os filtros selecionados."""
    df_filtrado = df.copy()

    if aluno != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Aluno"] == aluno]

    if orientador != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Orientador"] == orientador]

    if ano != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Ano de Ingresso"].astype(str) == ano]
    
    if tipo_producao != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Tipo de Produção"] == tipo_producao]
    
    if evento != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Evento"] == evento]

    return df_filtrado