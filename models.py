from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    # PK e index para melhorar a performance nas buscas
    id = Column(Integer, primary_key=True, index=True)
    # nullable=False → Obrigatório, ou seja, não pode ser NULL
    nome = Column(String, nullable=False)
    # Unique -> CNPJ único para cada empresa
    cnpj = Column(String, unique=True, nullable=False)
    endereco = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")

class ObrigacaoAcessoria(Base):  # Corrigido (o nome deve ser exatamente esse)
    __tablename__ = "obrigacoes_acessorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    periodicidade = Column(String, nullable=False)
    
    # Liga cada obrigação a uma empresa específica.
    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    empresa = relationship("Empresa", back_populates="obrigacoes")
