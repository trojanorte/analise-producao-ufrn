# 📜 Licença e Direitos Autorais

Este projeto é licenciado sob a **Creative Commons BY-NC-ND 4.0**. Isso significa que:
- ✅ Você pode compartilhar e utilizar os arquivos.
- ❌ **Não pode modificar** ou criar obras derivadas.
- ❌ **Não pode utilizar para fins comerciais.**

---

# 📊 Projeto: Análise da Produção Acadêmica dos Alunos da Pós-Graduação da UFRN

## 🎯 Objetivo
Este projeto visa **extrair, organizar e analisar** os dados de produção acadêmica dos alunos do Programa de Pós-Graduação em Engenharia de Produção da UFRN. Os dados são obtidos do **SIGAA** e **Plataforma Lattes**, permitindo avaliar os indicadores de produção científica, impacto acadêmico e reconhecimento institucional.

## 🔍 Etapas do Projeto

### **1️⃣ Extração de Dados do SIGAA**
- Obter a lista de alunos e orientadores.
- Extrair os **4 primeiros dígitos da matrícula** para identificar o ano de ingresso.
- Armazenar esses dados em um **DataFrame Pandas**.

### **2️⃣ Coleta de Dados na Plataforma Lattes**
- Automatizar a busca dos currículos.
- Capturar dados sobre:
  - **Publicações científicas** (artigos, congressos, eventos).
  - **Índice h** e citações.
  - **Tecnologias, patentes e premiações.**

### **3️⃣ Análise Comparativa: Produção Durante e Após o Mestrado**
- Separar a produção acadêmica em **durante** e **após o mestrado**.
- Analisar o impacto e continuidade da pesquisa.

### **4️⃣ Geração de Relatórios e Indicadores**
- Quantidade de publicações por **aluno e orientador**.
- Fração de **egressos com produção relevante**.
- Geração de **relatórios de impacto acadêmico**, como:
  - **Índice h2 (Scopus)** do corpo docente.
  - **Internacionalização e colaborações acadêmicas**.
  - **Premiações e reconhecimentos**.

---

## ⚙️ Tecnologias Utilizadas
✅ **Python** para extração e análise de dados.
✅ **Requests & BeautifulSoup** para web scraping.
✅ **Pandas** para manipulação e organização dos dados.
✅ **Matplotlib & Seaborn** para visualizações gráficas.
✅ **Streamlit & Plotly** para dashboard interativo.

---

## 📂 Estrutura do Projeto

```
/analise_producao_ufrn
│── data/                      # Arquivos CSV extraídos
│── src/                       # Código-fonte
│   ├── scraping_sigaa.py       # Extrai dados do SIGAA
│   ├── busca_lattes.py         # Obtém dados da Plataforma Lattes
│   ├── processar_dados.py      # Processa e estrutura os dados
│   ├── dashboard.py            # Interface gráfica (Streamlit)
│── README.md                  # Documentação do projeto
│── requirements.txt            # Dependências para instalação
```

---

## 🚀 Como Usar

### 📌 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/analise_producao_ufrn.git
cd analise_producao_ufrn
```

### 📌 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 📌 3. Execute a extração de dados do SIGAA:
```bash
python src/scraping_sigaa.py
```

### 📌 4. Busque os currículos Lattes:
```bash
python src/busca_lattes.py
```

### 📌 5. Gere os relatórios analíticos:
```bash
python src/processar_dados.py
```

### 📌 6. Execute o Dashboard:
```bash
streamlit run src/dashboard.py
```

---

## 📊 Resultados Esperados
✅ **Relatórios detalhados** sobre produção acadêmica.
✅ **Métricas de impacto científico** (artigos, eventos, índice h2).
✅ **Internacionalização e colaborações acadêmicas.**
✅ **Distribuição da produção durante e após o mestrado.**
✅ **Premiações e reconhecimentos acadêmicos.**

---

## 🤝 Contribuição
Se quiser contribuir com o projeto, faça um **fork**, crie **pull requests** ou sugira melhorias via **Issues**.

---

### 📢 Observação Importante
Este projeto respeita os **termos de uso do SIGAA e Plataforma Lattes**. Nenhum dado é compartilhado ou utilizado para fins comerciais.

