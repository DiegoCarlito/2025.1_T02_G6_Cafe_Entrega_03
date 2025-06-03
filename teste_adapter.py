from adapter import Noticia, Equipamento, Receita, Evento, TopicoAdapter

# Simulando um "gerenciador" simples para armazenar tópicos criados
class TopicoManager:
    def __init__(self):
        self.topicos = []

    def criar_topico(self, adapter):
        topico = adapter.criar()
        self.topicos.append(topico)
        print(f"Tópico criado: {topico}")

    def editar_topico(self, adapter, novo_nome):
        adapter.editar(novo_nome)
        print(f"Tópico editado para: {novo_nome}")

    def denunciar_topico(self, adapter):
        adapter.denunciar()
        print("Tópico denunciado.")

    def exibir_topicos(self):
        print("\n--- Tópicos Criados ---")
        for idx, topico in enumerate(self.topicos):
            print(f"{idx+1}. {topico}")

if __name__ == "__main__":
    manager = TopicoManager()

    noticia = Noticia(
        categoria="Tecnologia",
        autor="Maria",
        conteudo="Novo método de preparo de café.",
        data="2025-05-31",
        imagem="noticia1.png",
        fonte="Café News"
    )
    equipamento = Equipamento(
        nome_modelo="Cafeteira XPTO",
        tipo="Cafeteira",
        marca="CaféTop",
        valor=499.90
    )
    receita = Receita(
        cafe="Arábica",
        origem="Minas Gerais",
        data="2025-05-30",
        criador="João"
    )
    evento = Evento(
        local="Auditório Central",
        data="2025-06-10",
        tipo="Workshop",
        organizador="Associação do Café"
    )

    # Criando tópicos
    adapter_noticia = TopicoAdapter(noticia=noticia)
    manager.criar_topico(adapter_noticia)

    adapter_equipamento = TopicoAdapter(equipamento=equipamento)
    manager.criar_topico(adapter_equipamento)

    adapter_receita = TopicoAdapter(receita=receita)
    manager.criar_topico(adapter_receita)

    adapter_evento = TopicoAdapter(evento=evento)
    manager.criar_topico(adapter_evento)

    # Editando e denunciando tópicos
    manager.editar_topico(adapter_noticia, "Notícia Atualizada")
    manager.denunciar_topico(adapter_evento)

    # Exibindo todos os tópicos criados
    manager.exibir_topicos()

    