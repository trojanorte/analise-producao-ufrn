import streamlit as st
import pandas as pd
import utils.filtros as filtros
import utils.graficos as graficos
import utils.extrair_informacoes as extrair

# 📌 Caminho do arquivo
file_path = "c:/Users/allys/OneDrive/Documentos/GitHub/analise producao ufrn/data/alunos_com_lattes.csv"

# 📌 Tentar carregar os dados com detecção automática de separador
try:
    df = pd.read_csv(file_path, sep=None, engine="python", on_bad_lines="skip")
    st.success("✅ Dados carregados com sucesso!")
except FileNotFoundError:
    st.error("❌ Erro: O arquivo de dados não foi encontrado. Verifique o caminho.")
    st.stop()
except pd.errors.ParserError as e:
    st.error(f"❌ Erro ao processar o CSV: {e}")
    st.stop()

# 📌 Exibir as primeiras linhas para diagnóstico
st.write("🔍 **Pré-visualização dos dados:**", df.head())

# 📌 Verificar se a coluna "Produções" está presente
if "Produções" not in df.columns:
    st.error("⚠️ A coluna 'Produções' não foi encontrada no arquivo.")
    st.stop()

# 📌 Extrair Congressos/Revisas e Tipos de Produção diretamente da coluna "Produções"
df["Fonte"] = df["Produções"].apply(extrair.extrair_congresso_ou_revista)
df["Tipo de Produção"] = df["Produções"].apply(extrair.classificar_tipo)

# Criar interface Streamlit
st.title("📊 Análise de Produções Acadêmicas")

# Criar filtros
aluno, orientador, ano = filtros.criar_filtros(df)

# Aplicar filtros
df_filtrado = filtros.aplicar_filtros(df, aluno, orientador, ano)

# 📌 Verificar se há dados após o filtro
if df_filtrado.empty:
    st.warning("⚠️ Nenhum dado encontrado com os filtros selecionados.")
else:
    # 📌 Gerar gráficos corrigidos
    graficos.plot_top_congressos(df_filtrado)
    graficos.plot_tipo_producao(df_filtrado)
