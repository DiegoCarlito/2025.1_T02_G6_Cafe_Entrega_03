from abc import ABC, abstractmethod
from typing import List


# === Interface IUsuario ===
class IUsuario(ABC):
    @abstractmethod
    def acesso_topico(self) -> bool:
        pass

# === Decorator: Usuário Convidado ===
class UsuarioConvidado(IUsuario):
    def acesso_topico(self) -> bool:
        print("Convidado: acesso somente leitura.")
        return True

# === Decorator: Usuário Logado ===
class UsuarioLogado(IUsuario):
    def __init__(self, componente: IUsuario):
        self.componente = componente
        self.permissoes: List[str] = []
        self.rank: str = "membro"

    def acesso_topico(self) -> bool:
        return self.componente.acesso_topico()

    def comentar(self):
        print("Comentário realizado.")

    def excluir_comentario(self, comentario: str):
        print(f"Comentário '{comentario}' excluído.")

    def visualizar_links(self):
        print("Links visíveis para o usuário.")

# === Decorator: Lojista ===
class Lojista(IUsuario):
    def __init__(self, componente: UsuarioLogado):
        self.componente = componente
        self.estabelecimento = None

    def criar_estabelecimento(self, nome: str):
        self.estabelecimento = nome
        print(f"Estabelecimento '{nome}' criado.")
        return self.estabelecimento

    def acesso_topico(self) -> bool:
        return self.componente.acesso_topico()

    def visualizar_links(self):
        self.componente.visualizar_links()

    def comentar(self):
        self.componente.comentar()

    def excluir_comentario(self, comentario: str):
        self.componente.excluir_comentario(comentario)

# === Decorator: Moderador ===
class Moderador(IUsuario):
    def __init__(self, componente: UsuarioLogado, id_moderador: int):
        self.componente = componente
        self.id_moderador = id_moderador

    def aprovar_topico(self, topico: str):
        print(f"Tópico '{topico}' aprovado.")

    def remover_postagem(self, postagem: str):
        print(f"Postagem '{postagem}' removida.")

    def remover_permissoes(self, usuario: IUsuario, permissao: str):
        print(f"Permissão '{permissao}' removida do usuário.")

    def acesso_topico(self) -> bool:
        return self.componente.acesso_topico()

    def visualizar_links(self):
        self.componente.visualizar_links()

    def comentar(self):
        self.componente.comentar()

    def excluir_comentario(self, comentario: str):
        self.componente.excluir_comentario(comentario)

# === Decorator: Administrador ===
class Administrador(IUsuario):
    def __init__(self, componente: UsuarioLogado, id_adm: int):
        self.componente = componente
        self.id_adm = id_adm

    def aprovar_topico(self, topico: str):
        print(f"Administrador aprovou o tópico: {topico}")

    def remover_postagem(self, postagem: str):
        print(f"Administrador removeu a postagem: {postagem}")

    def conceder_permissoes(self, usuario: IUsuario, permissao: str):
        print(f"Permissão '{permissao}' concedida ao usuário.")

    def remover_permissoes(self, usuario: IUsuario, permissao: str):
        print(f"Permissão '{permissao}' removida do usuário.")

    def acesso_topico(self) -> bool:
        return self.componente.acesso_topico()

    def visualizar_links(self):
        self.componente.visualizar_links()

    def comentar(self):
        self.componente.comentar()

    def excluir_comentario(self, comentario: str):
        self.componente.excluir_comentario(comentario)

if __name__ == "__main__":
    print("\n--- USUÁRIO CONVIDADO ---")
    convidado = UsuarioConvidado()
    convidado.acesso_topico()

    print("\n--- USUÁRIO LOGADO ---")
    usuario_logado = UsuarioLogado(convidado)
    usuario_logado.acesso_topico()
    usuario_logado.comentar()
    usuario_logado.visualizar_links()

    print("\n--- LOJISTA ---")
    lojista = Lojista(usuario_logado)
    lojista.acesso_topico()
    lojista.comentar()
    lojista.criar_estabelecimento("Café dos Sonhos")

    print("\n--- MODERADOR ---")
    moderador = Moderador(usuario_logado, id_moderador=101)
    moderador.aprovar_topico("Novas Regras do Fórum")
    moderador.remover_postagem("Spam")
    moderador.comentar()

    print("\n--- ADMINISTRADOR ---")
    adm = Administrador(usuario_logado, id_adm=1)
    adm.aprovar_topico("Atualização da Plataforma")
    adm.conceder_permissoes(usuario_logado, "publicar_evento")
