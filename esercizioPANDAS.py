import pandas as pd
import numpy as np

class Dati:
    def __init__(self, n_clienti=10):
        self.n_clienti = n_clienti
        
    
    def generate_data(self):
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

# Utilizzo delle classi per generare, esplorare e pulire i dati
data_gen = Dati()
df = data_gen.generate_data()
data_gen.esplorazione_dati(df)

data_cleaner = PuliziaDati(df)
data_cleaner.pulisci_dati()




