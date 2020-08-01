

@app.route('/postagens', methods=['GET'])
def obter_todas_postagem():
    pass


@app.route('/postagens/<int:postagem_id>', methods=['GET'])
def obter_postagem_id(postagem_id):
    pass


@app.route('/postagens', methods=['POST'])
def nova_postagem():
    pass


@app.route('/postagens/<int:postagem_id>', methods=['PUT'])
def atualizar_postagem(postagem_id):
    pass


@app.route('/postagens/<int:postagem_id>', methods=['DELETE'])
def deletar_postagem(postagem_id):
    pass


# criar uma api para criar novos autores


@app.route('/autores', methods=['GET'])
def obter_todas_autores():
    autores = Autor.query.all()
    lista_de_autores = []
    for autor in autores:
        dados_autores = {}
        dados_autores['id_autor'] = autor.autor_id
        dados_autores['nome'] = autor.nome
        dados_autores['email'] = autor.email
    return jsonify({'autores': lista_de_autores})


@app.route('/autores/<int:autor_id>', methods=['GET'])
def obter_autores_id(autor_id):
    autor = Autor.query.filter_by(autor_id=id_autor).first()

    if not autor:
        return jsonify({'mensagem': 'Autor não encontrado'})
    dados_autor = {}
    dados_autor['id_autor'] = autor.id_autor
    dados_autor['nome'] = autor.nome
    dados_autor['email'] = autor.email

    return jsonify({'autor': dados_autor})


@app.route('/autores', methods=['POST'])
def novo_autor():
    dados = request.get_json()
    novo_usuario = Autor(nome=dados["nome"],
                         senha=dados["senha"], email=dados["email"])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'Novo usuario criado com sucesso'})


@app.route('/autores/<int:autor_id>', methods=['PUT'])
def atualizar_autor(autor_id):
    pass


@app.route('/autores/<int:autor_id>', methods=['DELETE'])
def deletar_autor(autor_id):
    pass
