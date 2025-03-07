import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Criar a pasta "data" se não existir
if not os.path.exists("data"):
    os.makedirs("data")

# URL do SIGAA (ajuste conforme necessário)
url = 'https://sigaa.ufrn.br/sigaa/public/programa/alunos.jsf?lc=fr_FR&id=105'

# Requisição HTTP para obter o conteúdo da página
response = requests.get(url)
response.encoding = 'ISO-8859-1'  # Define a codificação correta

if response.status_code == 200:
    # Decodificando a resposta corretamente
    html_content = response.content.decode('ISO-8859-1', 'ignore')  
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Encontra a tabela que contém os dados dos alunos
    table = soup.find('tbody')
    
    # Inicializa listas para armazenar os dados
    matriculas = []
    alunos = []
    orientadores = []
    anos_ingresso = []

    # Itera sobre as linhas da tabela
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) < 2:
            continue  # Ignorar linhas sem dados válidos

        matricula = cols[0].text.strip()
        nome_aluno = cols[1].contents[0].strip()  # Nome do aluno está na primeira posição

        # Corrigindo caracteres estranhos (se necessário)
        nome_aluno = nome_aluno.encode('ISO-8859-1').decode('utf-8', 'ignore')

        # Extraindo o orientador (se existir)
        orientador_tag = cols[1].find('a')
        if orientador_tag:
            orientador = orientador_tag.text.strip().replace('(Orientador)', '')
        else:
            orientador = "Sem Orientador"

        # Ano de ingresso com base nos 4 primeiros dígitos da matrícula
        ano_ingresso = matricula[:4] if matricula.isdigit() else "Desconhecido"

        # Adicionando os dados às listas
        matriculas.append(matricula)
        alunos.append(nome_aluno)
        orientadores.append(orientador)
        anos_ingresso.append(ano_ingresso)

    # Criando um DataFrame do Pandas
    df = pd.DataFrame({
        'Matrícula': matriculas,
        'Ano de Ingresso': anos_ingresso,
        'Aluno': alunos,
        'Orientador': orientadores
    })

    # Caminho para salvar dentro da pasta "data"
    csv_path = os.path.join("data", "alunos_por_orientador.csv")
    
    # Salvando os dados no arquivo CSV dentro da pasta "data"
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')  # Salva com UTF-8 para evitar problemas de acentuação

    print(f"Arquivo salvo com sucesso em: {csv_path}")
    print(df.head())  # Exibir os primeiros registros para conferência

else:
    print("Erro ao acessar a página do SIGAA.")
