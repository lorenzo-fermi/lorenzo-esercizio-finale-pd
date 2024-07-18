import pandas as pd
import numpy as np

class Dati:
    def __init__(self, n_clienti=10):
        self.n_clienti = n_clienti
        
    def genera_dati(self):
        np.random.seed(42)  # Per riproducibilità
        eta = np.random.randint(18, 80, size=self.n_clienti)
        durata_abbonamento = np.random.randint(1, 72, size=self.n_clienti)  # Durata abbonamento in mesi
        tariffa_mensile = np.random.randint(20, 100, size=self.n_clienti)  # Tariffa mensile in euro, ora intera
        dati_consumati = np.random.randint(1, 100, size=self.n_clienti)  # Dati consumati in GB, ora interi
        servizio_clienti_contatti = np.random.randint(0, 10, size=self.n_clienti)
        churn = np.random.choice([True, False], size=self.n_clienti, p=[0.8, 0.2])  # 80% non hanno lasciato, 20% hanno lasciato

        data = {
            'ID_Clienti': np.arange(1, self.n_clienti + 1),
            'Età': eta,
            'Durata_Abbonamento': durata_abbonamento,
            'Tariffa_Mensile': tariffa_mensile,
            'Dati_Consumati': dati_consumati,
            'Servizio_Clienti_Contatti': servizio_clienti_contatti,
            'Churn': churn
        }

        df = pd.DataFrame(data)
        df.to_csv('clienti.csv', index=False)
        
        return df
    
    def esplorazione_dati(self, df):
        print("ECCO LE INFO")
        df.info()
        print("\nECCO IL DESCRIBE")
        print(df.describe())
        print("\nECCO IL VALUECOUNTS")
        print(df.value_counts())

    def calcola_costo_per_GB(self, df):
        # Aggiunta della colonna Costo_per_GB
        df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']
        
        print("\nDataFrame con Costo_per_GB:")
        print(df)
        return df

class PuliziaDati:
    def __init__(self, df):
        self.df = df
    
    def pulisci_dati(self):
        print("Valori anomali in 'Età':")
        print(self.df[self.df['Età'] < 0])

        print("\nValori anomali in 'Tariffa_Mensile':")
        print(self.df[self.df['Tariffa_Mensile'] > 100])

        self.df.loc[self.df['Età'] < 0, 'Età'] = self.df['Età'].mean()
        self.df.loc[self.df['Tariffa_Mensile'] > 100, 'Tariffa_Mensile'] = 100

        print("\nDataFrame corretto:")
        print(self.df)
        return self.df
    
    def esp_relazione(self, df):
        # Raggruppamento per le colonne specificate
        gruppi = df.groupby(['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Churn']).size().reset_index(name='Count')
        
        # Calcolo della correlazione tra le colonne numeriche
        correlazione = df[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati']].corr()
        
        print("\nRaggruppamento per Età, Durata_Abbonamento, Tariffa_Mensile e Churn con correlazione:")
        print(gruppi)
        print("\nCorrelazione tra le colonne numeriche:")
        print(correlazione)


# Utilizzo delle classi per generare, esplorare e pulire i dati
dati = Dati()
df = dati.genera_dati()
dati.esplorazione_dati(df)

# Calcolo del costo per GB
df = dati.calcola_costo_per_GB(df)

# Pulizia dei dati
puliziadati = PuliziaDati(df)
df_pulito = puliziadati.pulisci_dati()

# Esplorazione dei dati raggruppati con correlazione
puliziadati.esp_relazione(df_pulito)



