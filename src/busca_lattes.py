## 1️⃣ Iniciar o navegador e resolver o CAPTCHA

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def iniciar_navegador():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")  # Reduz detecção de bot
    options.add_argument("--headless")  # Executa sem abrir janela
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# URL da plataforma Lattes
url_lattes = "https://buscatextual.cnpq.br/buscatextual/busca.do"

# Inicia o navegador
driver = iniciar_navegador()
driver.get(url_lattes)

# **Marcar a opção "Buscar demais"**
try:
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "buscarDemais")))
    if not checkbox.is_selected():
        checkbox.click()
    print("✅ Opção 'Buscar demais' marcada.")
except Exception as e:
    print(f"⚠️ Erro ao marcar a opção 'Buscar demais': {e}")

# **Pedir para o usuário resolver o CAPTCHA manualmente**
print("⚠️ Resolva o CAPTCHA manualmente e pressione Enter para continuar...")
input("Pressione Enter depois de resolver o CAPTCHA: ")

## 2️⃣ Pesquisar o aluno e acessar o resultado correto

def buscar_aluno(driver, nome):  # ✅ Agora aceita driver como argumento
    print(f"\n🔍 Buscando: {nome}")

    # **Localizar e preencher o campo de busca**
    try:
        campo_busca = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "textoBusca")))
        campo_busca.clear()
        campo_busca.send_keys(nome)

        # **Clicar no botão de busca**
        botao_busca = driver.find_element(By.ID, "botaoBuscaFiltros")
        botao_busca.click()
        time.sleep(3)  # Aguarda a pesquisa ser carregada

    except Exception as e:
        print(f"⚠️ Erro ao buscar {nome}: {e}")
        return None

    # **Selecionar o primeiro resultado correto**
    try:
        resultado = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, 'javascript:abreDetalhe')]"))
        )

        if resultado:
            resultado[0].click()  # Clica no primeiro nome encontrado
            time.sleep(3)  # Aguarda carregar
        else:
            print(f"⚠️ Nenhum resultado encontrado para {nome}")
            return None

    except Exception as e:
        print(f"⚠️ Erro ao selecionar o resultado de {nome}: {e}")
        return None

    return True

## 3️⃣ Abrir o currículo e extrair informações

def extrair_dados(driver):
    """
    Extrai informações do currículo Lattes apenas após clicar no botão 'Abrir Currículo' e carregar a nova aba.
    """

    # **Tentar clicar no botão "Abrir Currículo"**
    try:
        abrir_cv = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "idbtnabrircurriculo"))
        )
        abrir_cv.click()
        time.sleep(2)  # Pequeno delay para abertura da aba
    except Exception as e:
        print(f"⚠️ Erro ao clicar em 'Abrir Currículo': {e}")
        return None

    # **Verificar se a nova aba foi realmente aberta**
    janelas_antes = len(driver.window_handles)
    time.sleep(2)  # Pequeno tempo para a aba abrir

    if len(driver.window_handles) == janelas_antes:
        print("⚠️ A nova aba do currículo não abriu. Tentando novamente...")
        try:
            abrir_cv.click()
            time.sleep(3)  # Aguarda novamente
        except Exception as e:
            print(f"⚠️ Erro ao tentar reabrir o currículo: {e}")
            return None

    # **Trocar para a nova aba (onde estão os dados corretos)**
    driver.switch_to.window(driver.window_handles[-1])

    # **Aguardar a página carregar completamente**
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "nome"))
        )
    except:
        print("⚠️ Erro: O currículo não carregou corretamente.")
        return None

    # **Obter o link do currículo primeiro**
    link_lattes = driver.current_url

    # **Capturar informações após abrir o currículo**
    dados_curriculo = {"Lattes": link_lattes}

    try:
        dados_curriculo["Nome no Lattes"] = driver.find_element(By.CSS_SELECTOR, "h2.nome").text
    except:
        dados_curriculo["Nome no Lattes"] = "Nome não encontrado"

    try:
        dados_curriculo["Resumo"] = driver.find_element(By.CSS_SELECTOR, "p.resumo").text
    except:
        dados_curriculo["Resumo"] = "Resumo não encontrado"

    # **Capturar seções específicas**
    def extrair_secao(nome_secao):
        try:
            elemento = driver.find_element(By.XPATH, f"//a[@name='{nome_secao}']/following-sibling::div")
            return elemento.text.strip()
        except:
            return "Não encontrado"

    # **Capturar Produções, Prêmios e Formação acadêmica**
    dados_curriculo["Produções"] = extrair_secao("ProducoesCientificas")
    dados_curriculo["Premiações"] = extrair_secao("PremiosTitulos")
    dados_curriculo["Formações"] = extrair_secao("FormacaoAcademicaTitulacao")

    return dados_curriculo

## 4️⃣ Executar o processo para vários alunos

# **Executar o processo para vários alunos**
df_alunos = pd.read_csv("data/alunos_por_orientador.csv")

# **Criar lista para armazenar os resultados**
resultados = []

# **Iterar sobre todos os alunos**
for nome in df_alunos["Aluno"]:
    print(f"\n🔍 Processando: {nome}")

    # **Fechar e reiniciar o navegador para evitar problemas de memória**
    driver.quit()
    driver = iniciar_navegador()
    driver.get(url_lattes)

    # **Marcar a opção "Buscar demais" novamente**
    try:
        checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "buscarDemais")))
        if not checkbox.is_selected():
            checkbox.click()
        print("✅ Opção 'Buscar demais' marcada novamente.")
    except Exception as e:
        print(f"⚠️ Erro ao marcar a opção 'Buscar demais': {e}")

    # **Buscar o aluno e extrair os dados**
    if buscar_aluno(driver, nome):
        dados = extrair_dados(driver)  # ✅ Correção: Passando o driver como argumento
        if dados:
            resultados.append({"Aluno": nome, **dados})
        else:
            resultados.append({"Aluno": nome, "Lattes": "Não encontrado", "Nome no Lattes": "", "Resumo": "", "Produções": "", "Premiações": "", "Formações": ""})

    # **Salvar os resultados progressivamente para evitar perda de dados**
    df_parcial = pd.DataFrame(resultados)
    df_parcial.to_csv("data/alunos_parciais.csv", index=False)

# **Criar DataFrame final com os resultados**
df_resultados = pd.DataFrame(resultados)

# **Garantir que 'Aluno' esteja presente em ambos os DataFrames**
if "Aluno" in df_alunos.columns and "Aluno" in df_resultados.columns:
    df_final = df_alunos.merge(df_resultados, on="Aluno", how="left")
else:
    print("⚠️ Erro: Coluna 'Aluno' não encontrada em um dos DataFrames.")
    df_final = df_alunos

# **Salvar os links e informações no CSV final**
df_final.to_csv("data/alunos_com_lattes.csv", index=False)

print("✅ Coleta concluída! Dados salvos em 'data/alunos_com_lattes.csv'")
