from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Criará todas tabelas e colunas no PostgreSQL
models.Base.metadata.create_all(bind=engine)

# Modelos Pydantic (validar os dados que chegam na API)
class Empresa(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class ObrigacaoAcessoria(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

# Conexão ao DB (sempre fechará ao final)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/empresas/")
async def read_empresas(db: db_dependency):
    empresas = db.query(models.Empresa).all()
    return empresas


@app.post("/empresas/") # Create empresas 
async def create_empresa(empresa: Empresa, db: db_dependency):
    db_empresa = models.Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa


@app.post("/obrigacoes_acessorias/") # Create obrigacoes
async def create_obrigacao(obrigacao: ObrigacaoAcessoria, db: db_dependency):
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao


@app.get("/obrigacoes_acessorias/{empresa_id}") # Read
async def read_obrigacoes(empresa_id: int, db: db_dependency):
    obrigacoes = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.empresa_id == empresa_id).all()
    return obrigacoes


@app.put("/empresas/{empresa_id}") # Update
async def update_empresa(empresa_id: int, empresa: Empresa, db: db_dependency):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa not found")
    
    db_empresa.nome = empresa.nome
    db_empresa.cnpj = empresa.cnpj
    db_empresa.endereco = empresa.endereco
    db_empresa.email = empresa.email
    db_empresa.telefone = empresa.telefone

    db.commit()
    db.refresh(db_empresa)
    return db_empresa


@app.delete("/empresas/{empresa_id}") # Delete
async def delete_empresa(empresa_id: int, db: db_dependency):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa not found")
    
    db.delete(db_empresa)
    db.commit()
    return {"message": "Empresa deletada com sucesso!"}

