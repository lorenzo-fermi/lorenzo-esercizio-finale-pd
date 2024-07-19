import pandas as pd
import numpy as np

class RistoranteDaSofi:
    def __init__(self, n_giorni=30, n_filiali=5, seed=42):
        self.n_giorni = n_giorni
        self.n_filiali = n_filiali
        np.random.seed(seed)
        
        # Generazione delle date e delle filiali
        self.date_range = pd.date_range(start='2024-01-01', periods=n_giorni, freq='D')
        self.filiali = [f'Filiale_{i+1}' for i in range(n_filiali)]
        
        # Creazione del DataFrame con dati casuali
        self.df = pd.DataFrame({
            'Data': np.tile(self.date_range, self.n_filiali),
            'Filiale': np.repeat(self.filiali, self.n_giorni),
            'Vendite': np.random.randint(1000, 5000, size=self.n_giorni * self.n_filiali)
        })
    
    def calcola_media_vendite(self):
        # Calcolo della media delle vendite per "Data" e "Filiale"
        return self.df.groupby(['Data', 'Filiale'])['Vendite'].mean().reset_index()
    
    def filiale_con_maggiori_vendite(self):
        # Trovare la filiale con le vendite totali più alte
        vendite_totali = self.df.groupby('Filiale')['Vendite'].sum()
        filiale_top = vendite_totali.idxmax()
        return filiale_top, vendite_totali.max()
    
    def salva_dati_e_risultati(self):
        # Salvare i dati originali e le vendite medie in file CSV
        self.df.to_csv('vendite_giornaliere.csv', index=False)
        self.calcola_media_vendite().to_csv('vendite_medie_per_filiale.csv', index=False)
        
        filiale_top, vendite_top = self.filiale_con_maggiori_vendite()
        with open('filiale_top.txt', 'w') as f:
            f.write(f'Filiale con maggiori vendite: {filiale_top}\n')
            f.write(f'Vendite totali: {vendite_top}')

def menu():
    ristorante = RistoranteDaSofi()
    
    while True:
        print("\n--- Menu ---")
        print("1. Calcola e stampa la media delle vendite giornaliere per filiale")
        print("2. Determina e stampa la filiale con le vendite più alte")
        print("3. Salva dati e risultati su file")
        print("4. Esci")
        
        scelta = input("Scegli un'opzione (1-4): ")
        
        if scelta == '1':
            # Calcolo e stampa della media delle vendite giornaliere per filiale
            vendite_medie = ristorante.calcola_media_vendite()
            print("\nVendite medie giornaliere per filiale:")
            print(vendite_medie)
        
        elif scelta == '2':
            # Determinazione e stampa della filiale con le vendite più alte
            filiale_top, vendite_top = ristorante.filiale_con_maggiori_vendite()
            print(f"\nFiliale con maggiori vendite: {filiale_top}")
            print(f"Vendite totali: {vendite_top}")
        
        elif scelta == '3':
            # Salvataggio dei dati e risultati su file CSV
            ristorante.salva_dati_e_risultati()
            print("\nDati e risultati sono stati salvati.")
        
        elif scelta == '4':
            # Uscita dal programma
            print("Uscita dal programma.")
            break
        
        else:
            print("Opzione non valida, per favore scegli un'opzione tra 1 e 4.")

# Esecuzione del menu
menu()
