# Projeto: Análise da Produção Acadêmica dos Alunos da Pós-Graduação da UFRN

## 📌 Objetivo
Este projeto visa **extrair, organizar e analisar** os dados dos alunos do programa de pós-graduação em Engenharia de Produção da UFRN,** separando-os por orientador** e cruzando essas informações com suas produções acadêmicas na Plataforma Lattes. O resultado final permitirá avaliar os **indicadores de produção científica, impacto acadêmico e reconhecimento**, conforme os critérios definidos no checklist do programa.

## 🔍 Etapas do Projeto
### **1️⃣ Extração de Dados do SIGAA**
- Obter a lista de alunos e seus respectivos orientadores do site do SIGAA.
- Extrair os **4 primeiros dígitos da matrícula** para identificar o ano de ingresso.
- Armazenar essas informações em um DataFrame (Pandas) para manipulação posterior.

### **2️⃣ Busca de Currículos na Plataforma Lattes**
- Automatizar a busca dos alunos na Plataforma Lattes.
- Coletar dados sobre:
  - Publicações científicas (artigos, congressos, eventos).
  - Índice h e citações.
  - Tecnologias e patentes cadastradas.
  - **Premiações e reconhecimentos acadêmicos.**

### **3️⃣ Análise Comparativa: Produção Dentro e Fora do Mestrado**
- Utilizar o **ano de ingresso** para separar a produção acadêmica em:
  - **Produção durante o mestrado** (publicações, eventos, patentes registradas no período).
  - **Produção após a conclusão** (continuidade na produção científica, novos projetos e impacto acadêmico).

### **4️⃣ Geração de Relatórios e Análise dos Indicadores**
- Contabilizar a **quantidade de publicações por aluno e orientador**.
- Avaliar **a fração de egressos com produção relevante**.
- Gerar um **relatório final com métricas**, como:
  - **Índice h2 (Scopus) do corpo docente.**
  - **Impacto econômico e social do programa.**
  - **Internacionalização e colaboração acadêmica.**
  - **Premiações e reconhecimentos de discentes e docentes.**
  
## ⚙️ Tecnologias Utilizadas
- **Python** para extração e análise de dados.
- **Requests & BeautifulSoup** para raspagem de dados do SIGAA.
- **Pandas** para manipulação e análise dos dados.
- **Selenium (opcional)** para buscas automatizadas no Lattes.
- **Matplotlib/Seaborn** para visualização dos resultados.

## 📂 Estrutura do Projeto
```
/analise_producao_ufrn
│── data/                      # Pasta com os arquivos CSV extraídos
│── src/                       # Código-fonte do projeto
│   ├── scraping_sigaa.py       # Script para extrair dados do SIGAA
│   ├── busca_lattes.py         # Script para buscar produção no Lattes
│   ├── analise_indicadores.py  # Código para gerar relatórios
│── notebooks/                 # Jupyter Notebooks para exploração dos dados
│── README.md                  # Documento de explicação do projeto
│── requirements.txt            # Lista de dependências para instalação
```

## 🚀 Como Usar
1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/analise_producao_ufrn.git
cd analise_producao_ufrn
```
2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```
3. **Execute a raspagem de dados do SIGAA:**
```bash
python src/scraping_sigaa.py
```
4. **Busque os currículos Lattes (manual/automatizado):**
```bash
python src/busca_lattes.py
```
5. **Gere os relatórios analíticos:**
```bash
python src/analise_indicadores.py
```

## 📊 Resultados Esperados
Os resultados incluirão:
✅ **Relatórios sobre produção acadêmica** por aluno e orientador.
✅ **Métricas do impacto científico** (artigos, eventos, índice h2).
✅ **Análise da internacionalização e visibilidade do programa.**
✅ **Distribuição da produção dentro e após o mestrado.**
✅ **Premiações e reconhecimentos de discentes e docentes.**

## 🤝 Contribuição
Se você quiser contribuir com o projeto, sinta-se à vontade para fazer um **fork**, criar **pull requests** ou sugerir melhorias. 

---
### 📢 Observação Importante
Este projeto respeita os **termos de uso das plataformas SIGAA e Lattes