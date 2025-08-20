import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Ler arquivo original
df = pd.read_csv("file.csv")

# Intervalo de datas
start_date = datetime(2024, 8, 1)
end_date = datetime(2025, 7, 31)

# Função para gerar data aleatória no intervalo
def random_date(start, end):
    return start + timedelta(days=np.random.randint(0, (end - start).days + 1))

df['propensity_date'] = [random_date(start_date, end_date).strftime('%Y-%m-%d') for _ in range(len(df))]

# Criar variedade nos scores
scores = []
for _ in range(len(df)):
    p = np.random.rand()
    if p < 0.4:   # 40% dos casos -> extremos
        scores.append(np.random.beta(0.5, 0.5))
    elif p < 0.7: # 30% dos casos -> médios
        scores.append(np.random.normal(0.5, 0.15))
    else:         # 30% dos casos -> uniformemente distribuídos
        scores.append(np.random.rand())

# Garantir que fiquem dentro de [0,1]
df['propensity_score'] = np.clip(scores, 0, 1)

# Salvar
df.to_csv("seu_arquivo_modificado.csv", index=False)

print("✅ Dados mais variados gerados!")
