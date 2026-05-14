# regras_decisao.py
from dados_colonia import energia_atual, consumo_atual, sistemas_colonia

def verificar_sistema():
    print(f"Status Atual - Energia: {energia_atual} | Consumo: {consumo_atual}")
    
    if energia_atual < 50:
        if consumo_atual > 60:
            print("\n ALERTA CRÍTICO: Ativar modo economia extrema.")
            print("- Ação: Desligando sistemas não essenciais...")

            for sistema, subsistemas in sistemas_colonia.items():
                if sistema != "suporte_vida":
                    print(f"\n  > Sistema '{sistema}' operando em modo reduzido.")
                else:
                    print(f"\n  > Sistema '{sistema}' MANTIDO (Prioridade Máxima).")
        else:
            print("\n ALERTA: Energia baixa. Reduzir consumo de sistemas secundários.")
    
    else:
        print("\n Sistemas funcionando normalmente. Todos os subsistemas operacionais.")