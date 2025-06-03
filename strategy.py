from abc import ABC, abstractmethod
from typing import List

#  Interface Strategy 
class EstrategiaRankeamento(ABC):
    @abstractmethod
    def calcular(self, usuario) -> float:
        pass

# Estratégias Concretas 
class RankPorParticipacao(EstrategiaRankeamento):
    def calcular(self, usuario) -> float:
        return len(usuario.comentarios) * 1.5 + len(usuario.topicos) * 2

class RankPorAvaliacoes(EstrategiaRankeamento):
    def calcular(self, usuario) -> float:
        if not usuario.avaliacoes:
            return 0.0
        return sum(usuario.avaliacoes) / len(usuario.avaliacoes)

class RankPorTempoNoSistema(EstrategiaRankeamento):
    def calcular(self, usuario) -> float:
        return usuario.meses_ativo * 0.8

#  Contexto 
class Usuario:
    def __init__(self, nome: str):
        self.nome = nome
        self.comentarios: List[str] = []
        self.topicos: List[str] = []
        self.avaliacoes: List[float] = []
        self.meses_ativo: int = 0
        self._estrategia: EstrategiaRankeamento = None

    def set_estrategia_rankeamento(self, estrategia: EstrategiaRankeamento):
        self._estrategia = estrategia

    def calcular_rank(self) -> float:
        if not self._estrategia:
            raise Exception("Estratégia de rankeamento não definida.")
        return self._estrategia.calcular(self)

    def __str__(self):
        return f"Usuário {self.nome}"

#  Exemplo de uso 
if __name__ == "__main__":
    user = Usuario("Carlos")
    user.comentarios = ["bom", "excelente"]
    user.topicos = ["Café especial", "Dicas de preparo"]
    user.avaliacoes = [4.0, 5.0, 4.5]
    user.meses_ativo = 12

    user.set_estrategia_rankeamento(RankPorParticipacao())
    print("Rank por participação:", user.calcular_rank())

    user.set_estrategia_rankeamento(RankPorAvaliacoes())
    print("Rank por avaliações:", user.calcular_rank())

    user.set_estrategia_rankeamento(RankPorTempoNoSistema())
    print("Rank por tempo:", user.calcular_rank())
