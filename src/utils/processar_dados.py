import streamlit as st
import pandas as pd
import utils.filtros as filtros
import utils.graficos as graficos
import utils.extrair_informacoes as extrair

# 📌 Carregar os dados
file_path = "c:/Users/allys/OneDrive/Documentos/GitHub/analise producao ufrn/data/alunos_com_lattes.csv"
df = pd.read_csv(file_path, sep=';')

# 📌 Exibir colunas carregadas para depuração
st.write("📋 **Colunas disponíveis no DataFrame:**", df.columns.tolist())

# 📌 Verificar se a coluna "Produções" existe
if "Produções" not in df.columns:
    st.error("⚠️ A coluna 'Produções' não foi encontrada no arquivo. Verifique o CSV.")
    st.stop()

# 📌 Extrair Congressos/Revisas e Tipos de Produção diretamente da coluna "Produções"
df["Fonte"] = df["Produções"].apply(extrair.extrair_congresso_ou_revista)
df["Tipo de Produção"] = df["Produções"].apply(extrair.classificar_tipo)

# Criar filtros
aluno, orientador, ano = filtros.criar_filtros(df)

# Aplicar filtros
df_filtrado = filtros.aplicar_filtros(df, aluno, orientador, ano)

# 📌 Gerar gráficos diretamente no Streamlit
graficos.plot_top_congressos(df_filtrado)
graficos.plot_tipo_producao(df_filtrado)
