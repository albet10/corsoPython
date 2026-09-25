# analisi delle temperature di collaudo
# le letture vengono analizzate e se superano la soglia impostata restituisce un allarme
# conta_sopra_soglia(lista, soglia) che restituisce (con return) quante letture superano la soglia

temp_soglia = int(input("Inserire la temperatura di soglia: "))
print(f"La temperatura di soglia impostata è di: {temp_soglia} °C")
def linea():
    print("-" * 25)
linea()

temperature_registrate = [82, 95, 101, 78, 110, 88, 105, 76]

def conta_sopra_soglia(x,y):
    z = 0
    for t in x:
	    if t > y:
		    z += 1
    return z

def media (x):
    return sum(x) / len(x)

n = conta_sopra_soglia(temperature_registrate,temp_soglia)
m = media(temperature_registrate)

print ("le letture sono: ", len(temperature_registrate))
print (f"la temperatura media è: {m}")
print (f"le letture oltre la soglia sono {n}")

linea()

if (n>(len(temperature_registrate)/2)):
    print("troppe registrazioni oltre la soglia")
else:
    print("tutto ok")
    

linea()
    
pressioni = [12.5, 15.0, 9.8, 16.2, 14.1, 11.0]
pressioni_2 = [12.3,14,11,15,13,239]


#stampa una nuova lista con solo i valori oltre la soglia


pressioni = [12.5, 15.0, 9.8, 16.2, 14.1, 11.0]

def sopra_soglia(lista, soglia=14):
    risultato = []
    for p in lista:
        if p > soglia:
            risultato.append(p)
    return risultato

r1 = sopra_soglia(pressioni_2)
print(f"Soglia 14: {r1} ({len(r1)} valori)")

r2 = sopra_soglia(pressioni_2, soglia=12)
print(f"Soglia 12: {r2} ({len(r2)} valori)")


linea()

#Esercizio D — Esiti di collaudo
#righe = ["V-101;OK", "P-202;KO", "V-103;OK", "T-301;KO", "P-204;OK"]

#Scrivi una funzione codici_ko(righe) che per ogni riga separi codice ed esito con split, e restituisca la lista dei soli codici con esito KO. Poi stampali uniti con join.

#Risultato atteso: ['P-202', 'T-301'] e poi P-202 / T-301

righe = ["V-101;OK", "P-202;KO", "V-103;OK", "T-301;KO", "P-204;OK"]

def codice_ko(lista)
    cod_pulito = []
    if t in lista:
        