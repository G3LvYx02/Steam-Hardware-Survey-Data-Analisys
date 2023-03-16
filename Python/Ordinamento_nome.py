import pandas as pd

# Leggere il file CSV dato il percorso; senza percorso il file deve essere nella stessa directory
df = pd.read_csv("gpu.csv")

# Ordiniamo i dati per Nome
df_sorted = df.sort_values(by=['GPU NAME', '% CHANGE'])

# Creare un nuovo file CSV e mettere il nuovo nome del file CSV;  senza percorso il
# file deve essere nella stessa directory
df_sorted.to_csv('gpu_name.csv', index=False)

