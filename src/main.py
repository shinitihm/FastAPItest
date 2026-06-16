from utils.api import generate
from pathlib import Path
import yaml

def main():
    caminho_config = Path(__file__).parent.parent / 'config' / 'config.yaml'
    with open(caminho_config, 'r', encoding='utf-8') as arquivo:
        config = yaml.safe_load(arquivo)

    ## carregando variaveis fixas
    MODEL = config["Agent_Model"]['gemini_flash']

    prompt = input("digite o prompt: ")

    resposta = generate(prompt=prompt, model=MODEL)
    print("\nResposta do modelo:")
    print(resposta)

if __name__ == '__main__':
    main()