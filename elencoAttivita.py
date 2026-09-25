#Cosa devi fare

#Scrivi una funzione pulisci(testo) che restituisca (con return, non print) il testo senza spazi ai lati e con l'iniziale maiuscola su ogni parola.
#Crea una lista vuota attivita_pulite, poi con un ciclo for sulla lista grezza passa ogni elemento a pulisci() e aggiungi il risultato con .append().
#Stampa la lista pulita.
#Conta quante attività contengono la parola Collaudo, usando in dentro il ciclo, e stampa il risultato con una f-string.

attivita_grezze = ["  montaggio caldaia ", "COLLAUDO idraulico", "  verifica saldature","collaudo elettrico  ", "PULIZIA cantiere "]
attivita_pulite = []
def linea():
    print("-" * 25)

def pulisci(testo): #questa funzione pulisce il testo dagli spazi inizio/fine e mette la maiuscola iniziale
    return testo.strip().title()

linea()
print(attivita_grezze)
linea()

for a in attivita_grezze:
    attivita_pulite.append(pulisci(a))


print(attivita_pulite)

linea()

def controllo(lista,parola):
    c = 0
    for b in lista:
        if parola in b: 
            c += 1
    return (c)

n= (controllo(attivita_pulite,"Elettrico"))
print(f"le attività in corso sono: {n}")