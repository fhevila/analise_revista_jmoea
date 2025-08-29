import requests
import pandas as pd
import time
import numpy as np
from concurrent.futures import ThreadPoolExecutor

# Carregar dados do CSV
df = pd.read_csv("C:\\Users\\fhevi\\Desktop\\artigo_jmoe-main\\artigos_com_universidade.csv")
df.columns = df.columns.str.strip()  # Limpar espaços extras nas colunas

# Inicializar a lista de citações com NaN para todas as linhas
citations_list = [np.nan] * len(df)

# Função para buscar citações para um artigo
def fetch_citations(i, title):
    print(f"Processando artigo {i+1}: {title}")
    try:
        # Busca no CrossRef usando o título
        url = f"https://api.crossref.org/works?query.title={title}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if len(data["message"]["items"]) > 0:
                article = data["message"]["items"][0]  # Pega o primeiro artigo encontrado
                citations = article.get("is-referenced-by-count", "Não disponível")  # Número de citações
                citations_list[i] = citations
            else:
                citations_list[i] = "Não encontrado"
        else:
            citations_list[i] = "Erro na requisição"
    except Exception as e:
        print(f"Erro ao buscar citações para '{title}': {e}")
        citations_list[i] = "Erro"

# Função para processar os artigos em paralelo
def process_in_parallel():
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Processar os artigos em paralelo (10 threads)
        executor.map(fetch_citations, range(len(df)), df['titulo'])

    # Adicionar as citações ao DataFrame
    df['Citações'] = citations_list

    # Salvar os dados no arquivo CSV com append
    df.to_csv("artigos_com_citacoes.csv", mode='w', header=True, index=False)
    print("Processamento concluído e arquivo gerado com as citações.")

# Iniciar o processamento em paralelo
process_in_parallel()
