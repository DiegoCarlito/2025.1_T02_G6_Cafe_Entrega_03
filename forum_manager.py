class Usuario:
    def __init__(self, nome, nome_usuario, senha, permissoes):
        self.nome = nome
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.permissoes = permissoes
        self.topicos_seguidos = set()
        self.usuarios_seguidos = set()

    def seguir_topico(self, topico):
        self.topicos_seguidos.add(topico)

    def seguir_usuario(self, outro_usuario):
        self.usuarios_seguidos.add(outro_usuario)

    def curtir_resposta(self, resposta):
        resposta.curtir()

    def denunciar_resposta(self, resposta):
        resposta.denunciar()

    def __str__(self):
        return f'@{self.nome_usuario}'

class Resposta:
    def __init__(self, conteudo, autor):
        self.conteudo = conteudo
        self.autor = autor
        self.quantidade_likes = 0

    def curtir(self):
        self.quantidade_likes += 1

    def denunciar(self):
        print(f"Resposta de {self.autor} denunciada.")

    def __str__(self):
        return f'Resposta({self.conteudo[:30]}...)'

class Postagem:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto
        self.respostas = []

    def adicionar_resposta(self, resposta):
        self.respostas.append(resposta)

    def editar_postagem(self, novo_texto):
        self.texto = novo_texto

    def __str__(self):
        return f'Postagem de {self.autor}: {self.texto[:40]}...'

class Topico:
    def __init__(self, titulo, autor, tipo, descricao):
        self.titulo = titulo
        self.autor = autor
        self.tipo = tipo
        self.descricao = descricao
        self.postagens = []

    def adicionar_postagem(self, postagem):
        self.postagens.append(postagem)

    def __str__(self):
        return f'Tópico: {self.titulo} ({self.tipo})'

class ComunidadeCafeManager:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ComunidadeCafeManager, cls).__new__(cls)
            cls._instancia._inicializar()
        return cls._instancia

    def _inicializar(self):
        self.usuarios = {}
        self.topicos = []

    def registrar_usuario(self, nome, nome_usuario, senha, permissoes="padrão"):
        if nome_usuario not in self.usuarios:
            usuario = Usuario(nome, nome_usuario, senha, permissoes)
            self.usuarios[nome_usuario] = usuario
            print(f"Usuário @{nome_usuario} registrado com sucesso.")
        else:
            print("Nome de usuário já existe.")

    def criar_topico(self, titulo, nome_usuario, tipo, descricao):
        if nome_usuario not in self.usuarios:
            print("Usuário não encontrado.")
            return

        autor = self.usuarios[nome_usuario]
        topico = Topico(titulo, autor, tipo, descricao)
        self.topicos.append(topico)
        print(f"Tópico '{titulo}' criado por @{nome_usuario}.")
        return topico

    def adicionar_postagem(self, titulo_topico, nome_usuario, texto):
        topico = next((t for t in self.topicos if t.titulo == titulo_topico), None)
        if not topico:
            print("Tópico não encontrado.")
            return

        if nome_usuario not in self.usuarios:
            print("Usuário não encontrado.")
            return

        autor = self.usuarios[nome_usuario]
        postagem = Postagem(autor, texto)
        topico.adicionar_postagem(postagem)
        print(f"Postagem adicionada ao tópico '{titulo_topico}' por @{nome_usuario}.")
        return postagem

    def responder_postagem(self, titulo_topico, index_postagem, nome_usuario, conteudo_resposta):
        topico = next((t for t in self.topicos if t.titulo == titulo_topico), None)
        if not topico:
            print("Tópico não encontrado.")
            return

        if nome_usuario not in self.usuarios:
            print("Usuário não encontrado.")
            return

        try:
            postagem = topico.postagens[index_postagem]
        except IndexError:
            print("Postagem não encontrada.")
            return

        autor = self.usuarios[nome_usuario]
        resposta = Resposta(conteudo_resposta, autor)
        postagem.adicionar_resposta(resposta)
        print(f"Resposta adicionada por @{nome_usuario} à postagem #{index_postagem} em '{titulo_topico}'.")

    def exibir_topicos(self):
        print("=== Tópicos ===")
        for t in self.topicos:
            print(t)

    def exibir_postagens_do_topico(self, titulo_topico):
        topico = next((t for t in self.topicos if t.titulo == titulo_topico), None)
        if not topico:
            print("Tópico não encontrado.")
            return

        print(f"--- Postagens em '{titulo_topico}' ---")
        for i, p in enumerate(topico.postagens):
            print(f"[{i}] {p}")

    def exibir_respostas_da_postagem(self, titulo_topico, index_postagem):
        topico = next((t for t in self.topicos if t.titulo == titulo_topico), None)
        if not topico:
            print("Tópico não encontrado.")
            return

        try:
            postagem = topico.postagens[index_postagem]
        except IndexError:
            print("Postagem não encontrada.")
            return

        print(f"--- Respostas da postagem #{index_postagem} em '{titulo_topico}' ---")
        for r in postagem.respostas:
            print(f"- {r}")
