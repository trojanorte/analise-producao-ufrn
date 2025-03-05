import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Define uma fonte compatível com emojis
plt.rcParams['font.family'] = 'Segoe UI Emoji'  # Para Windows

# Carregar os dados
file_path = "c:/Users/allys/OneDrive/Documentos/GitHub/analise producao ufrn/data/alunos_parciais.csv"  # Atualize conforme necessário
df = pd.read_csv(file_path)

# Função para contar o número de títulos diferentes em qualquer coluna
def contar_titulos(texto):
    if pd.isna(texto) or texto.strip() == "Não encontrado":
        return 0
    return len(set(texto.strip().split("\n")))

# Aplicar a função para contar títulos únicos em todas as colunas relevantes
df["Quantidade de Produções"] = df["Produções"].apply(contar_titulos)
df["Quantidade de Premiações"] = df["Premiações"].apply(contar_titulos)
df["Quantidade de Formações"] = df["Formações"].apply(contar_titulos)
df["Quantidade de Resumo"] = df["Resumo"].apply(contar_titulos)

# Estatísticas gerais das contagens
print("\n📊 Estatísticas gerais:")
print(df[["Quantidade de Produções", "Quantidade de Premiações", "Quantidade de Formações", "Quantidade de Resumo"]].describe())

# Alunos com mais produções acadêmicas
top_produtores = df.sort_values(by="Quantidade de Produções", ascending=False).head(10)
print("\n🏆 Top 10 alunos com mais produções acadêmicas:")
print(top_produtores[["Aluno", "Quantidade de Produções"]])

# Criar gráficos para visualização

# Histograma de produções acadêmicas
plt.figure(figsize=(10, 5))
df["Quantidade de Produções"].hist(bins=20, edgecolor="black")
plt.title("📊 Distribuição de Produções Acadêmicas por Aluno")
plt.xlabel("Número de Produções Únicas")
plt.ylabel("Quantidade de Alunos")
plt.grid(axis="y", alpha=0.75)
plt.show()

# Histograma de premiações
plt.figure(figsize=(10, 5))
df["Quantidade de Premiações"].hist(bins=10, edgecolor="black")
plt.title("🏅 Distribuição de Premiações por Aluno")
plt.xlabel("Número de Premiações Únicas")
plt.ylabel("Quantidade de Alunos")
plt.grid(axis="y", alpha=0.75)
plt.show()

# Histograma de produções acadêmicas
plt.figure(figsize=(10, 5))
df["Quantidade de Produções"].hist(bins=20, edgecolor="black")
plt.title("Distribuição de Produções Acadêmicas por Aluno")  # 🔹 Removi o emoji 📊
plt.xlabel("Número de Produções Únicas")
plt.ylabel("Quantidade de Alunos")
plt.grid(axis="y", alpha=0.75)
plt.show()

# Histograma de resumos
plt.figure(figsize=(10, 5))
df["Quantidade de Resumo"].hist(bins=10, edgecolor="black")
plt.title("📄 Distribuição de Resumos por Aluno")
plt.xlabel("Número de Resumos Únicos")
plt.ylabel("Quantidade de Alunos")
plt.grid(axis="y", alpha=0.75)
plt.show()
