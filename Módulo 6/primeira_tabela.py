import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import base
from models.db_models import Album, Artista


def iniciar():
    configurar_bd()

# para Criar um banco de dados SQLite3


def configurar_bd():

    engine = create_engine('sqlite:///artista.db', echo=True)
    base.metadata.drop_all(bind=engine)
    base.metadata.create_all(bind=engine)
    Conexao = sessionmaker(bind=engine)
    conexao = Conexao()
    return conexao

# criar um novo artista


def criar_artista(conexao, nome):
    novo_artista = Artista()
    novo_artista.nome = nome
    conexao.add(novo_artista)
    conexao.commit()

# criar um novo album


def criar_album(conexao, nome, preco, artista_id):
    novo_album = Album()
    novo_album.titulo = nome
    novo_album.preco = preco
    novo_album.artista_id = artista_id
    conexao.add(novo_album)
    conexao.commit()


# alterar dados
# album_a_ser_alterado = conexao.query(Album).filter(
#   Album.titulo == 'Winter Times').first()
#album_a_ser_alterado.titulo = 'Winter Times 3000'
# conexao.commit()

# deleta  dados
# album_a_ser_alterado = conexao.query(Album).filter(
#    Album.titulo == 'Winter Times 3000').first()
# conexao.delete(album_a_ser_alterado)
# conexao.commit()

# QUERY

def Todos_artista(conexao):
    for item in conexao.query(Artista).all():
        print(item.artista_id, item.nome)


def quantidade__de_albuns(conexao):
    # obter a quantidade de registos em uma tabela
    print(conexao.query(Album).count())


def Procura_string(conexao, texto):
    # pesquisa por itens que contem uma string
    for item in conexao.query(Album).filter(Album.titulo.like(texto)):
        print(item.titulo, item.artista_id)
