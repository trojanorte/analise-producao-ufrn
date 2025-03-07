## 📌 1. Código para Processar Produções Acadêmicas

import pandas as pd
import re

# 📌 Carregar os dados do CSV original
df = pd.read_csv("data/alunos_com_lattes.csv", encoding="utf-8")

# 📌 Função para limpar e extrair informações das produções
def extrair_dados_producao(texto_producao):
    if pd.isna(texto_producao) or texto_producao.strip() == "":
        return [("Sem Produções", "Sem Título", "Sem Evento", "0000", "Sem Tipo")]

    # 🔹 Verificar se o cabeçalho indica que o aluno tem produções
    tem_producao = "Produção bibliográfica" in texto_producao

    # 🔹 Expressão regular para capturar produções acadêmicas (buscando números no início)
    padrao = re.compile(r"^(\d+)\.\s*(.+?)\s*\.\s*(.+?)\s*In:\s*(.+?),\s*(\d{4})", re.MULTILINE)

    producoes = []
    
    for linha in texto_producao.split("\n\n"):  # Separar por quebras de linha duplas
        linha = linha.strip()
        match = padrao.search(linha)
        
        if match:
            numero = match.group(1).strip()
            autores = match.group(2).strip()
            titulo = match.group(3).strip()
            evento = match.group(4).strip()
            ano = match.group(5).strip()
            
            # 🔹 Identificar o tipo de produção
            if "Congresso" in evento or "Encontro" in evento or "Simpósio" in evento:
                tipo_producao = "Trabalho em Congresso"
            elif "Revista" in evento or "Periódico" in evento:
                tipo_producao = "Artigo em Periódico"
            elif "Resumo" in evento:
                tipo_producao = "Resumo em Congresso"
            else:
                tipo_producao = "Outros"
                
            producoes.append((autores, titulo, evento, ano, tipo_producao))
    
    if not producoes and tem_producao:
        producoes.append(("Produção existente, mas não reconhecida", "Sem Título", "Sem Evento", "0000", "Sem Tipo"))
    elif not producoes:
        producoes.append(("Sem Produções", "Sem Título", "Sem Evento", "0000", "Sem Tipo"))

    return producoes

# 📌 Criar um novo DataFrame para armazenar as produções
linhas_expandidas = []

for _, row in df.iterrows():
    aluno = row["Aluno"].strip()
    
    # 🔹 Ignorar registros inválidos
    if aluno.lower() in ["étudiant/leader", "desconhecido", "sem aluno", "none", ""]:
        continue

    matricula = row["Matrícula"]
    ano_ingresso = row["Ano de Ingresso"]
    orientador = row["Orientador"]

    producoes = extrair_dados_producao(row.get("Produções", ""))

    for autores, titulo, evento, ano, tipo_producao in producoes:
        linhas_expandidas.append([matricula, ano_ingresso, aluno, orientador, autores, titulo, evento, ano, tipo_producao])

# 📌 Criando um novo DataFrame apenas para Produções Acadêmicas
df_producoes = pd.DataFrame(linhas_expandidas, columns=["Matrícula", "Ano de Ingresso", "Aluno", "Orientador", "Autores", "Título", "Evento", "Ano", "Tipo de Produção"])

# 📌 Salvando os dados processados
df_producoes.to_csv("data/alunos_producoes_separadas.csv", index=False, encoding="utf-8")

print("✅ Arquivo de Produções gerado: 'alunos_producoes_separadas.csv'")


## 📌 2. Código para Processar Formações e Premiações

# 📌 Criar um novo DataFrame para Formações e Premiações (sem repetição)
df_formacoes_premiacoes = df[["Matrícula", "Aluno", "Ano de Ingresso", "Orientador", "Lattes", "Resumo", "Premiações", "Formações"]].drop_duplicates()

# 📌 Salvando os dados processados
df_formacoes_premiacoes.to_csv("data/alunos_formacoes_premiacoes.csv", index=False, encoding="utf-8")

print("✅ Arquivo de Formações e Premiações gerado: 'alunos_formacoes_premiacoes.csv'")
