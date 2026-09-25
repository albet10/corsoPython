
def linea():
    print("-" * 25)
linea()

numero = int(input ("scrivi un numero "))
if (numero % 2) == 0:
	print(f"il numero {numero} è pari")
	
	print(f"i numeri pari fino al numero {numero} sono")
	for i in range(0,numero,2):
		print(i)
else:
	print(f"il numero {numero} non è pari")

linea()

numeri = [10,20,30,40,50,60]
lungh = len(numeri)
#print (lungh)
print(f"il numero di componenti della lista 'NUMERI' è {lungh}")
if (lungh % 2) ==0 :
    for i in range(0,lungh+1,2):
        print (i)
else:
    print(f"il numero di componenti della lista 'NUMERI' è {lungh} ed è dispari")

linea()

lista = [10,22,31,40,50]
print (f"I seguenti numeri della lista {lista} sono pari: ")
for n in lista:
    if (n%2)==0:
        print(n)

linea ()

numeri = [10,20,30,40,53,61]
print (numeri)
def conta_pari(numeri):
    n=0
    for i in numeri:
        if (i%2)==0:
            n += 1
    return n
risultato = conta_pari(numeri)
print(f"I numeri pari sono: {risultato}")

nome = input("Inserire il tuo nome: ")
cognome = input ("Inserire il tuo cognome: ")
print ("nome completo: " + nome + " " + cognome)
print(f"Il nome completo è: {nome} {cognome}")

linea()

frase = "Ingegneria Industriale"
print(frase[0])
print(frase[0:5])
print(frase[0],frase[5])
print(frase[:5])
print(frase[5:])

linea()

testo = " cIao mOndo "
print (testo.upper())
print (testo.lower())
print (testo.strip())
print (testo.capitalize())
print (testo.title())

sentence = "Il cane è nero"
nuova_sentence = sentence.replace("cane", "gatto")
print (nuova_sentence)

stringa ="   MARIO rossi  "
nuova_stringa = stringa.strip().title()
#nuova_nuova_stringa = nuova_stringa.title()
print (nuova_stringa)


frase ="calcio, pere, macchina"
lista = frase.split(",")
print(lista)
print(frase)

phrase = "Progetto - Fase - Attività"
list = phrase.split("-")
print(list)
incollata = "/".join(list)
print(incollata)