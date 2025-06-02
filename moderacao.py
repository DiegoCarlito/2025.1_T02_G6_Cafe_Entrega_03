from typing import List, Dict

class Observador:
    def atualizar(self):
        pass

class SujeitoObserver:
    def __init__(self):
        self.observers: List[Observador] = []

    def vincular(self, observer: Observador):
        self.observers.append(observer)

    def desvincular(self, observer: Observador):
        self.observers.remove(observer)

    def notificar(self):
        for observer in self.observers:
            observer.atualizar()


# Classes principais
class Usuario:
    def __init__(self, nome, nome_usuario, senha, permissoes, idade, ranking, qtd_likes, profissao, cidade, qtd_comentarios, tipo_usuario, descricao):
        self.nome = nome
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.permissoes = permissoes
        self.idade = idade
        self.ranking = ranking
        self.qtd_likes = qtd_likes
        self.profissao = profissao
        self.cidade = cidade
        self.qtd_comentarios = qtd_comentarios
        self.tipo_usuario = tipo_usuario
        self.descricao = descricao

    def curtirResposta(self, resposta): pass
    def seguirTopico(self, topico): pass
    def seguirUsuario(self, usuario_origem, usuario_destino): pass
    def criarTopico(self): pass
    def acessarTopico(self, topico): pass
    def responderPostagem(self, topico, postagem): pass
    def editarResposta(self, resposta): pass
    def excluirResposta(self, resposta): pass
    def denunciarUsuario(self, usuario): pass


class Moderador(Usuario, Observador):
    def __init__(self, *args, idModerador=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.idModerador = idModerador
        self.estadoTopicosModerados: Dict[str, str] = {}

    def removerPostagem(self, topico, usuario): pass
    def aprovarTopico(self, topico): pass
    def removerResposta(self, topico, usuario): pass
    def obterEstadoTopico(self, topico): return self.estadoTopicosModerados.get(topico.titulo, "Desconhecido")

    def atualizar(self):
        print(f"Moderador {self.nome_usuario} foi notificado de uma alteração.")


class Topico(SujeitoObserver):
    def __init__(self, titulo, autor: str, data_criacao: int, tipo, descricao):
        super().__init__()
        self.titulo = titulo
        self.autor = autor
        self.data_criacao = data_criacao
        self.tipo = tipo
        self.descricao = descricao
        self.quantidade_posts = 0
        self.aprovado = False
        self.moderadores: List[Moderador] = []

    def criarTopico(self, usuario: Usuario):
        print(f"Topico '{self.titulo}' criado por {usuario.nome_usuario}")
        self.notificar()

    def editar(self, usuario: Usuario, string: str):
        self.descricao = string
        print(f"Topico '{self.titulo}' editado por {usuario.nome_usuario}")
        self.notificar()

    def acessarPostagem(self, postagem): pass
    def compartilhar(self, usuario: Usuario, id): pass
    def denunciar(self, usuario: Usuario, motivo: str): pass
