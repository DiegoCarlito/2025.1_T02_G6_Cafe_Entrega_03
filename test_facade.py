class Produto:
    def __init__(self, nome, preco, estabelecimento):
        self.nome = nome
        self.preco = preco
        self.estabelecimento = estabelecimento
        self.disponivel = True

    def exibir_resumo(self):
        return f"{self.nome} - R${self.preco:.2f}"


class Estabelecimento:
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao
        self.produtos = []
        self.avaliacoes = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def adicionar_avaliacao(self, nota):
        self.avaliacoes.append(nota)

    def media_avaliacoes(self):
        if not self.avaliacoes:
            return "Sem avaliações"
        media = sum(self.avaliacoes) / len(self.avaliacoes)
        return f"{media:.2f}"


class Lojista:
    def __init__(self, nome):
        self.nome = nome
        self.lojas = []

    def criar_loja(self, loja):
        self.lojas.append(loja)


class GestaoEstabelecimento:
    def __init__(self):
        self.lojistas = {}  
        self.estabelecimentos = []  

    def cadastrarLojista(self, lojista):
        self.lojistas[lojista.nome] = lojista

    def cadastrarProduto(self, produto, est):
        est.adicionar_produto(produto)

    def obterMediaAvaliacoes(self, est):
        return est.media_avaliacoes()

    def listarTodasLojas(self):
        return [loja for lojista in self.lojistas.values() for loja in lojista.lojas]

    def exibirProdutos(self, est):
        return est.produtos

    def listarEstabelecimentos(self):
        return self.estabelecimentos

    def adicionarEstabelecimento(self, est):
        self.estabelecimentos.append(est)


# --- USO / TESTE DO SISTEMA ---

gestao = GestaoEstabelecimento()

# Cadastrando um barista (lojista)
barista = Lojista("Ana")
gestao.cadastrarLojista(barista)

# Criando e adicionando uma cafeteria
cafeteria = Estabelecimento("Café Central", "Centro")
barista.criar_loja(cafeteria)
gestao.adicionarEstabelecimento(cafeteria)

# Adicionando produtos ao cardápio da cafeteria
bebida1 = Produto("Cappuccino", 12.00, cafeteria)
bebida2 = Produto("Latte", 10.50, cafeteria)
gestao.cadastrarProduto(bebida1, cafeteria)
gestao.cadastrarProduto(bebida2, cafeteria)

# Adicionando avaliações dos clientes
cafeteria.adicionar_avaliacao(5)
cafeteria.adicionar_avaliacao(4)
cafeteria.adicionar_avaliacao(5)

# Exibindo o cardápio
print("Bebidas disponíveis:")
for produto in gestao.exibirProdutos(cafeteria):
    print(produto.exibir_resumo())

# Mostrando média de avaliações
print(f"\nMédia de avaliações da cafeteria '{cafeteria.nome}': {gestao.obterMediaAvaliacoes(cafeteria)}")

# Listando todas as cafeterias cadastradas
print("\nTodas as cafeterias cadastradas:")
for l in gestao.listarTodasLojas():
    print(f"- {l.nome} ({l.localizacao})")

