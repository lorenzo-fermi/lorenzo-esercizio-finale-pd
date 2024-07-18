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
        churn = np.random.choice(['No', 'Sì'], size=self.n_clienti, p=[0.8, 0.2])  # 80% non hanno lasciato, 20% hanno lasciato

        # Creazione del DataFrame con i dati generati
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
        df.to_csv('clienti.csv', index=False)  # Salvataggio su file CSV
        
        return df
    
    def esplorazione_dati(self, df):
        # Funzione per esplorare i dati, mostrando informazioni principali
        print("ECCO LE INFO")
        df.info()
        print("\nECCO IL DESCRIBE")
        print(df.describe())
        print("\nECCO IL VALUECOUNTS")
        print(df.value_counts())

    def calcola_costo_per_GB(self, df):
        # Funzione per calcolare il costo per GB e aggiungerlo al DataFrame
        df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']
        
        print("\nDataFrame con Costo_per_GB:")
        print(df)
        return df

class PuliziaDati:
    def __init__(self, df):
        self.df = df
    
    def pulisci_dati(self):
        # Funzione per pulire i dati, gestendo valori anomali
        print("Valori anomali in 'Età':")
        print(self.df[self.df['Età'] < 0])

        print("\nValori anomali in 'Tariffa_Mensile':")
        print(self.df[self.df['Tariffa_Mensile'] > 100])

        # Sostituzione dei valori anomali con valori validi
        self.df.loc[self.df['Età'] < 0, 'Età'] = self.df['Età'].mean()
        self.df.loc[self.df['Tariffa_Mensile'] > 100, 'Tariffa_Mensile'] = 100

        print("\nDataFrame corretto:")
        print(self.df)
        return self.df
    
    def esp_relazione(self):
        # Funzione per calcolare la relazione tra variabili
        df_relazione = self.df.groupby(['Età','Durata_Abbonamento','Tariffa_Mensile','Churn']).corr()
        print("\nRelazione tra variabili:")
        print(df_relazione)

# Funzione per normalizzare le colonne numeriche usando numpy
def normalizza_colonne(df):
    # Selezioniamo solo le colonne numeriche da normalizzare
    colonne_da_normalizzare = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti']

    # Normalizziamo le colonne numeriche
    df[colonne_da_normalizzare] = (df[colonne_da_normalizzare] - df[colonne_da_normalizzare].min()) / (df[colonne_da_normalizzare].max() - df[colonne_da_normalizzare].min())

    return df

# Funzione per stampare il menu e gestire le scelte dell'utente
def stampa_menu():
    print("\n*** MENU ***")
    print("1. Genera dati")
    print("2. Esplora dati")
    print("3. Calcola costo per GB")
    print("4. Pulisci dati")
    print("5. Calcola relazione tra variabili")
    print("6. Esci")

    scelta = input("\nSeleziona un'opzione: ")
    return scelta

# Utilizzo delle classi per gestire i dati
dati = Dati()
puliziadati = None
df = None

while True:
    scelta = stampa_menu()

    if scelta == '1':
        df = dati.genera_dati()  # Genera i dati e li assegna alla variabile df
    elif scelta == '2':
        if df is not None:
            dati.esplorazione_dati(df)  # Esplora i dati se sono stati generati
        else:
            print("Devi prima generare i dati (opzione 1)")
    elif scelta == '3':
        if df is not None:
            df = dati.calcola_costo_per_GB(df)  # Calcola il costo per GB se ci sono dati
        else:
            print("Devi prima generare i dati (opzione 1)")
    elif scelta == '4':
        if df is not None:
            puliziadati = PuliziaDati(df)
            df = puliziadati.pulisci_dati()  # Pulisce i dati se sono stati generati
        else:
            print("Devi prima generare i dati (opzione 1)")
    elif scelta == '5':
        if df is not None:
            if puliziadati is not None:
                puliziadati.esp_relazione()  # Calcola la relazione tra variabili se i dati sono stati puliti
            else:
                print("Devi prima pulire i dati (opzione 4)")
        else:
            print("Devi prima generare i dati (opzione 1)")
    elif scelta == '6':
        print("Programma terminato.")
        break
    else:
        print("Scelta non valida. Riprova.")


