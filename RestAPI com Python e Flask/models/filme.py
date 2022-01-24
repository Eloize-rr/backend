from sql_alchemy import banco


class FilmeModel(banco.Model):
    __tablename__ = 'filmes'

    filme_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    ano = banco.Column(banco.Float(precision=2))
    genero = banco.Column(banco.String(80))

    def __init__(self, filme_id, nome, estrelas, ano, genero):
        self.filme_id = filme_id
        self.nome = nome
        self.estrelas = estrelas
        self.ano = ano
        self.genero = genero

    def json(self):
        return {
            'filme_id': self.filme_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'ano': self.ano,
            'genero': self.genero
        }

    @classmethod
    def find_filme(cls, filme_id):
        filme = cls.query.filter_by(filme_id=filme_id).first()
        if filme:
            return filme
        return None

    def save_filme(self):
        banco.session.add(self)
        banco.session.commit()

    def update_filme(self, nome, estrelas, ano, genero):
        self.nome = nome
        self.estrelas = estrelas
        self.ano = ano
        self.genero = genero

    def delete_filme(self):
        banco.session.delete(self)
        banco.session.commit()
