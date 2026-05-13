# Plano de Estruturação - FASE_3_CC

Este documento descreve a estrutura de pastas e arquivos para o sistema integrado da colônia inteligente, atendendo aos requisitos da Fase 3.

## Estrutura de Diretórios Proposta

```text
FASE_3_CC/
│
├── main.py                 # Arquivo principal que integra todos os módulos e executa o sistema.
├── dados_colonia.py        # Organização dos dados (listas, dicionários e hierarquia).
├── regras_decisao.py       # Lógica do sistema e regras de decisão automática.
├── modelo_previsao.py      # Implementação da regressão simples para estimativas.
├── analise_energetica.py   # Comparação de geração vs consumo e sugestões.
└── README.md               # Documentação do projeto (explicação, entradas e saídas).
```

## Descrição dos Módulos

### 1. `main.py`
O coração do sistema. Irá importar as funções dos outros arquivos e realizar a orquestração:
- Recebe inputs do usuário ou simula dados.
- Chama as funções de processamento.
- Exibe os resultados e alertas finais.

### 2. `dados_colonia.py`
Responsável por estruturar a "inteligência" da colônia em termos de informação:
- Armazenamento de variáveis de energia, consumo e clima.
- Implementação da navegação hierárquica entre subsistemas (Energético, Suporte à Vida, etc.).

### 3. `regras_decisao.py`
Contém as funções que aplicam as regras de negócio:
- Verificação de níveis críticos de energia.
- Combinação de condições (Energia Baixa + Consumo Alto).
- Priorização de sistemas vitais.

### 4. `modelo_previsao.py`
Implementa a lógica matemática da regressão linear simples sem bibliotecas externas:
- Função para calcular a "reta" de ajuste (coeficientes).
- Função para prever valores futuros (ex: Vento -> Energia).

### 5. `analise_energetica.py`
Focado na saúde energética da colônia:
- Compara geração atual vs consumo.
- Gera recomendações de armazenamento ou corte de gastos.
