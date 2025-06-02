# Composite

## Introdução

Em sistemas de comunicação online, a organização hierárquica de conteúdo representa um dos maiores desafios arquiteturais. O padrão Composite emerge como uma estratégia estrutural que permite modelar e gerenciar eficientemente essas hierarquias complexas, tratando elementos atômicos e agregados através de uma abordagem unificada.

A essência do Composite reside na capacidade de abstrair as diferenças entre componentes individuais e coleções de componentes, permitindo que o código cliente interaja com ambos através de uma interface consistente. Esta uniformidade operacional elimina condicionais complexas e reduz significativamente o acoplamento entre módulos, características essenciais para sistemas escaláveis e maintíveis.

Sistemas de fóruns de discussão exemplificam perfeitamente cenários onde o Composite demonstra seu valor. Nestes ambientes, coexistem elementos fundamentalmente distintos: mensagens individuais que representam contribuições específicas dos usuários, e categorias temáticas que organizam e agrupam essas contribuições. A complexidade surge quando categorias podem conter não apenas mensagens, mas também subcategorias, formando uma rede hierárquica de profundidade variável.

Implementar funcionalidades como renderização completa de discussões, indexação de conteúdo ou análise de engajamento dos usuários exigiria, tradicionalmente, algoritmos que distinguem entre diferentes tipos de elementos e navegam pela estrutura de forma específica para cada tipo. Esta abordagem convencional gera código fragmentado, com lógica duplicada e alta dependência entre componentes.

## Metodologia

O desenvolvimento do modelo utilizando o padrão Composite iniciou-se com a análise dos requisitos de um sistema de fórum online. A necessidade de representar discussões hierárquicas, onde tópicos podem conter postagens e sub-tópicos, evidenciou a adequação do padrão para resolver problemas de estruturas uniformes e aninhadas.

O padrão Composite demonstrou-se ideal para esta aplicação por permitir tratamento uniforme de todos os elementos através de uma interface comum, suportando aninhamento ilimitado e facilitando extensibilidade futura. Os requisitos do projeto alinharam-se diretamente com as vantagens oferecidas pelo padrão.

O modelo foi desenvolvido seguindo uma abordagem iterativa, começando pela definição da interface abstrata `ForumComponent`. Esta interface incluiu o método essencial `exibir()` para apresentação de conteúdo, além de operações de composição como `add()`, `remove()` e `get_child()`. Embora estes métodos de composição não sejam aplicáveis a elementos folha, sua inclusão na interface mantém a uniformidade necessária para o padrão.

Para demonstrar a aplicação prática, foram implementados dois tipos fundamentais de componentes:

- **Elementos folha**, representados pela classe Postagem, que armazenam conteúdo textual e atuam como nós terminais da hierarquia.
- **Elementos compostos**, representados pela classe Topico, que gerenciam coleções de outros componentes e implementam operações de manipulação hierárquica.

Durante o processo de desenvolvimento, várias questões conceituais surgiram e foram resolvidas através de análise cuidadosa:

- **Sobre métodos de composição na interface**: Questionou-se inicialmente a necessidade de incluir métodos como `add()` e `remove()` na interface base, considerando que elementos folha não os utilizariam. Compreendeu-se, contudo, que estes métodos são fundamentais para manter a uniformidade da interface, objetivo central do padrão.

- **Sobre operações recursivas**: Discutiu-se a implementação de operações recursivas, como a exibição de conteúdo em tópicos com múltiplos níveis de aninhamento. A solução adotada permite navegação natural pela estrutura através dos métodos de composição.

Alternativas como separação de interfaces ou uso de herança múltipla foram consideradas, mas descartadas por comprometerem a simplicidade e uniformidade características do padrão. O modelo final seguiu rigorosamente os princípios clássicos do Composite, garantindo que elementos simples e compostos compartilhem a mesma interface.

## Modelagem

O uso do padrão Composite neste projeto cria uma estrutura onde uma única interface, chamada `ForumComponent`, define as regras que todos os elementos devem seguir — tanto os itens individuais quanto os que agrupam outros elementos. Isso torna muito mais fácil trabalhar com a hierarquia, como mostrado na figura 1.

<center>
<p style="text-align: center"><b>Figura 1:</b> Primeira versão do Diagrama de Classes do Padrão Composite</p>
<div align="center">
  <img src="assets/composite.png" alt="Diagrama UML do Composite Pattern" >
</div>
<font size="3"><p style="text-align: center"><b>Fonte:</b> <a href="https://github.com/DiegoCarlito">Diego Carlito</a> e <a href="https://github.com/Filipe-002">Filipe Carvalho</a>, 2025</p></font>
</center>

Os componentes principais da estrutura podem ser interpretados da seguinte forma:

- **ForumComponent**: Interface abstrata que define operações comuns para folhas e compostos, incluindo métodos de manipulação hierárquica.
- **Postagem**: Implementa ForumComponent representando elementos terminais (folhas) da hierarquia, sem capacidade de conter outros elementos.
- **Topico**: Implementa ForumComponent com capacidade de gerenciar filhos, delegando operações recursivamente para seus componentes.

## Histórico de Versões

| Versão | Data       | Alteração              | Responsável     | Revisor           | Data de revisão |
|--------|------------|------------------------|------------------|-------------------|------------------|
| `1.0`  | 01/06/2025 | Criação do documento com introdução, metodologia e modelagem | [Diego Carlito](https://github.com/DiegoCarlito) e [Filipe Carvalho](https://github.com/Filipe-002) |  |  |
