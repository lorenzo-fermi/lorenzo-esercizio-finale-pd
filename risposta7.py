import numpy as np
import pandas as pd

class TemperaturaNapoletana:
    def __init__(self, n_ore=24, seed=42):
       
        self.n_ore = n_ore
        np.random.seed(seed)
        self.temperature = 20 + np.random.randn(n_ore)  # Genera temperature casuali attorno ai 20 gradi
        self.aumento_costante = 0.2
        self.df = pd.DataFrame({'Temperature': self.temperature})  # Crea un DataFrame con le temperature
    
    def stampa_temperature(self):
       
        print("Temperature registrate nelle ultime 24 ore:")
        print(self.df)  # Stampa il DataFrame con le temperature
    
    def calcola_media(self):
        
        return self.df['Temperature'].mean()  # Calcola e restituisce la temperatura media
    
    def calcola_massima(self):
       
        
        return self.df['Temperature'].max()  # Calcola e restituisce la temperatura massima
    
    def calcola_minima(self):
       
        return self.df['Temperature'].min()  # Calcola e restituisce la temperatura minima
    
    def previsioni_prossime_ore(self, n_ore_previste=4):
       
        ultime_temperatura = self.df['Temperature'].iloc[-1]  # Ultima temperatura registrata
        previsioni = ultime_temperatura + np.arange(1, n_ore_previste + 1) * self.aumento_costante  # Calcola le previsioni
        return pd.Series(previsioni, name='Previsioni')  # Restituisce le previsioni come Serie pandas
    
    def verifica_temperatura(self, temperature):
      
        if np.any(temperature > 40):  # Controlla se c'è almeno una temperatura superiore a 40 gradi
            print("\nsi jett o sang")  # Stampa il messaggio di avviso
            for temp in temperature:  # Itera su tutte le temperature
                if temp > 40:  # Se la temperatura supera i 40 gradi
                    print(f"Temperatura prevista: {temp} gradi - si jett o sang")  # Stampa il messaggio di avviso per ciascuna temperatura che supera i 40 gradi


# Creazione dell'oggetto
temp_nap = TemperaturaNapoletana()

# Stampa delle temperature registrate
temp_nap.stampa_temperature()

# Calcolo e stampa della temperatura media
media_temperatura = temp_nap.calcola_media()
print("\nTemperatura media:", media_temperatura)

# Calcolo e stampa della temperatura massima
max_temperatura = temp_nap.calcola_massima()
print("Temperatura massima:", max_temperatura)

# Calcolo e stampa della temperatura minima
min_temperatura = temp_nap.calcola_minima()
print("Temperatura minima:", min_temperatura)

# Previsioni delle prossime 4 ore
prossime_temperature = temp_nap.previsioni_prossime_ore()
print("\nTemperature previste per le prossime 4 ore:")
print(prossime_temperature)

# Verifica e stampa del messaggio se la temperatura supera i 40 gradi
temp_nap.verifica_temperatura(prossime_temperature)
