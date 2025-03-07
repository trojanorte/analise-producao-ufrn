import re
import pandas as pd

def extrair_congresso_ou_revista(texto):
    """Extrai corretamente o nome da revista ou congresso a partir do texto da produção."""
    if isinstance(texto, str):
        # 📌 Identifica congressos usando "In: ...,"
        match_congresso = re.search(r'In:\s*([^,]+),', texto)
        if match_congresso:
            return match_congresso.group(1).strip()  # Retorna o nome do congresso

        # 📌 Identifica revistas formatadas em ABNT
        match_revista = re.search(r'\.\s*([\w\s&-]+),\s*v\.\s*\d+', texto)
        if match_revista:
            return match_revista.group(1).strip()  # Retorna o nome da revista

    return "Desconhecido"

def classificar_tipo(texto):
    """Classifica o tipo da produção acadêmica."""
    if isinstance(texto, str):
        texto = texto.lower()  # Normaliza para evitar problemas de formatação

        if "resumo expandido" in texto or "resumos expandidos" in texto:
            return "Resumo Expandido"
        elif "artigo" in texto or "artigos completos publicados em periódicos" in texto:
            return "Artigo"
        elif "trabalho completo" in texto or "trabalhos completos publicados em anais de congressos" in texto:
            return "Trabalho Completo"
        elif "anais" in texto:
            return "Anais de Congresso"
    return "Outro"

def limpar_dados(df):
    """Filtra corretamente as produções acadêmicas da coluna 'Produções'."""

    # 📌 Função para separar corretamente as produções dentro da coluna "Produções"
    def extrair_producoes(texto):
        if isinstance(texto, str):
            # Remove metadados irrelevantes que não são produções reais
            if any(termo in texto.lower() for termo in ["número de citações", "primeiro autor", "impacto jcr",
                                                        "ordem de importância", "apresentação de trabalho"]):
                return []

            # Divide os trabalhos corretamente pelos números da lista (1., 2., 3., etc.)
            producoes = re.split(r"\n\d+\.\s+", texto)
            return [p.strip() for p in producoes if p.strip()]  # Remove elementos vazios
        return []

    # Aplica a extração de produções
    df["Produções Separadas"] = df["Produções"].apply(extrair_producoes)

    # Remove valores nulos e reorganiza os dados corretamente
    df = df.explode("Produções Separadas").dropna(subset=["Produções Separadas"]).reset_index(drop=True)

    # 📌 Identificar Congressos e Revistas diretamente na própria coluna "Produções Separadas"
    df["Fonte"] = df["Produções Separadas"].apply(extrair_congresso_ou_revista)

    # 📌 Classificar o Tipo de Produção
    df["Tipo de Produção"] = df["Produções Separadas"].apply(classificar_tipo)

    return df
