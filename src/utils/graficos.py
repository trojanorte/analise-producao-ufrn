import streamlit as st
import plotly.express as px
import pandas as pd

def plot_top_congressos(df):
    """ Gera gráfico dos 10 congressos/revistas mais publicados """
    if "Evento" not in df.columns:
        st.error("⚠️ A coluna 'Evento' não foi encontrada no arquivo.")
        return

    st.subheader("📰 Top 10 Congressos e Revistas Mais Publicados")

    top_congressos = df["Evento"].value_counts().head(10).reset_index()
    top_congressos.columns = ["Evento", "Quantidade"]

    st.dataframe(top_congressos)

    fig = px.bar(
        top_congressos,
        x="Quantidade",
        y="Evento",
        orientation="h",
        color="Quantidade",
        color_continuous_scale="viridis",
        title="Top 10 Congressos e Revistas Mais Publicados"
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_tipo_producao(df):
    """ Gera gráfico da distribuição dos tipos de produção """
    if "Tipo de Produção" not in df.columns:
        st.error("⚠️ A coluna 'Tipo de Produção' não foi encontrada no arquivo.")
        return

    st.subheader("📚 Distribuição dos Tipos de Produção")

    tipos_producao = df["Tipo de Produção"].value_counts().reset_index()
    tipos_producao.columns = ["Tipo de Produção", "Quantidade"]

    st.dataframe(tipos_producao)

    fig = px.bar(
        tipos_producao,
        x="Quantidade",
        y="Tipo de Produção",
        orientation="h",
        color="Quantidade",
        color_continuous_scale="magma",
        title="Distribuição dos Tipos de Produção"
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_producao_por_ano(df):
    """ Gera gráfico interativo da quantidade de produções por ano """
    if "Ano" not in df.columns:
        st.warning("⚠️ A coluna 'Ano' não está disponível para análise.")
        return

    # 📌 Corrigir anos inválidos (anos muito antigos ou não numéricos)
    df["Ano"] = pd.to_numeric(df["Ano"], errors="coerce")
    df = df.dropna(subset=["Ano"])
    df = df[(df["Ano"] >= 1950) & (df["Ano"] <= 2025)]  # Mantendo intervalos coerentes

    contagem = df["Ano"].value_counts().reset_index()
    contagem.columns = ["Ano", "Quantidade"]
    contagem = contagem.sort_values("Ano")

    st.subheader("📆 Produções Acadêmicas por Ano")

    st.dataframe(contagem)

    fig = px.bar(
        contagem,
        x="Ano",
        y="Quantidade",
        color="Quantidade",
        color_continuous_scale="blues",
        title="Produções Acadêmicas por Ano"
    )
    fig.update_layout(xaxis=dict(tickmode="linear", dtick=1))  # 📌 Ajustar para cada ano ser visível no eixo X

    st.plotly_chart(fig, use_container_width=True)

    # 📌 **Gerar Insights Dinâmicos**
    st.subheader("🔍 Insights sobre Produções Acadêmicas")

    if not contagem.empty:
        ano_mais_publicado = contagem.loc[contagem["Quantidade"].idxmax(), "Ano"]
        total_publicacoes = contagem["Quantidade"].sum()
        media_publicacoes = round(contagem["Quantidade"].mean(), 2)

        st.write(f"📌 **Ano com mais publicações:** {ano_mais_publicado}")
        st.write(f"📊 **Total de produções cadastradas:** {total_publicacoes}")
        st.write(f"📈 **Média de publicações por ano:** {media_publicacoes}")

    else:
        st.write("⚠️ Nenhuma produção válida encontrada.")


def plot_distribuicao_eventos(df):
    """ Gera gráfico da distribuição dos eventos mais publicados """
    if "Evento" not in df.columns:
        st.warning("⚠️ A coluna 'Evento' não está disponível para análise.")
        return

    contagem = df["Evento"].value_counts().reset_index()
    contagem.columns = ["Evento", "Quantidade"]

    st.subheader("🎭 Distribuição de Publicações por Evento")

    st.dataframe(contagem)

    fig = px.pie(
        contagem.head(10),  # Mostrar apenas os 10 eventos mais frequentes
        names="Evento",
        values="Quantidade",
        title="Distribuição de Publicações por Evento",
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(fig, use_container_width=True)
