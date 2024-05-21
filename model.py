from sqlalchemy import Column, String, Integer, Double, DateTime
from connection import db
from datetime import datetime

class Inscricao(db.Model):
    __tablename__ = "inscricoes"

    id_inscricao = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    idade = Column(String, nullable=False)
    evento = Column(String, nullable=False)
    data = Column(DateTime, default=datetime.now())
    valor = Column(Double, nullable=False)
    telefone = Column(String, nullable=False)

class Contato(db.Model):
    __tablename__ = "contatos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    assunto = Column(String, nullable=False)
    mensagem = Column(String, nullable=False)