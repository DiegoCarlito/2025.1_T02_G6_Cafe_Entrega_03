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

# Cadastrando um lojista
lojista = Lojista("João")
gestao.cadastrarLojista(lojista)

# Criando e adicionando uma loja
loja = Estabelecimento("Mercado Central", "Centro")
lojista.criar_loja(loja)
gestao.adicionarEstabelecimento(loja)

# Adicionando produtos à loja
p1 = Produto("Arroz", 20.50, loja)
p2 = Produto("Feijão", 7.30, loja)
gestao.cadastrarProduto(p1, loja)
gestao.cadastrarProduto(p2, loja)

# Adicionando avaliações
loja.adicionar_avaliacao(4)
loja.adicionar_avaliacao(5)
loja.adicionar_avaliacao(3)

# Exibindo produtos
print("Produtos disponíveis:")
for produto in gestao.exibirProdutos(loja):
    print(produto.exibir_resumo())

# Mostrando média de avaliações
print(f"\nMédia de avaliações da loja '{loja.nome}': {gestao.obterMediaAvaliacoes(loja)}")

# Listando todas as lojas
print("\nTodas as lojas cadastradas:")
for l in gestao.listarTodasLojas():
    print(f"- {l.nome} ({l.localizacao})")
