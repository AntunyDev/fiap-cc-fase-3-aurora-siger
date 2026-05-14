# analise_energetica.py

from dados_colonia import geracao_energia, consumo_atual

def analisar_energia():

    if consumo_atual > geracao_energia:
        print("\n ALERTA: consumo maior que geração")

    elif geracao_energia > consumo_atual:
        print("\n SUGESTÂO: armazenar energia excedente")

    else: 
        print("\n Energia equilibrada")

