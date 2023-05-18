import json
from googletrans import Translator

# Pede ao usuário para digitar o texto a ser traduzido
texto = input("Digite o texto a ser traduzido: ")

# Define os idiomas de destino
idiomas_destino = ['pt', 'en'] 

# Cria uma instância do objeto Translator
translator = Translator()

# Itera pelos idiomas e traduz o texto para cada um deles
for idioma in idiomas_destino:
    # Define o caminho do arquivo JSON de destino
    arquivo_destino = f'../vfclub/vfclub/src/translate/{idioma}.json'
    
    try:
        # Tenta abrir o arquivo JSON
        with open(arquivo_destino, 'r') as f:
            # Carrega o conteúdo do arquivo em um objeto Python
            dados = json.load(f)
    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo objeto com a nova tradução
        dados = {"translation": {}}
    
    # Verifica se a tradução para o idioma já existe no objeto
    if texto in dados["translation"].values():
        print(f"A tradução para o idioma {idioma} já existe.")
        continue
    
    # Traduz o texto para o idioma de destino
    traducao = translator.translate(texto, dest=idioma)
    
    # Adiciona a nova tradução ao objeto
    dados["translation"][texto] = traducao.text
    
    # Salva o objeto como um arquivo JSON
    with open(arquivo_destino, 'w') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        
    print(f"A tradução para o idioma {idioma} foi salva em {arquivo_destino}.")
