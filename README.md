# Decisões técnicas mais relevantes na construção do pipeline:
 - Foram tomadas decisões com foco em simplicidade, eficiência e clareza durante a implementação do pipeline de integração contínua, visto que estou adentrando ao mundo devops e, portanto, preferi implementar um pipeline simples, com funções simples para que assim eu conseguisse entender melhor cada etapa da implementação. 
 
 - Escolhi a linguagem Python devido à facilidade de configuração e integração simples com ferramentas de testes, como por exemplo o pytest. Seguindo os requisitos técnicos da sistematização, utilizei o GitHub Actions, eliminando então a necessidade de utilização de ferramentas externas, visto que o GitHub Actions é uma solução nativa do GitHub, e facilitando a automação diretamente no repositório.

- Sobre o Workflow, o mesmo foi configurado para execução automática em eventos de push e pull_request, garantindo que qualquer alteração no código seja validada imediatamente. Meu pipeline contempla etapas de checkout do código, configuração do ambiente, instalação de dependências e execução de testes automatizados.

- Em relação aos testes, criei cenários diferentes e utilizei as funções de testes para cobrir estes casos, incluindo casos com números negativos e zero.

# Impactos da ausência de testes automatizados:
- Sem os testes, erros podem passar despercebidos durante o desenvolvimento, sendo identificados em fases mais avançadas e até mesmo em produção, aumentando o custo de correção e comprometendo a qualidade do sistema. A falta de testes atrapalha a evolução do código, pois não há garantias de que novas alterações não irão quebrar funcionalidades já existentes. 

- No contexto de Integração Contínua, a falta dos testes compromete totalmente o pipeline, uma vez que não há validação automática do comportamento da aplicação.

# Possibilidades reais de evolução para Entrega Contínua:
- A evolução para Entrega Contínua se dá através da inclusão de etapas de build e deploy automatizado para ambientes de homologação ou produção, isso permitiria que a aplicação fosse disponibilizada para uso, de forma automática, após a aprovação nos testes.

- Também é possível integrar o pipeline com ferramentas de monitoramento, garantindo que eventuais falhas em produção sejam rapidamente identificadas.

- Uma outra possível evolução seria a utilização de estratégias de deploy como canary release ou blue-green, reduzindo riscos durante a entrega de novas versões.

# Riscos técnicos mitigados pela Integração Contínua:
- Adotar a Integração Contínua contribui diretamente para a mitigação de diversos riscos técnicos, como por exemplo, a redução de falhas de integração, já que o código é validado constantemente a cada alteração. Isso evita problemas em merges de código e garante maior estabilidade do sistema.

- Evita também a introdução de bugs em produção, uma vez que os testes automatizados atuam como uma barreira de validação antes que o código avance no pipeline. A CI também reduz a dependência de processos manuais, tornando o fluxo de desenvolvimento mais confiável, rápido e padronizado.