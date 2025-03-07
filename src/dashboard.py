import streamlit as st
import pandas as pd
import plotly.express as px
import utils.filtros as filtros
import utils.graficos as graficos

# 📌 Configuração da página
st.set_page_config(page_title="Dashboard de Produções Acadêmicas", layout="wide")

# 📌 Caminho do arquivo processado
file_path = "c:/Users/allys/OneDrive/Documentos/GitHub/analise producao ufrn/data/alunos_producoes_separadas.csv"

# 📌 Carregar os dados processados
st.sidebar.header("⚙️ Configurações")
try:
    df = pd.read_csv(file_path, encoding="utf-8")
    st.sidebar.success("✅ Dados carregados com sucesso!")
except FileNotFoundError:
    st.sidebar.error("❌ Erro: O arquivo não foi encontrado. Execute 'processar_producoes.py'.")
    st.stop()
except pd.errors.ParserError as e:
    st.sidebar.error(f"❌ Erro ao processar o CSV: {e}")
    st.stop()

# 📌 Criar interface principal
st.title("📊 Dashboard de Produções Acadêmicas")
st.markdown("### 📌 Análise das Produções de Alunos e Orientadores")

# 📌 Criar filtros no sidebar
with st.sidebar:
    aluno, orientador, tipo_producao, ano_ingresso, evento = filtros.criar_filtros(df)

# 📌 Aplicar filtros
df_filtrado = filtros.aplicar_filtros(df, aluno, orientador, tipo_producao, ano_ingresso, evento)

# 📌 Layout: Criar métricas principais
st.markdown("### 📈 Resumo dos Dados")
col1, col2, col3 = st.columns(3)
col1.metric("📚 Total de Produções", len(df_filtrado))
col2.metric("👨‍🎓 Alunos Registrados", df_filtrado["Aluno"].nunique())
col3.metric("👨‍🏫 Orientadores Registrados", df_filtrado["Orientador"].nunique())

# 📌 Exibir pré-visualização dos dados filtrados com tabela formatada
st.markdown("### 🔍 Dados Filtrados")
st.dataframe(df_filtrado, use_container_width=True)

# 📌 Verificar se há dados após o filtro
if df_filtrado.empty:
    st.warning("⚠️ Nenhum dado encontrado com os filtros selecionados.")
else:
    # 📌 Gráficos organizados em colunas para melhor visualização
    st.markdown("## 📊 Visualização dos Dados")
    col1, col2 = st.columns(2)

    with col1:
        graficos.plot_top_congressos(df_filtrado)
        graficos.plot_producao_por_ano(df_filtrado)

    with col2:
        graficos.plot_tipo_producao(df_filtrado)
        graficos.plot_distribuicao_eventos(df_filtrado)

# 📌 **Seção de Insights Dinâmicos**
st.markdown("## 🔎 Insights sobre Produções Acadêmicas")

if not df_filtrado.empty:
    top_anos = df_filtrado["Ano"].value_counts().nlargest(3).index.tolist()
    top_evento = df_filtrado["Evento"].value_counts().idxmax() if not df_filtrado["Evento"].isna().all() else "Nenhum evento encontrado"
    top_tipo = df_filtrado["Tipo de Produção"].value_counts().idxmax() if not df_filtrado["Tipo de Produção"].isna().all() else "Nenhum tipo encontrado"

    st.write(f"""
    - 🔹 **A maioria das produções ocorreu nos anos:** {', '.join(map(str, top_anos))}
    - 🔹 **O evento mais frequente foi:** {top_evento}
    - 🔹 **O tipo de produção mais comum foi:** {top_tipo}
    """)
else:
    st.info("📌 Nenhum dado disponível para gerar insights.")

# 📌 Mensagem de dica no sidebar
st.sidebar.info("📌 Dica: Você pode usar os filtros para visualizar dados específicos.")
