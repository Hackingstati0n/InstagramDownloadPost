# Instagram Image Downloader

[![Assista ao vídeo](https://img.youtube.com/vi/BYJiVNAhJUc/0.jpg)](https://youtu.be/BYJiVNAhJUc)

Este projeto permite baixar imagens de postagens do Instagram automaticamente, utilizando o navegador Brave com Selenium para simular a navegação e a biblioteca Requests para fazer o download das imagens em alta resolução.

## Funcionalidades

- O código lê URLs de postagens do Instagram a partir de um arquivo `urls.txt`.
- Abre as postagens no navegador Brave.
- Coleta a imagem de alta resolução.
- Faz o download automático das imagens para uma pasta chamada `imagens_instagram`.

## Requisitos

Para rodar este projeto, é necessário ter os seguintes requisitos instalados:

- **Python 3.x**: Linguagem de programação utilizada.
- **Selenium**: Para automatizar o navegador.
- **Requests**: Para baixar as imagens.
- **WebDriver do Chrome (ou Brave)**: Necessário para o Selenium controlar o navegador.
- **Brave Browser (ou Chrome)**: Navegador utilizado para acessar o Instagram.

Você pode instalar os pacotes Python necessários usando o seguinte comando:

```bash
pip install selenium requests
```

## Como Configurar

### Passo 1: Instalar o Brave Browser (ou Chrome)
Se você ainda não tem o Brave instalado, faça o download e instale-o. Caso prefira usar o Google Chrome, basta instalar o Chrome e alterar o caminho no código.

### Passo 2: WebDriver
Baixe o WebDriver do Chrome ou Brave e coloque o caminho do WebDriver no seu sistema. O Selenium irá localizar automaticamente o WebDriver para o Chrome, mas é necessário garantir que ele esteja instalado corretamente.

### Passo 3: Configurar o Perfil do Navegador
O código foi projetado para usar o perfil do Brave, garantindo que você esteja logado no Instagram e consiga acessar postagens privadas, caso necessário.

O caminho do perfil do Brave no seu sistema pode ser algo como:

```plaintext
C:\Users\SEU_USUARIO\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default
```

Substitua este caminho no código para o caminho correto do seu perfil do Brave. Se você não quiser usar o perfil do navegador, o código ainda funcionará, mas pode ser necessário fazer login manualmente.

### Passo 4: Criar o Arquivo de URLs
O código lê URLs de um arquivo `urls.txt`, onde cada linha deve conter uma URL de uma postagem do Instagram, como por exemplo:

```plaintext
https://www.instagram.com/p/POST_SHORTCODE_1/
https://www.instagram.com/p/POST_SHORTCODE_2/
...
```

### Passo 5: Rodar o Script
Depois de configurar o perfil e o arquivo de URLs, basta rodar o script Python:

```bash
python baixar_imagens.py
```

O script irá:

- Ler as URLs de postagens do arquivo `urls.txt`.
- Abrir cada URL no navegador Brave.
- Coletar a URL da imagem de alta resolução.
- Baixar a imagem para a pasta `imagens_instagram`.
- Fechar a guia do navegador após o download da imagem.

## Estrutura do Projeto

```plaintext
instagram-image-downloader/
├── baixar_imagens.py       # Código principal para baixar as imagens
├── urls.txt                # Arquivo contendo as URLs das postagens
├── imagens_instagram/      # Pasta onde as imagens serão salvas
└── README.md               # Este arquivo
```

## Como Funciona o Código

- **Configuração do WebDriver e Brave**: O Selenium é configurado para usar o Brave como navegador e carregar o perfil de usuário especificado.
- **Abertura das Postagens**: O script abre as postagens do Instagram nas URLs fornecidas e aguarda o carregamento da página.
- **Coleta da Imagem**: A imagem de alta resolução é extraída através de um XPath, e o link da imagem é capturado.
- **Download da Imagem**: Usando a biblioteca Requests, o script faz o download da imagem e a salva na pasta `imagens_instagram`.
- **Fechamento do Navegador**: Após o download de cada imagem, o navegador é fechado automaticamente.

## Problemas Comuns

- **Erro ao encontrar o chromedriver**: Certifique-se de que o WebDriver do Chrome ou Brave está instalado corretamente e configurado no PATH ou forneça o caminho completo no código.
- **Erro de login**: Se o perfil for privado, o script pode não conseguir acessar as imagens. Neste caso, certifique-se de que você está logado no perfil do Instagram no navegador Brave que está sendo utilizado pelo Selenium.
