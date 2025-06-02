import unittest
from io import StringIO
import sys

# Importe suas classes aqui se estiverem em outro arquivo, por exemplo:
# from seu_modulo import Usuario, Moderador, Topico

from moderacao import Usuario, Moderador, Topico  # se o código original estiver em "main.py"

class TestTopicoObserver(unittest.TestCase):
    def setUp(self):
        self.usuario = Usuario(
            nome="João",
            nome_usuario="joao123",
            senha="senha",
            permissoes=["postar", "editar"],
            idade=25,
            ranking="Bronze",
            qtd_likes=10,
            profissao="Estudante",
            cidade="São Paulo",
            qtd_comentarios=5,
            tipo_usuario="comum",
            descricao="Usuário ativo"
        )

        self.moderador = Moderador(
            nome="Ana",
            nome_usuario="ana_mod",
            senha="1234",
            permissoes=["moderar"],
            idade=30,
            ranking="Prata",
            qtd_likes=50,
            profissao="Professora",
            cidade="Rio de Janeiro",
            qtd_comentarios=100,
            tipo_usuario="moderador",
            descricao="Moderadora experiente",
            idModerador=1
        )

        self.topico = Topico(
            titulo="Título Exemplo",
            autor=self.usuario.nome_usuario,
            data_criacao=123456,
            tipo="Dúvida",
            descricao="Descrição inicial"
        )

        self.topico.vincular(self.moderador)

    def test_criar_topico_dispara_notificacao(self):
        # Captura a saída padrão para testar o print
        captured_output = StringIO()
        sys.stdout = captured_output

        self.topico.criarTopico(self.usuario)

        sys.stdout = sys.__stdout__  # Restaura a saída padrão

        output = captured_output.getvalue()
        self.assertIn("Topico 'Título Exemplo' criado por joao123", output)
        self.assertIn("Moderador ana_mod foi notificado de uma alteração.", output)

    def test_editar_topico_dispara_notificacao(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        self.topico.editar(self.usuario, "Nova descrição")

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("editado por joao123", output)
        self.assertIn("Moderador ana_mod foi notificado de uma alteração.", output)


if __name__ == '__main__':
    unittest.main()