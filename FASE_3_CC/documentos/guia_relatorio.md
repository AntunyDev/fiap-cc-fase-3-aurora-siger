# Guia para o Relatório PDF - FASE_3_CC

Este guia contém os pontos essenciais que devem ser incluídos no seu relatório final para garantir a pontuação máxima nos critérios de avaliação.

## 1. Estruturação de Dados
Explique como os dados foram organizados:
- **Hierarquia**: Usamos dicionários aninhados em `dados_colonia.py` para separar sistemas (Energético, Suporte à Vida).
- **Eficiência**: O uso de chaves e valores permite acesso rápido às informações de cada subsistema.

## 2. Lógica de Decisão
Descreva as regras implementadas em `regras_decisao.py`:
- **Regras Básicas**: Verificação de limites de energia (ex: < 50%).
- **Condições Combinadas**: Como o sistema reage quando a energia está baixa e o consumo está alto simultaneamente.
- **Priorização**: Em casos críticos, o sistema prioriza o Suporte à Vida, demonstrando inteligência operacional.

## 3. Modelagem e Previsão
Explique o modelo matemático em `modelo_previsao.py`:
- **Regressão Linear Simples**: O sistema ajusta uma reta ($y = mx + b$) aos dados históricos de vento e geração.
- **Predição**: Como o sistema usa essa relação para estimar a geração futura, permitindo que a colônia saia de um estado reativo para um preditivo.

## 4. Implementação em Python
Destaque os pontos técnicos:
- Código modularizado em funções e arquivos separados.
- Ausência de bibliotecas externas (foco em lógica pura).
- Separação clara entre Lógica, Dados e Decisão (conforme pedido no entregável).

## 5. Melhoria no Uso de Energia
Conclua explicando o impacto:
- "O sistema ajuda a colônia a antecipar quedas de geração e ajustar o consumo antes que as reservas cheguem a níveis perigosos, garantindo a segurança dos colonos."

---
**Dica**: Não esqueça de incluir o link do seu repositório GitHub público no final do documento!
