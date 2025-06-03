from abc import ABC, abstractmethod
from datetime import date


# === Interface Builder ===
class Builder(ABC):
    @abstractmethod
    def reset(self): pass

    @abstractmethod
    def set_criador(self, nome): pass

    @abstractmethod
    def set_data_criacao(self, data): pass

    @abstractmethod
    def set_titulo(self, titulo): pass

    @abstractmethod
    def get_result(self): pass


# === Diretor ===
class Diretor:
    def __init__(self, builder: Builder = None):
        self.builder = builder

    def mudar_builder(self, builder: Builder):
        self.builder = builder

    def construir_receita(self):
        self.builder.reset()
        self.builder.set_criador("Maria Barista")
        self.builder.set_data_criacao("2025-06-01")
        self.builder.set_titulo("Cold Brew com Canela")

    def construir_evento(self):
        self.builder.reset()
        self.builder.set_criador("João Café")
        self.builder.set_data_criacao("2025-06-10")
        self.builder.set_titulo("Workshop de Latte Art")

    def construir_produto(self):
        self.builder.reset()
        self.builder.set_criador("Café Central")
        self.builder.set_data_criacao("2025-06-01")
        self.builder.set_titulo("Pacote 500g Bourbon Amarelo")

class Produto:
    def __init__(self):
        self.nome = None
        self.descricao = None
        self.categoria = None
        self.preco = 0.0
        self.disponivel = True
        self.imagem = None
        self.estabelecimento = None

    def __str__(self):
        return f"[Produto] {self.nome} - R${self.preco} ({'Disponível' if self.disponivel else 'Indisponível'}) - [Descrição] {self.descricao}"


class ProdutoBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.produto = Produto()

    def set_criador(self, nome):
        self.produto.estabelecimento = nome

    def set_data_criacao(self, data):
        self.produto.data_criacao = data

    def set_titulo(self, titulo):
        self.produto.nome = titulo

    def set_categoria(self, categoria):
        self.produto.categoria = categoria

    def set_preco(self, preco):
        self.produto.preco = preco

    def set_descricao_produto(self, descricao):
        self.produto.descricao = descricao

    def set_disponibilidade(self, status: bool):
        self.produto.disponivel = status

    def get_result(self):
        return self.produto

class Evento:
    def __init__(self):
        self.organizador = None
        self.tipo = None
        self.valor_entrada = 0.0
        self.data = None
        self.uid = None
        self.cidade = None
        self.bairro = None
        self.rua = None
        self.status = False

    def __str__(self):
        return f"[Evento] {self.tipo} por {self.organizador} em {self.data} - {self.cidade}, {self.bairro}"


class EventoBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.evento = Evento()

    def set_criador(self, nome):
        self.evento.organizador = nome

    def set_data_criacao(self, data):
        self.evento.data = data

    def set_titulo(self, titulo):
        self.evento.tipo = titulo

    def set_valor_entrada(self, valor):
        self.evento.valor_entrada = valor

    def set_rua(self, rua):
        self.evento.rua = rua

    def set_bairro(self, bairro):
        self.evento.bairro = bairro

    def set_cidade(self, cidade):
        self.evento.cidade = cidade

    def set_status(self, status):
        self.evento.status = status

    def get_result(self):
        return self.evento

class Receita:
    def __init__(self):
        self.cafe = None
        self.origem = None
        self.data_criacao = None
        self.criador = None
        self.categoria = None
        self.descricao = None

    def __str__(self):
        return f"[Receita] {self.cafe} por {self.criador} - {self.categoria} ({self.origem})"


class ReceitaBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.receita = Receita()

    def set_criador(self, nome):
        self.receita.criador = nome

    def set_data_criacao(self, data):
        self.receita.data_criacao = data

    def set_titulo(self, cafe):
        self.receita.cafe = cafe

    def set_categoria(self, categoria):
        self.receita.categoria = categoria

    def set_origem(self, origem):
        self.receita.origem = origem

    def set_descricao(self, desc):
        self.receita.descricao = desc

    def get_result(self):
        return self.receita

if __name__ == "__main__":
    diretor = Diretor()

    # Construir um evento
    evento_builder = EventoBuilder()
    diretor.mudar_builder(evento_builder)
    diretor.construir_evento()
    evento_builder.set_valor_entrada(50.0)
    evento_builder.set_cidade("São Paulo")
    evento_builder.set_bairro("Centro")
    evento_builder.set_rua("Rua do Café")
    evento_builder.set_status(True)
    evento = evento_builder.get_result()
    #print(evento)

    # Construir uma receita
    receita_builder = ReceitaBuilder()
    diretor.mudar_builder(receita_builder)
    diretor.construir_receita()
    receita_builder.set_categoria("Gelado")
    receita_builder.set_origem("Etiópia")
    receita_builder.set_descricao("Infusão lenta com canela")
    receita = receita_builder.get_result()
    #print(receita)

    # Construir um produto
    produto_builder = ProdutoBuilder()
    diretor.mudar_builder(produto_builder)
    diretor.construir_produto()
    produto_builder.set_categoria("Grãos")
    produto_builder.set_preco(39.90)
    produto_builder.set_descricao_produto("Grãos de café Bourbon Amarelo, torra média")
    produto_builder.set_disponibilidade(True)
    produto = produto_builder.get_result()
    print(produto)
