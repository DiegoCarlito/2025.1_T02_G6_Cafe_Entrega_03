import unittest
from notificacao_respostas import Usuario, Topico  # ajuste o nome do módulo

class TestForum(unittest.TestCase):
    def setUp(self):
        self.usuario1 = Usuario(nome="João Silva", nome_usuario="joao123")
        self.usuario2 = Usuario(nome="Ana Maria", nome_usuario="ana_m")

        self.topico1 = Topico(titulo="Dúvida sobre Python", autor=self.usuario1, data_criacao="2025-06-01", descricao="Como usar listas em Python?")
        self.topico2 = Topico(titulo="Sugestão de livro", autor=self.usuario2, data_criacao="2025-06-02", descricao="Qual o melhor livro para aprender algoritmos?")

    def test_respostas_e_notificacoes(self):
        resposta1 = self.topico1.gerarResposta(usuario=self.usuario2, texto="Você pode usar a função append() para adicionar itens.")
        resposta2 = self.topico2.gerarResposta(usuario=self.usuario1, texto="Recomendo o 'Algoritmos' do Cormen.")

        # Verifica se as respostas foram adicionadas ao tópico
        self.assertIn(resposta1, self.topico1.respostas)
        self.assertIn(resposta2, self.topico2.respostas)

        # Verifica se as respostas foram registradas no usuário correto
        self.assertIn(resposta1, self.usuario2.respostas)
        self.assertIn(resposta2, self.usuario1.respostas)

        # Verifica se o autor do tópico recebeu a notificação
        # Como notificar() só printa, não dá pra testar diretamente,
        # mas você pode mockar ou checar efeitos colaterais em um teste mais avançado.

if __name__ == "__main__":
    unittest.main()
