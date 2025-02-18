import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import time

# Nome da pasta onde as imagens serão salvas
PASTA_IMAGENS = "imagens_instagram"
os.makedirs(PASTA_IMAGENS, exist_ok=True)

# Caminho para o perfil do Brave
PROFILE_PATH = r"C:\Users\SEU USUARIO\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default"  # Substitua pelo caminho do seu perfil

# Caminho do Brave
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # Pasta padrao onde o Brave esta Instalado

def baixar_imagem(instagram_url):
    try:
        # Configuração do Brave para usar o perfil
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"user-data-dir={PROFILE_PATH}")  # Carregar o perfil do usuário
        chrome_options.binary_location = BRAVE_PATH  # Usar o Brave como navegador

        # Inicializar o WebDriver
        driver = webdriver.Chrome(options=chrome_options)  # Selenium localiza o ChromeDriver automaticamente

        # Acessar a URL da postagem
        driver.get(instagram_url)

        # Esperar a página carregar
        time.sleep(5)

        # Tentar pegar a URL da imagem de alta resolução
        try:
            # Buscar pelo elemento de imagem de alta resolução
            img_element = driver.find_element(By.XPATH, '//article//img')
            image_url = img_element.get_attribute("src")
        except Exception as e:
            print(f"Erro ao pegar a imagem: {e}")
            image_url = None

        # Fazer download da imagem
        if image_url:
            nome_arquivo = os.path.join(PASTA_IMAGENS, image_url.split("/")[-1].split("?")[0])
            img_response = requests.get(image_url, stream=True)
            img_response.raise_for_status()  # Garantir que a requisição foi bem-sucedida
            with open(nome_arquivo, "wb") as f:
                for chunk in img_response.iter_content(1024):
                    f.write(chunk)

            print(f"Imagem salva: {nome_arquivo}")
        else:
            print(f"Imagem não encontrada para a URL: {instagram_url}")

        # Fechar a guia
        driver.quit()

    except Exception as e:
        print(f"Erro ao processar {instagram_url}: {e}")

# Ler URLs de um arquivo urls.txt
arquivo_urls = "urls.txt"

try:
    with open(arquivo_urls, "r") as f:
        urls = f.read().splitlines()

    print(f"{len(urls)} URLs encontradas. Iniciando download...\n")

    for url in urls:
        baixar_imagem(url)

    print("\nProcesso concluído.")
except FileNotFoundError:
    print(f"Arquivo {arquivo_urls} não encontrado. Crie um arquivo com as URLs das postagens.")
