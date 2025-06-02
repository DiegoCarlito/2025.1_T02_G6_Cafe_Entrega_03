# Command

## Introdução

O padrão comportamental Command representa uma abordagem sofisticada para transformar solicitações em objetos independentes, proporcionando flexibilidade excepcional no controle e manipulação de operações. Através desta estratégia, sistemas podem parametrizar objetos com diferentes requisições, implementar filas de processamento e estabelecer mecanismos robustos de reversibilidade operacional.

A característica distintiva do Command reside na capacidade de desacoplar completamente o emissor de uma requisição do objeto que efetivamente a processa. Esta separação permite que operações sejam tratadas como entidades de primeira classe, possibilitando armazenamento, transmissão e manipulação como qualquer outro objeto do sistema.

Em contextos de sistemas de moderação online, especialmente plataformas que demandam controle rigoroso sobre conteúdo e comportamento de usuários, o padrão Command demonstra valor significativo. Considere cenários onde moderadores precisam executar múltiplas ações de moderação - ocultar postagens, bloquear usuários, remover comentários, destacar conteúdo - onde cada ação deve ser rastreável e potencialmente reversível para garantir flexibilidade operacional.

Implementações tradicionais para funcionalidades de moderação frequentemente resultam em acoplamento direto entre interfaces administrativas e lógica de moderação, criando sistemas rígidos onde modificações em políticas de moderação exigem alterações extensivas em múltiplas camadas. A ausência de mecanismos de desfazimento complica ainda mais a experiência dos moderadores e a manutenção do sistema.

O padrão Command endereça essas limitações através da introdução de uma abstração que encapsula cada operação como um objeto independente, estabelecendo contratos claros entre solicitantes e executores, e facilitando a implementação de funcionalidades avançadas como histórico de operações e processamento em lote.

## Metodologia

O desenvolvimento da solução utilizando o padrão Command iniciou-se com a análise detalhada dos requisitos de um sistema de moderação de conteúdo online. A necessidade de implementar funcionalidades de desfazer/refazer ações de moderação, combinada com a flexibilidade para processar diferentes tipos de operações moderativas, direcionou a escolha do padrão como estratégia arquitetural principal.

O padrão Command mostrou-se ideal para esta aplicação por oferecer encapsulamento completo de ações de moderação, suporte nativo à reversibilidade de operações e desacoplamento efetivo entre camadas de interface administrativa e processamento de moderação. Os requisitos funcionais do projeto alinharam-se naturalmente com as capacidades oferecidas pelo padrão.

A implementação seguiu uma abordagem incremental, iniciando pela definição das interfaces Command que estabelecem o contrato básico para todos os comandos do sistema de moderação. Estas interfaces incluíram métodos fundamentais como executar() para execução de ações moderativas e desfazer() para reversibilidade, garantindo consistência comportamental entre todas as implementações.

Durante o processo de desenvolvimento, foram identificados e resolvidos diversos desafios conceituais:

- **Gerenciamento de estado de moderação**: A necessidade de preservar estados anteriores para possibilitar operações de desfazer exigiu estratégias cuidadosas de captura e armazenamento de dados de moderação.
- **Granularidade de comandos**: Definir o nível apropriado de atomicidade para cada ação de moderação, balanceando flexibilidade operacional com simplicidade de implementação.
- **Distinção entre ações reversíveis e irreversíveis**: Separar adequadamente ações que podem ser desfeitas (como ocultar postagens) daquelas que são permanentes (como exclusão definitiva).

Para demonstrar a aplicabilidade prática, foram implementados comandos específicos para diferentes aspectos da moderação de conteúdo:

- **Comandos de moderação de conteúdo**: Encapsulam ações como ocultação e destaque de postagens, remoção de comentários.
- **Comandos de moderação de usuários**: Gerenciam bloqueio e desbloqueio de usuários do sistema.

## Modelagem

A arquitetura desenvolvida para implementar o padrão Command no sistema de moderação está estruturada em componentes bem definidos que colaboram para garantir flexibilidade e controle operacional. O diagrama de classes apresentado na figura 1 ilustra as relações entre estes componentes e suas responsabilidades específicas.

### Descrição dos Componentes do Diagrama UML

O diagrama UML apresenta uma implementação sofisticada do padrão Command que diferencia comandos reversíveis dos irreversíveis, característica fundamental para sistemas de moderação onde algumas operações devem ser permanentes.

**ControladorModeracao (Invoker)**: Localizado no topo da hierarquia, este componente atua como o ponto central de controle do sistema. Mantém duas listas essenciais - `historico` para comandos executados e `desfeitos` para comandos que foram revertidos. Seus métodos `executar_comando()`, `desfazer()` e `refazer()` implementam a lógica de gerenciamento de operações, garantindo que apenas comandos reversíveis sejam incluídos no histórico de controle.

**Hierarquia de Interfaces**: O diagrama apresenta duas interfaces distintas - `ComandoModeracao` e `ComandoIrreversivel`. A primeira define o contrato para operações que podem ser desfeitas, incluindo os métodos `executar()` e `desfazer()`. A segunda interface é mais restritiva, oferecendo apenas `executar()`, refletindo a natureza permanente dessas operações.

**Comandos Concretos Reversíveis**: As classes `OcultarPostagemCommand`, `BloquearUsuarioCommand`, `DestacarPostagemCommand` e `RemoverComentarioCommand` implementam a interface `ComandoModeracao`. Cada uma encapsula uma operação específica de moderação mantendo referências ao objeto `Moderador` e aos dados necessários (postagem, usuário, comentário). A implementação de ambos os métodos `executar()` e `desfazer()` permite que essas operações sejam completamente reversíveis.

**Comando Irreversível**: A classe `ExcluirPostagemCommand` implementa `ComandoIrreversivel`, representando operações que não podem ser desfeitas. Esta separação arquitetural garante que operações críticas como exclusão definitiva sejam tratadas adequadamente pelo sistema.

**Moderador (Receiver)**: Posicionado na base do diagrama, o `Moderador` concentra toda a lógica de negócio de moderação. Seus métodos correspondem às operações básicas do domínio (ocultar, excluir, bloquear usuários, etc.) e são invocados pelos comandos concretos. Esta centralização facilita manutenção e garante consistência operacional.

As setas tracejadas no diagrama indicam relações de dependência, mostrando como os comandos concretos dependem tanto das interfaces quanto do objeto `Moderador` para sua funcionalidade. A relação sólida entre `ControladorModeracao` e as interfaces demonstra o polimorfismo utilizado para tratar diferentes tipos de comandos uniformemente.

Esta modelagem exemplifica os princípios fundamentais do padrão Command: encapsulamento de operações como objetos, desacoplamento entre invocador e receptor, e suporte robusto à reversibilidade operacional.

<center>
<p style="text-align: center"><b>Figura 1:</b> Primeira versão do Diagrama de Classes do Padrão Command</p>
<div align="center">
  <img src="assets/command.png" alt="Diagrama UML do Command Pattern" >
</div>
<font size="3"><p style="text-align: center"><b>Fonte:</b> <a href="https://github.com/DiegoCarlito">Diego Carlito</a> e <a href="https://github.com/PedroHhenriq">Pedro Henrique</a>, 2025.</p></font>
</center>

## Histórico de Versão

| Versão | Data       | Alteração              | Responsável     | Revisor           | Data de revisão |
|--------|------------|------------------------|------------------|-------------------|------------------|
| `1.0`  |01/06/2025| Criação do documento com introdução, metodologia e modelagem | [Diego Carlito](https://github.com/DiegoCarlito) e [Pedro Henrique](https://github.com/PedroHhenriq) |  |  |