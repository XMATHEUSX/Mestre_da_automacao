from sqlalchemy import create_engine, Column, Integer, String, Sequence, Numeric, ForeignKey, desc
from sqlalchemy.orm import relationship
from models.base import base


class Produto(base):
    __tablename__ = 'produto'
    produto_id = Column(Integer, Sequence(
        'produto_id_auto_incremento', start=1), primary_key=True)
    nome = Column(String)
    preco = Column(Numeric(10, 2))
    descricao = Column(String)
