# modelo_previsao.py

from dados_colonia import dados_vento, dados_energia

def prever_energia(vento_futuro):
    # Calcula a relação entre vento e energia para cada ponto histórico
    # Demonstra o ajuste de uma "reta" (y = ax) usando a média das taxas
    taxas = [e / v for e, v in zip(dados_energia, dados_vento)]
    taxa_media = sum(taxas) / len(taxas)

    previsao = vento_futuro * taxa_media

    print(f"\n Base histórica: Vento {dados_vento} -> Energia {dados_energia}")
    print(f"- Previsão para vento de {vento_futuro} m/s: {previsao:.1f} unidades de energia")
