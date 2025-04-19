# Import
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import yfinance as yf
import os

# Import das variaveis de ambiente
load_dotenv()

commodities = ['CL=F', 'GC=F', 'SI=F']

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASSWORD = os.getenv('DB_PASSWORD_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')
DB_THREADS = os.getenv('DB_THREADS_PROD')
DB_TYPE = os.getenv('DB_TYPE_PROD')
DBT_PROFILES_DIR = os.getenv('DBT_PROFILES_DIR')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)


def buscar_dados_commodities(simbolo, periodo = '5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados_commodities(commodities):
    return pd.concat([buscar_dados_commodities(simbolo) for simbolo in commodities])

def salvar_no_postgres(df, schema='public'):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)

if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities(commodities)
    salvar_no_postgres(dados_concatenados, schema='Public')


# pegar a cotacao dos ativos

# concatenar os meus ativos

# salvar no banco de dados

# pegar a cotacao dos ativos

# concatenar os meus ativos

# salvar no banco de dados

# pegar a cotacao dos ativos

# concatenar os meus ativos

# salvar no banco de dados

# pegar a cotacao dos ativos

# concatenar os meus ativos

# salvar no banco de dados