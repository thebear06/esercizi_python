tupla_meteo = (("Bergamo", [("gennaio", 6),("febbraio", 10),("marzo", 12),("aprile", 14),("maggio", 16),("giugno", 22),("luglio", 30),("agosto", 35),("settempre", 20),("ottobre", 16),("novembre", 10), ("dicembre", 5)]),
              ("Brescia", [("gennaio", 4),("febbraio", 8),("marzo", 10),("aprile", 12),("maggio", 14),("giugno", 20),("luglio", 25),("agosto", 30),("settempre", 15),("ottobre", 14),("novembre", 8), ("dicembre", 3)]),
              ("Como", [("gennaio", 8),("febbraio", 12),("marzo", 14),("aprile", 16),("maggio", 18),("giugno", 24),("luglio", 35),("agosto", 37),("settempre", 22),("ottobre", 18),("novembre", 12), ("dicembre", 8)]),
              ("Cremona", [("gennaio", 7),("febbraio", 9),("marzo", 13),("aprile", 15),("maggio", 17),("giugno", 23),("luglio", 34),("agosto", 38),("settempre", 24),("ottobre", 15),("novembre", 11), ("dicembre", 2)])
              )

def calcolo(citta):

    lista = []

    #calcolo media


    #calcolo minimo
    min = 0
    
    for capoluogo, mesi_valori in tupla_meteo:
        
        if(capoluogo == citta):
            print(capoluogo)
            
            print(mesi_valori)
            somma = 0
            for mese, valore in mesi_valori:
                min = valore
   
citta = input("inserisci la citta da controllare: ")
calcolo(citta)
