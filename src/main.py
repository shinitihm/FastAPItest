import requests
from pathlib import Path
import yaml
from utils.api import ENDPOINT
from utils.api import x_api_key

def main():
    caminho_config = Path(__file__).parent.parent / 'config' / 'config.yaml'
    with open(caminho_config, 'r', encoding='utf-8') as arquivo:
        config = yaml.safe_load(arquivo)

    ## carregando variaveis fixas
    MODEL = config["Agent_Model"]['gemini_flash']
    host = config["EndPoint"]["host"]
    port = config["EndPoint"]["port"]
    url = f"http://{host}:{port}/{ENDPOINT}"

    
    prompt = input("Insira sua pergunta: ")

    parametros = {
        "prompt": prompt,
        "model": MODEL 
    }
    cabecalhos = {
        "x-api-key": x_api_key
    }

    print("\nEnviando requisição para a API...")
    
    resposta = requests.post(url, params=parametros,headers=cabecalhos)

    if resposta.status_code == 200:
        print("\nResposta do modelo:")
        print(resposta.json()["response"])
    else:
        print("\nOpa, deu erro na API!")
        print(f"Status: {resposta.status_code}")
        print(f"Detalhes: {resposta.text}")

if __name__ == '__main__':
    main()