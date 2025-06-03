from forum_manager import ComunidadeCafeManager  # Importa o singleton

# Execução do cenário de testes
manager = ComunidadeCafeManager()

# Criar usuários
manager.registrar_usuario("Alice Souza", "alice", "123")
manager.registrar_usuario("Bruno Lima", "bruno", "456")

# Criar tópico
manager.criar_topico("Melhores Cafés do Sul", "alice", "Discussão", "Compartilhe lugares com café especial no sul do Brasil.")

# Adicionar postagens
manager.adicionar_postagem("Melhores Cafés do Sul", "bruno", "Eu visitei um ótimo café em Florianópolis chamado Café Cultura!")
manager.adicionar_postagem("Melhores Cafés do Sul", "alice", "Adoro o Café do Mercado em Porto Alegre. Ótimo ambiente e grãos especiais.")

# Responder postagens
manager.responder_postagem("Melhores Cafés do Sul", 0, "alice", "Nossa, já ouvi falar! Vale a visita?")
manager.responder_postagem("Melhores Cafés do Sul", 1, "bruno", "Esse também é ótimo! Já fui lá uma vez.")

# Mostrar resultados
manager.exibir_topicos()
manager.exibir_postagens_do_topico("Melhores Cafés do Sul")
manager.exibir_respostas_da_postagem("Melhores Cafés do Sul", 0)
manager.exibir_respostas_da_postagem("Melhores Cafés do Sul", 1)
