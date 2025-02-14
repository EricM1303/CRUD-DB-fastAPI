# Conexão com o banco de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

if load_dotenv():
    print("Arquivo .env carregado com sucesso!")
else:
    print("Erro ao carregar o arquivo .env")

db_url = os.getenv("URL_DATABASE")

engine = create_engine(db_url)
# As alterações não são salvas automaticamente / Evita atualizações automáticas antes de cada consulta / 
# Conecta essa sessão ao banco criado com engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Todos os modelos (tabelas) do banco serão filhos dessa Base
Base = declarative_base()