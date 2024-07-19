import pandas as pd
import numpy as np

# Creazione di un DataFrame di esempio
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Età': [25, 30, 35, 40, 45],
    'Salario': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)

# Visualizzazione del DataFrame
print("DataFrame originale:")
print(df)

# Accesso a una colonna specifica
print("\nColonna 'Nome':")
print(df['Nome'])

# Accesso a una riga specifica usando il metodo iloc
print("\nRiga con indice 2:")
print(df.iloc[2])

# Filtrare il DataFrame per trovare persone con età superiore a 30
print("\nPersone con età superiore a 30:")
print(df[df['Età'] > 30])

# Aggiungere una nuova colonna che calcola il salario annuale
df['Salario_Annuale'] = df['Salario'] * 12
print("\nDataFrame con colonna 'Salario_Annuale' aggiunta:")
print(df)

# Calcolare la media dell'età e del salario
print("\nMedia dell'età:")
print(df['Età'].mean())
print("Media del salario:")
print(df['Salario'].mean())

# Creare un DataFrame con valori mancanti
df_missing = df.copy()
df_missing.loc[1, 'Salario'] = np.nan  # Inserire un valore mancante

# Raggruppare per 'Età' e calcolare la media del 'Salario' per ogni gruppo
print("\nMedia del salario per età:")
print(df.groupby('Età')['Salario'].mean())


# Ordinare il DataFrame per 'Salario' in ordine decrescente
print("\nDataFrame ordinato per 'Salario' in ordine decrescente:")
print(df.sort_values(by='Salario', ascending=False))
