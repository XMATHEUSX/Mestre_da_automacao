from flask import Flask, jsonify, request

cancoes = [
    {
        "Nome": "Faded",
        "Estilo":"Eletrônica",
        "Autor": "Alan Walker"
    },
    {
        "Nome": "Rap L",
        "Estilo":"Rap Geek",
        "Autor": "7minutoz"
    },
    {
        "Nome": "Monster",
        "Estilo":"Rap Geek",
        "Autor": "Tauz"
    },
    {
        "Nome": "Admirável Chip Novo",
        "Estilo":"Rock Alternativo",
        "Autor": "Pitty"
    }
]
app = Flask(__name__)


@app.route('/cancoes', methods=['GET'])
def obter_todas_cancao():
    return jsonify(cancoes)


@app.route('/cancoes/<int:cancao_id>', methods=['GET'])
def obter_cancao_id(cancao_id):
    return jsonify(cancoes[cancao_id])

@app.route('/cancoes', methods=['POST'])
def nova_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)
    return jsonify({'mensagem':'recurso criado com sucesso'}),200

@app.route('/cancoes/<int:cancao_id>', methods=['PUT'])
def atualizar_cancao(cancao_id):
    resultado = request.get_json()
    cancoes[cancao_id].update(resultado)
    return jsonify({'mensagem':'recurso Atualizado com sucesso'}),200
    

@app.route('/cancoes/<int:cancao_id>', methods=['DELETE'])
def deletar_cancao(cancao_id):
    del cancoes[cancao_id]
    return jsonify({'mensagem':'recurso Deletado com sucesso'}),200


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
