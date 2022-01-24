from flask_restful import Resource, reqparse
from models.filme import FilmeModel


class Filmes(Resource):
    def get(self):
        return {'filmes': [filme.json() for filme in FilmeModel.query.all()]}


class Filme(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('estrelas')
    atributos.add_argument('ano')
    atributos.add_argument('genero')

    def get(self, filme_id):
        filme = FilmeModel.find_filme(filme_id)
        if filme:
            return filme.json()
        return {'message': 'Filme not found.'}, 404

    def post(self, filme_id):
        if FilmeModel.find_filme(filme_id):
            return {"message": "Filme id '{}' alread exists.".format(filme_id)},

        dados = Filme.atributos.parse_args()
        filme = FilmeModel(filme_id, **dados)
        filme.save_filme()
        return filme.json()

    def put(self, filme_id):
        dados = Filme.atributos.parse_args()
        filme_encontrado = FilmeModel.find_filme(filme_id)
        if filme_encontrado:
            filme_encontrado.update_filme(**dados)
            filme_encontrado.save_filme()
            return filme_encontrado.json(), 200  # 0k
        filme = FilmeModel(filme_id, **dados)
        filme.save_filme()
        return filme.json(), 201  # created

    def delete(self, filme_id):
        filme = FilmeModel.find_filme(filme_id)
        if filme:
            filme.delete_filme()
            return {'message': 'Filme deleted.'}
        return{'message': 'Filme not found.'}, 404
