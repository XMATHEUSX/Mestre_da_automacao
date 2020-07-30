# filtra por propriedade especificas
# for item in conexao.query(Album).filter(Album.artista_id == 4):
#    print(item.titulo)

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
