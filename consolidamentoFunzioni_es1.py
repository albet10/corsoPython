#Esercizio A — Codici componenti

#codici = [" v-101", "P-202 ", "v-103", " t-301 ", "P-204"]

#Scrivi una funzione normalizza(codice) che restituisca il codice senza spazi e tutto in maiuscolo. Poi costruisci con un ciclo e append la lista codici_puliti e stampala.

#Risultato atteso: ['V-101', 'P-202', 'V-103', 'T-301', 'P-204']

codici = [" v-101", "P-202 ", "v-103", " t-301 ", "P-204"]
lista_pulita = []

def linea():
	print ("--" * 25)
	
linea ()
print(codici)
linea()

def normalizza(a):
    return a.strip().upper()
    
for codice in codici: 
    lista_pulita.append(normalizza(codice))
    
print(lista_pulita)

#Esercizio B — Contare per tipo

#Sulla lista pulita dell'esercizio A, scrivi una funzione conta_tipo(lista, lettera) che restituisca quanti codici iniziano con quella lettera. Suggerimento: il primo carattere di una stringa si prende con l'indice [0].

#Risultato atteso: V → 2, P → 2, T → 1

def conta_tipo(lista,lettera):
    c = 0 
    for codice in lista:
        if codice[0] == lettera:
            c += 1 
    return c
print(f"Valvole: {conta_tipo(lista_pulita,"V")}")
print(f"Serbatoi: {conta_tipo(lista_pulita,"T")}")