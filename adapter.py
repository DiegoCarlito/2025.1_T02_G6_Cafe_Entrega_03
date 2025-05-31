from abc import ABC, abstractmethod

class Noticia:
    def __init__(self, categoria, autor, conteudo, data, imagem, fonte):
        self.categoria = categoria
        self.autor = autor
        self.conteudo = conteudo
        self.data = data
        self.imagem = imagem
        self.fonte = fonte

class Equipamento:
    def __init__(self, nome_modelo, tipo, marca, valor):
        self.nome_modelo = nome_modelo
        self.tipo = tipo
        self.marca = marca
        self.valor = valor

class Receita:
    def __init__(self, cafe, origem, data, criador):
        self.cafe = cafe
        self.origem = origem
        self.data = data
        self.criador = criador

class Evento:
    def __init__(self, local, data, tipo, organizador):
        self.local = local
        self.data = data
        self.tipo = tipo
        self.organizador = organizador

# --- Interface Adapter ---

class TopicoAdapterInterface(ABC):
    @abstractmethod
    def criar(self):
        pass

    @abstractmethod
    def editar(self, topico):
        pass

    @abstractmethod
    def denunciar(self):
        pass

# --- Adapter unificado ---

class TopicoAdapter(TopicoAdapterInterface):
    def __init__(self, noticia=None, equipamento=None, receita=None, evento=None):
        self.noticia = noticia
        self.equipamento = equipamento
        self.receita = receita
        self.evento = evento

    def criar(self):
        if self.noticia:
            return self._criar_noticia()
        elif self.equipamento:
            return self._criar_equipamento()
        elif self.receita:
            return self._criar_receita()
        elif self.evento:
            return self._criar_evento()
        else:
            raise ValueError("Nenhum tópico fornecido para criação.")

    def editar(self, topico):
        print(f"Editando tópico: {topico}")

    def denunciar(self):
        print("Denúncia registrada.")

    def _criar_noticia(self):
        return f"Notícia criada: {self.noticia.categoria} - {self.noticia.autor} - {self.noticia.fonte}"

    def _criar_equipamento(self):
        return f"Equipamento criado: {self.equipamento.nome_modelo} - {self.equipamento.marca}"

    def _criar_receita(self):
        return f"Receita criada: {self.receita.cafe} - {self.receita.origem}"

    def _criar_evento(self):
        return f"Evento criado: {self.evento.tipo} em {self.evento.local} por {self.evento.organizador}"
    
    