import numpy as np
import pandas as pd

class AnalisiVendite:
    def __init__(self, n_giorni=30, seed=42):
        np.random.seed(seed)
        self.date_range = pd.date_range(start='2024-01-01', periods=n_giorni, freq='D')
        # Generazione di dati casuali per Vendite e Ore Lavorative
        self.vendite = np.random.randint(1000, 5000, size=n_giorni)
        self.ore_lavorative = np.random.randint(5, 12, size=n_giorni)
        # Creazione del DataFrame
        self.df = pd.DataFrame({
            'Data': self.date_range,
            'Vendite': self.vendite,
            'Ore Lavorative': self.ore_lavorative
        })
    
    def calcola_vendite_per_ora(self):
        # Calcola le vendite medie per ora lavorativa
        self.df['Vendite per Ora'] = self.df['Vendite'] / self.df['Ore Lavorative']
        return self.df[['Data', 'Vendite per Ora']]
    
    def giorni_efficienza(self):
        # Identifica il giorno con la massima e la minima efficienza
        max_efficienza = self.df.loc[self.df['Vendite per Ora'].idxmax()]
        min_efficienza = self.df.loc[self.df['Vendite per Ora'].idxmin()]
        return max_efficienza, min_efficienza
    
    def salva_dati(self):
        # Salva il DataFrame e i risultati in file CSV
        self.df.to_csv('performance_giornaliera.csv', index=False)
        vendite_per_ora = self.calcola_vendite_per_ora()
        vendite_per_ora.to_csv('vendite_per_ora.csv', index=False)
        max_efficienza, min_efficienza = self.giorni_efficienza()
        with open('efficienza_giorni.txt', 'w') as f:
            f.write(f"Giorno con massima efficienza:\n{max_efficienza}\n")
            f.write(f"Giorno con minima efficienza:\n{min_efficienza}\n")

# Creazione dell'oggetto e utilizzo delle funzionalità
analisi = AnalisiVendite()

# Calcolo e stampa delle vendite per ora lavorativa
vendite_per_ora = analisi.calcola_vendite_per_ora()
print("Vendite per ora lavorativa:")
print(vendite_per_ora)

# Identificazione dei giorni con la massima e minima efficienza
max_efficienza, min_efficienza = analisi.giorni_efficienza()
print(f"Giorno con massima efficienza:\n{max_efficienza}")
print(f"Giorno con minima efficienza:\n{min_efficienza}")

# Salvataggio dei dati e risultati su file
analisi.salva_dati()
