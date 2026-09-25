# Corso di Python — Riepilogo del percorso

Percorso di apprendimento Python da zero, con lezioni progressive, schede PDF
riassuntive stampabili ed esercizi pratici corretti passo per passo.

## Lezioni completate

**Lezione 1 — Le basi**
Variabili e tipi (str, int, float, bool), operatori (+ - * / // % **),
differenza tra `=` e `==`, condizioni `if/elif/else`, indentazione, cicli
`for`/`while`, `range()`.
→ Scheda: scheda_python_basi.pdf

**Lezione 2 — Le liste**
Creazione e accesso (`lista[i]`, indici negativi, `len()`), metodi utili
(`append`, `remove`, `sort`, `in`), ciclare su una lista (`for v in lista`
vs `for i in range(len(lista))`), `enumerate()`.
→ Scheda: scheda_python_liste.pdf

**Lezione 3 — Le funzioni**
`def`, parametri, `return` vs `print`, valori di default. Errore tipico
approfondito: `return` dentro un ciclo `for` esce alla prima iterazione —
va messo dopo il ciclo, allo stesso livello di indentazione del `for`.
→ Scheda: scheda_python_funzioni.pdf

**Lezione 4 — Le stringhe**
5 nuclei: creazione/concatenazione, indicizzazione e slicing (`[inizio:fine]`,
fine sempre escluso), metodi di trasformazione (`strip`, `upper`, `title`,
`replace` — immutabilità), ricerca (`in`, `find`, `count`), `split`/`join`.
→ Scheda: scheda_python_stringhe.pdf

**Scheda di ripasso — Errori tipici**
Nomi riservati da non usare come variabili (`list`, `str`, `len`...),
`split()` che lascia gli spazi nei pezzi, immutabilità delle stringhe e
metodi incatenati, `return` nel posto sbagliato dentro un ciclo.
→ Scheda: scheda_python_errori_tipici.pdf

## Esercizi di riepilogo in corso

**Esercizio 1 — Controllo temperature di collaudo** ✅ completato
Funzioni `conta_sopra_soglia()` e `media()` su una lista di temperature,
report con f-string, bonus con condizione su soglia percentuale.

**Esercizio 2 — Pulizia elenco attività di progetto** — da svolgere
Funzione `pulisci()` con `strip()+title()`, costruzione di una nuova lista
con `.append()` in un ciclo, conteggio con `in`.

## Prossimo argomento
I dizionari (coppie chiave → valore).

## Stile didattico usato finora (utile per continuità)
- Correzioni puntuali sul codice scritto dall'utente, mai riscritto da zero
  senza spiegazione
- Errori spiegati nel "perché", non solo nel "cosa correggere"
- Esercizi con verifica manuale del risultato atteso prima di proseguire
- Schede PDF in formato A4 orizzontale, 4 zone indipendenti (no mappa
  concettuale con frecce), ogni zona con bullet + esempi di codice reali
