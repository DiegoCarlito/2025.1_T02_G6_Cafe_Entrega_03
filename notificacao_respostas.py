class Resposta:
    def __init__(self, autor, descricao):
        self.autor = autor
        self.descricao = descricao

    def __repr__(self):
        return f"Resposta({self.autor.nome_usuario}: '{self.descricao}')"


class Usuario:
    def __init__(self, nome, nome_usuario):
        self.nome = nome
        self.nome_usuario = nome_usuario
        self.postagens = []
        self.respostas = []

    def notificar(self):
        print(f"[NOTIFICAÇÃO] {self.nome_usuario}, seu tópico recebeu uma nova resposta!")

    def registrarResposta(self, resposta):
        self.respostas.append(resposta)

    def __repr__(self):
        return f"Usuario({self.nome_usuario})"


class Postagem:
    def __init__(self, autor, data_criacao, descricao):
        self.autor = autor
        self.data_criacao = data_criacao
        self.descricao = descricao
        self.respostas = []

    def gerarResposta(self, usuario, texto):
        resposta = Resposta(usuario, texto)
        self.respostas.append(resposta)
        self.autor.notificar()
        usuario.registrarResposta(resposta)
        return resposta


class Topico(Postagem):
    def __init__(self, titulo, autor, data_criacao, descricao):
        super().__init__(autor, data_criacao, descricao)
        self.titulo = titulo

    def __repr__(self):
        return f"Topico('{self.titulo}', autor={self.autor.nome_usuario})"
