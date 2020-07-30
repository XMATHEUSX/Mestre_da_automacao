import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import base
from db_models import Album, Artista

def iniciar():
    configurar_bd()

def configurar_bd():
    # para Criar um banco de dados SQLite3
    engine = create_engine('sqlite:///artista.db', echo=True)
    base.metadata.drop_all(bind=engine)
    base.metadata.create_all(bind=engine)
    Conexao = sessionmaker(bind=engine)
    conexao = Conexao()
    return conexao 

# criar um novo artista
def criar_artista(conexao,nome):
    novo_artista = Artista()
    novo_artista.nome = nome
    conexao.add(novo_artista)
    conexao.commit()

def criar_album(conexao,nome,preco,artista_id):
    novo_album = Album()
    novo_album.titulo = nome
    novo_album.preco = preco
    novo_album.artista_id = artista_id
    conexao.add(novo_album)
    conexao.commit()

for item in conexao.query(Artista).all():
    print(item.artista_id, item.nome)
# obter a quantidade de registos em uma tabela
print(conexao.query(Album).count())


# obter a quantidade de registos em uma tabela
print(conexao.query(Album).count())

# pesquisa por itens que contem uma string
for item in conexao.query(Album).filter(Album.titulo.like('%novo%')):
    print(item.titulo, item.artista_id)

# filtra por propriedade especificas
for item in conexao.query(Album).filter(Album.artista_id == 4):
    print(item.titulo)

for item in conexao.query(Album).filter(Album.preco < 30.00):
    print(item.titulo, item.preco)

# alterar dados
album_a_ser_alterado = conexao.query(Album).filter(
    Album.titulo == 'Winter Times').first()
album_a_ser_alterado.titulo = 'Winter Times 3000'
conexao.commit()

for item in conexao.query(Album).filter(Album.artista_id == 4):
    print(item.titulo)

# deleta  dados
album_a_ser_alterado = conexao.query(Album).filter(
    Album.titulo == 'Winter Times 3000').first()
conexao.delete(album_a_ser_alterado)
conexao.commit()
# obtem os resultados ordenados baseados em alguma condição
# for item in conexao.query(Album).order_by(desc(Album.artista_id)):
#    print(item.titulo, item.artista_id)
# obtem o primeiro registro
#artista = conexao.query(Artista).first()
#print(artista.artista_id, artista.nome)
# obtem apenas a quantidade especificada
# for item in conexao.query(Album).limit(3):
#    print(item.titulo, item.artista_id)
# filtra por propriedade especificas
# for item in conexao.query(Album).filter(Album.album_id >= 1).\
#        filter(Album.preco >= 15.00):
#    print(item.titulo, item.preco)

# pesquisa por itens que contem uma string
# for item in conexao.query(Album).filter(Album.titulo.like('%Album%')):
#    print(item.titulo, item.artista_id)
