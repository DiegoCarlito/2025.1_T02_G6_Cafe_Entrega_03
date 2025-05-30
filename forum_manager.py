import threading
from datetime import datetime

# Logger Singleton
class Logger:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self._log_file = "registro_comunidade_cafe.txt"
        self._file_lock = threading.Lock()

    @classmethod
    def get_logger(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = Logger()
            return cls._instance

    def _obter_timestamp(self):
        agora = datetime.now()
        return agora.strftime("%d/%m/%Y %H:%M:%S")

    def _escrever_log(self, mensagem):
        with self._file_lock:
            try:
                with open(self._log_file, "a", encoding="utf-8") as f:
                    f.write(f"{self._obter_timestamp()} - {mensagem}\n")
            except Exception as e:
                print(f"Erro ao escrever no log: {e}")

    def registrar_sucesso(self, mensagem):
        self._escrever_log(f"SUCESSO - {mensagem}")

    def registrar_erro(self, mensagem):
        self._escrever_log(f"ERRO - {mensagem}")

    def registrar_aviso(self, mensagem):
        self._escrever_log(f"AVISO - {mensagem}")

    def obter_log(self):
        with self._file_lock:
            try:
                with open(self._log_file, "r", encoding="utf-8") as f:
                    return f.read()
            except FileNotFoundError:
                return "Nenhum registro encontrado na comunidade ainda."

# ForumManager Singleton
class ComunidadeCafeManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._membros = set()
                cls._instance._discussoes = {}
                cls._instance._logger = Logger.get_logger()
            return cls._instance

    def adicionar_membro(self, nome):
        if nome in self._membros:
            self._logger.registrar_aviso(f"Membro '{nome}' já está na comunidade.")
            return f"O membro '{nome}' já está na comunidade."
        self._membros.add(nome)
        self._logger.registrar_sucesso(f"Membro '{nome}' entrou na comunidade do café.")
        return f"Bem-vindo à comunidade do café, {nome}!"

    def iniciar_discussao(self, titulo, autor):
        if autor not in self._membros:
            self._logger.registrar_erro(f"Tentativa de iniciar discussão por membro não cadastrado: {autor}")
            return f"Erro: O membro '{autor}' não está cadastrado na comunidade."
        if titulo in self._discussoes:
            self._logger.registrar_aviso(f"A discussão '{titulo}' já existe.")
            return f"A discussão '{titulo}' já foi iniciada."
        self._discussoes[titulo] = {"autor": autor, "mensagens": []}
        self._logger.registrar_sucesso(f"Discussão '{titulo}' iniciada por '{autor}'.")
        return f"Discussão '{titulo}' iniciada com sucesso."

    def adicionar_mensagem(self, titulo_discussao, autor, mensagem):
        if autor not in self._membros:
            self._logger.registrar_erro(f"Membro não cadastrado '{autor}' tentou enviar mensagem.")
            return f"Erro: O membro '{autor}' não está na comunidade."
        if titulo_discussao not in self._discussoes:
            self._logger.registrar_erro(f"Tentativa de mensagem em discussão inexistente: {titulo_discussao}")
            return f"Erro: A discussão '{titulo_discussao}' não existe."
        nova_mensagem = {"autor": autor, "mensagem": mensagem}
        self._discussoes[titulo_discussao]["mensagens"].append(nova_mensagem)
        self._logger.registrar_sucesso(f"Mensagem adicionada à discussão '{titulo_discussao}' por '{autor}'.")
        return f"Mensagem adicionada com sucesso à discussão '{titulo_discussao}'."

    def obter_log(self):
        return self._logger.obter_log()

# Exemplo de uso
if __name__ == "__main__":
    comunidade = ComunidadeCafeManager()

    print(comunidade.adicionar_membro("Ana"))
    print(comunidade.adicionar_membro("João"))
    print(comunidade.adicionar_membro("Ana"))  # Já está na comunidade

    print(comunidade.iniciar_discussao("Melhores métodos de preparo", "Ana"))
    print(comunidade.iniciar_discussao("Melhores métodos de preparo", "Ana"))  # Já existe
    print(comunidade.iniciar_discussao("História do café", "Carlos"))  # Membro não existe

    print(comunidade.adicionar_mensagem("Melhores métodos de preparo", "Ana", "Eu adoro o método Hario V60!"))
    print(comunidade.adicionar_mensagem("Melhores métodos de preparo", "João", "Prefiro a prensa francesa."))
    print(comunidade.adicionar_mensagem("Melhores métodos de preparo", "Carlos", "Alguém já usou aeropress?"))  # Membro não existe
    print(comunidade.adicionar_mensagem("Cafés Africanos", "Ana", "Quais vocês recomendam?"))  # Discussão não existe

    print("\nRegistro de atividades da Comunidade do Café:")
    print(comunidade.obter_log())
