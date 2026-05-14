# main.py

from regras_decisao import verificar_sistema
from analise_energetica import analisar_energia
from modelo_previsao import prever_energia

def executar_sistema():
    print("\n" + "="*60)
    print("SISTEMA INTELIGENTE DA COLÔNIA - AURORA SIGER")
    print("="*60)

    print("\n[PASSO 1] Verificando Regras de Decisão...")
    verificar_sistema()

    print("\n[PASSO 2] Analisando Uso de Energia...")
    analisar_energia()

    print("\n[PASSO 3] Executando Modelo de Previsão...")
    prever_energia(11)

    print("\n" + "="*60)
    print("PROCESSAMENTO CONCLUÍDO")
    print("="*60)

if __name__ == "__main__":
    executar_sistema()
