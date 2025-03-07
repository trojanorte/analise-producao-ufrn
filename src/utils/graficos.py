import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def plot_top_congressos(df):
    """ Gera gráfico dos 10 congressos mais publicados """
    if "Congresso/Revista" not in df.columns:
        st.error("⚠️ A coluna 'Congresso/Revista' não foi encontrada no arquivo.")
        return

    st.subheader("📰 Top 10 Congressos e Revistas Mais Publicados")

    top_congressos = df["Congresso/Revista"].value_counts().head(10).reset_index()
    top_congressos.columns = ["Congresso/Revista", "Quantidade"]

    st.dataframe(top_congressos)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="Quantidade", y="Congresso/Revista", data=top_congressos, palette="coolwarm", ax=ax)
    ax.set_title("Top 10 Congressos e Revistas Mais Publicados", fontsize=14)
    ax.set_xlabel("Quantidade")
    ax.set_ylabel("Congresso/Revista")
    
    st.pyplot(fig)

def plot_tipo_producao(df):
    """ Gera gráfico da distribuição dos tipos de produção """
    if "Tipo de Produção" not in df.columns:
        st.error("⚠️ A coluna 'Tipo de Produção' não foi encontrada no arquivo.")
        return

    st.subheader("📚 Distribuição dos Tipos de Produção")

    tipos_producao = df["Tipo de Produção"].value_counts().reset_index()
    tipos_producao.columns = ["Tipo de Produção", "Quantidade"]

    st.dataframe(tipos_producao)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="Quantidade", y="Tipo de Produção", data=tipos_producao, palette="viridis", ax=ax)
    ax.set_title("Distribuição dos Tipos de Produção", fontsize=14)
    ax.set_xlabel("Quantidade")
    ax.set_ylabel("Tipo de Produção")

    st.pyplot(fig)
