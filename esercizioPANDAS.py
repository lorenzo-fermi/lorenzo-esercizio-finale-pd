import pandas as pd
import numpy as np

# Funzione per generare e esplorare i dati
def caricamento_Esplorazione():
    np.random.seed(42)  # Per riproducibilità

    n_clienti = 10  # Numero di clienti
    eta = np.random.randint(18, 80, size=n_clienti)
    durata_abbonamento = np.random.randint(1, 72, size=n_clienti)  # Durata abbonamento in mesi
    tariffa_mensile = np.random(20, 100, size=n_clienti)  # Tariffa mensile in euro
    dati_consumati = np.random(1, 100, size=n_clienti)  # Dati consumati in GB
    servizio_clienti_contatti = np.random.randint(0, 10, size=n_clienti)
    churn = np.random.choice([True, False], size=n_clienti, p=[0.8, 0.2])  # 80% non hanno lasciato, 20% hanno lasciato

    # Creazione del DataFrame
    data = {
        'ID_Clienti': np.arange(1, n_clienti + 1),
        'Età': eta,
        'Durata_Abbonamento': durata_abbonamento,
        'Tariffa_Mensile': tariffa_mensile,
        'Dati_Consumati': dati_consumati,
        'Servizio_Clienti_Contatti': servizio_clienti_contatti,
        'Churn': churn
    }

    df = pd.DataFrame(data)

    # Salvataggio del DataFrame in un file CSV
    df.to_csv('clienti.csv', index=False)

    # Visualizzazione del DataFrame
    print("ECCO LE INFO")
    df.info()
    print("\nECCO IL DESCRIBE")
    print(df.describe())
    print("\nECCO IL VALUECOUNTS")
    print(df.value_counts())

    return df

# Funzione per pulire i dati
def pulizia_dati(df):
    # Identificazione delle anomalie
    print("Valori anomali in 'Età':")
    print(df[df['Età'] < 0])

    print("\nValori anomali in 'Tariffa_Mensile':")
    print(df[df['Tariffa_Mensile'] > 100])

    # Correzione delle anomalie
    # Per 'Età' negativa, possiamo sostituirla con il valore assoluto o una media plausibile
    df.loc[df['Età'] < 0, 'Età'] = df['Età'].mean()

    # Per 'Tariffa_Mensile' troppo alta, possiamo impostarla a un valore massimo ragionevole (es. 100)
    df.loc[df['Tariffa_Mensile'] > 100, 'Tariffa_Mensile'] = 100

    # Visualizzazione del DataFrame corretto
    print("\nDataFrame corretto:")
    print(df)

# Generazione ed esplorazione del dataset
df = caricamento_Esplorazione()

# Pulizia dei dati
pulizia_dati(df)




