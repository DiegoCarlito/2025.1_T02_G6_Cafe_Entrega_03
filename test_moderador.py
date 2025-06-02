from moderacao import Usuario, Moderador, Topico
 
class TopicoManager:
    def __init__(self):
        self.topicos = []
 
    def criar_topico(self, topico, usuario):
        topico.criarTopico(usuario)
        self.topicos.append(topico)
        print(f"Tópico criado: {topico.titulo}")
 
    def editar_topico(self, topico, usuario, nova_descricao):
        topico.editar(usuario, nova_descricao)
        print(f"Tópico editado para: {nova_descricao}")
 
    def denunciar_topico(self, topico, usuario, motivo):
        topico.denunciar(usuario, motivo)
        print("Tópico denunciado.")
 
    def exibir_topicos(self):
        print("\n--- Tópicos Criados ---")
        for idx, topico in enumerate(self.topicos):
            print(f"{idx+1}. {topico.titulo} - {topico.descricao}")
 
if __name__ == "__main__":
    manager = TopicoManager()
 
    usuario = Usuario(
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
 
    moderador = Moderador(
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
 
    topico1 = Topico(
        titulo="Primeiro Tópico",
        autor=usuario.nome_usuario,
        data_criacao=123456,
        tipo="Dúvida",
        descricao="Descrição inicial"
    )
    topico1.vincular(moderador)
 
    topico2 = Topico(
        titulo="Segundo Tópico",
        autor=usuario.nome_usuario,
        data_criacao=123457,
        tipo="Sugestão",
        descricao="Outra descrição"
    )
    topico2.vincular(moderador)
 
    # Criando tópicos
    manager.criar_topico(topico1, usuario)
    manager.criar_topico(topico2, usuario)
 
    # Editando e denunciando tópicos
    manager.editar_topico(topico1, usuario, "Descrição atualizada do primeiro tópico")
    manager.denunciar_topico(topico2, usuario, "Conteúdo inapropriado")
 
    # Exibindo todos os tópicos criados
    manager.exibir_topicos()