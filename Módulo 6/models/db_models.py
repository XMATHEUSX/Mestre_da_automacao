from sqlalchemy import create_engine, Column, Integer, String, Sequence, Numeric, ForeignKey, desc
from sqlalchemy.orm import relationship
from models.base import base

class Artista(base):
    __tablename__ = 'artista'
    artista_id = Column(Integer, Sequence(
        'artista_id_auto_incremento', start=1), primary_key=True)
    nome = Column(String)
    albuns = relationship('Album')


class Estilo(base):
    __tablename__ = 'estilo'
    estilo_id = Column(Integer, Sequence(
        'estilo_id_auto_incremento', start=1), primary_key=True)
    nome = Column(String)


class Album(base):
    __tablename__ = 'album'
    album_id = Column(Integer, Sequence(
        'album_id_auto_incremento', start=1), primary_key=True)
    titulo = Column(String)
    preco = Column(Numeric(10, 2))
    artista_id = Column(Integer, ForeignKey(Artista.artista_id))
    estilo_id = Column(Integer, ForeignKey(Estilo.estilo_id))
    cancoes = relationship('Cancao')


class Cancao(base):
    __tablename__ = 'cancao'
    cancao_id = Column(Integer, Sequence(
        'cancao_id_auto_incremento', start=1), primary_key=True)
    nome = Column(String)
    album_id = Column(Integer, ForeignKey(Album.album_id))