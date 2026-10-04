# ###############################################################################
# RIPASSO FONDAMENTI DI PROGRAMMAZIONE - Lezioni 1-4 + Laboratorio
# ###############################################################################

# ! LEGENDA (serve l'estensione "Better Comments" per i colori)
# TODO  -> consegne / cose da fare
# ?     -> spiegazioni
# *     -> punti da evidenziare (esempi, trucchi, formule)
# !     -> cose importanti (errori tipici, attenzione)

# ! Il file si può eseguire tutto: gli errori sono sempre lasciati come commento.


# ###############################################################################
# 1. TIPI, VARIABILI, CONVERSIONI (Lezione 1-2)
# ###############################################################################

# * Tipi base: int (interi), float (virgola mobile), str (stringhe), bool (True/False)
# * type(x) restituisce il tipo di x

eta = 17              # int
altezza = 1.65        # float
nome = "Hermione"     # str
maggiorenne = False   # bool
print(type(eta), type(altezza), type(nome), type(maggiorenne))

# ? Una variabile è un NOME associato a un oggetto (valore).
# ? Con "=" Python valuta prima la parte DESTRA, poi associa il risultato al nome a sinistra.
# ? eta = eta + 1 non è un'equazione: prende il valore attuale di eta, aggiunge 1
# ? e ri-associa il risultato al nome eta.

# * Conversioni: int(), float(), str(), bool()
print(int("42"), float("52.29"), str(7), bool(0))

# ! input() restituisce SEMPRE una stringa: per usarla come numero va convertita
# ! eta = int(input("Quanti anni hai? "))
# ! base = float(input("Base: "))

# ! In Python il separatore decimale è il PUNTO: 24.95, non 24,95
# ! (con la virgola si crea una tupla!)

# * print() con più valori: li separa con uno spazio
print("Ciao", nome, "hai", eta, "anni")

# * Valore booleano di altri oggetti (bool(x)):
# *   False: 0, 0.0, "" (stringa vuota)
# *   True: ogni numero diverso da 0, ogni stringa non vuota
print(bool(0), bool(0.0), bool(""), bool(-42), bool("ciao"))


# ###############################################################################
# 2. OPERATORI ARITMETICI
# ###############################################################################

# *  +   somma            -   sottrazione        *   prodotto
# *  /   divisione (sempre float: 10/2 = 5.0)
# *  //  divisione intera (scarta i decimali)
# *  %   resto (modulo)
# *  **  potenza

print(10 / 2, 17 // 5, 17 % 5, 2 ** 3)

# ! ^ NON è la potenza: in Python è lo XOR bit a bit. La potenza è **
# ! 2^3 dà 1 (sbagliato!), 2**3 dà 8
print(2 ^ 3, 2 ** 3)

# ? Precedenza (dalla più alta): ** -> * / // % -> + -
# ? Con le parentesi decido io l'ordine.
# ! Attenzione: delta ** 1/2 = (delta**1)/2, NON la radice! Serve delta ** (1/2) o delta ** 0.5

# * Trucchi con % e //
# *   n % 2 == 0   -> n è pari
# *   n % 10       -> ultima cifra di n
# *   n // 10      -> n senza l'ultima cifra
# *   secondi % 60 e secondi // 60 -> conversione secondi -> minuti
print(7 % 2 == 0, 4 % 2 == 0, 123 % 10, 123 // 10)

# * Operatori unari: +2 vale 2; 2++2 vale 4 (2 + (+2)); 2--2 vale 4
# ! Python NON ha x++ : si scrive x += 1
print(2 ++ 2, 2 -- 2)

# * Assegnamenti potenziati
x = 5
x += 3     # x = x + 3  -> 8
x *= 2     # x = x * 2  -> 16
x -= 4     # x = x - 4  -> 12
x //= 5    # x = x // 5 -> 2
x %= 2     # x = x % 2  -> 0
print(x)

# * Assegnamento multiplo e scambio senza variabile temporanea
a, b = 1, 2
a, b = b, a
print(a, b)         # 2 1
x = y = 1           # entrambe valgono 1

# ! Errori sintattici classici sugli assegnamenti
# ! 42 = n   -> SyntaxError (a sinistra serve una variabile)
# ! 02       -> SyntaxError (zeri iniziali non ammessi; ottale = 0o2)
# ! xy       -> è il NOME di una variabile, il prodotto si scrive x*y


# ###############################################################################
# 3. STRINGHE (Lezione 2)
# ###############################################################################

s = "Hermione"

# * Apici singoli e doppi sono equivalenti. Per apostrofi: "I'm" oppure 'I\'m'
# * Stringhe su più righe: """ ... """
# * Caratteri speciali: \n (a capo), \t (tab), \\ (backslash)

# * Concatenazione (+) e ripetizione (*)
print("Ciao " + s, s * 2)

# * Appartenenza con in (case-sensitive!)
print("Her" in s, "h" in s)

# * len(): numero di caratteri (gli spazi contano!)
print(len(s))       # 8
# ! len("     ") = 5, vale 0 solo per la stringa vuota ""

# * Indicizzazione: si parte da 0. Ultimo indice = len(s) - 1
# *   H  e  r  m  i  o  n  e
# *   0  1  2  3  4  5  6  7
# *  -8 -7 -6 -5 -4 -3 -2 -1
print(s[0], s[4], s[-1], s[-2])
# ! s[8] -> IndexError (indice fuori dall'intervallo)

# * Slicing: s[start:end:step]
# *   start INCLUSO, end ESCLUSO; il numero di caratteri è end - start
# *   Trucco: gli indici sono i "tagli" tra i caratteri
print(s[0:4])    # Herm
print(s[2:6])    # rmio
print(s[:4])     # Herm   (start omesso -> dall'inizio)
print(s[4:])     # ione   (end omesso -> fino alla fine)
print(s[:])      # tutta la stringa
print(s[::2])    # Hrin   (un carattere ogni due)
print(s[::3])    # Hmn
print(s[::-1])   # enoimreH (al contrario)
print(s[::-2])   # eome
# ! Lo slicing NON dà errore se esci dai limiti: s[0:100] va bene, s[3:1] dà ""

# * index() e find(): posizione della PRIMA occorrenza di una sottostringa
testo = "Hermione and Harry Potter"
print(testo.index("Harry"))    # 13
print(testo.find("Harry"))     # 13
print(testo.find("Ron"))       # -1
# ! Se non trova: index() -> ValueError, find() -> -1

# * Estrarre una parola: inizio -> fine -> slicing
start = testo.index("Harry")
end = start + len("Harry")
print(testo[start:end])        # Harry

# * Metodi che RESTITUISCONO una nuova stringa
print(s.lower(), s.upper(), s.replace("e", "E"))
print("  ciao  ".strip(), "  ciao  ".lstrip(), "  ciao  ".rstrip())
print("xxciaoxx".strip("x"))
print("Hermione and Harry".split())          # lista di parole
print("Hermione.Harry.Ron".split("."))       # separatore a scelta
print("a".isdigit(), "7".isdigit(), " ".isspace())

# ! Le stringhe sono IMMUTABILI: s[0] = "h" -> TypeError
# ! I metodi non modificano s: bisogna riassegnare  ->  s = s.lower()
nuovo = "h" + s[1:]
print(nuovo)

# ! "trim" non esiste in Python: l'equivalente è strip()

# * f-string: f"testo {variabile} {espressione}"
nome, eta = "Hermione", 17
print(f"Ciao {nome}, hai {eta} anni. L'anno prossimo {eta + 1}.")
prezzo, sconto = 45.9876, 0.25
print(f"Prezzo: {prezzo:.2f} euro")      # 2 decimali
print(f"Sconto: {sconto:.0%}")           # percentuale senza decimali
print(f"{5:02d}")                         # 05 (sempre 2 cifre)


# ###############################################################################
# 4. BOOLEANI, CONFRONTI, OPERATORI LOGICI
# ###############################################################################

# * Confronti: ==  !=  <  >  <=  >=   (producono True/False)
# * = è un assegnamento, == è un confronto
print(5 == 5, 5 != 7, 12 < 11.3, 10 >= 10)

# * Confronto concatenato: più leggibile di "voto >= 0 and voto <= 30"
voto = 27
print(0 <= voto <= 30)

# * Confronto tra stringhe: == è case-sensitive; < e > seguono l'ordine dei caratteri
print("Harry" == "harry", "H" < "h")

# * and: True solo se ENTRAMBE vere
# * or:  True se ALMENO UNA è vera
# * not: inverte
# * Precedenza: not -> and -> or  (nel dubbio, parentesi)
piove, ho_ombrello = True, False
print(piove and not ho_ombrello)

# * Short-circuit: Python si ferma appena il risultato è noto
# *   False and ... -> False     True or ... -> True
# ! Utile per controlli sicuri: l'ordine delle condizioni conta!
testo_vuoto = ""
print(bool(testo_vuoto and testo_vuoto[0] == "H"))   # nessun IndexError


# ###############################################################################
# 5. CONDIZIONI: if / elif / else (Lezione 3)
# ###############################################################################

# ! L'INDENTAZIONE è parte della sintassi: decide quali righe stanno nel blocco
# ! Dopo if/elif/else/for/while/def ci vogliono i DUE PUNTI :

voto = 27
if voto >= 30:
    print("Ottimo")
elif voto >= 27:
    print("Molto buono")
elif voto >= 18:
    print("Sufficiente")
else:
    print("Non superato")

# ? if/else = scelta tra due percorsi (ne viene eseguito uno solo).
# ? elif = ulteriori alternative; Python si ferma al PRIMO ramo vero.
# ! Con if consecutivi (senza elif) i test sono INDIPENDENTI: vengono valutati tutti.
# ! Ordine: prima la condizione più restrittiva (>= 30 prima di >= 18)

# * match/case (optional): alternativa a lunghe catene di if/elif
azione = "I"
match azione:
    case "A":
        print("Attacco")
    case "I":
        print("Inventario")
    case _:                      # _ = qualsiasi altro valore
        print("Non riconosciuto")


# ###############################################################################
# 6. CICLI: for, range, while, break, continue
# ###############################################################################

# * for elemento in sequenza: -> visita gli elementi uno alla volta
for carattere in "Harry":
    print(carattere, end=" ")
print()

# * range(stop) / range(start, stop) / range(start, stop, step)   (stop ESCLUSO)
print(list(range(5)), list(range(2, 7)), list(range(2, 10, 2)), list(range(10, 0, -2)))

# * Se serve anche la posizione
parola = "Harry"
for i in range(len(parola)):
    print(i, parola[i], end=" | ")
print()
# * Meglio ancora: enumerate()
for i, c in enumerate(parola):
    print(i, c, end=" | ")
print()

# * Pattern CONTATORE
def conta_a(parola):
    contatore = 0
    for c in parola.lower():
        if c == "a":
            contatore += 1
    return contatore
print(conta_a("Azkaban"))        # 3

# * while: ripete finché la condizione è vera (quando non so quante iterazioni servono)
x = 0
while x < 5:
    print(x, end=" ")
    x += 1                       # ! senza questo -> ciclo infinito
print()

# * for -> sequenza / numero di iterazioni noto;  while -> condizione dinamica
# * break -> esce subito dal ciclo più interno
# * continue -> salta alla iterazione successiva
for c in "Hermione":
    if c == "o":
        break
    print(c, end="")
print()
for c in "Hermione".lower():
    if c in "aeiou":
        continue
    print(c, end="")
print()


# ###############################################################################
# 7. FUNZIONI
# ###############################################################################

# * def nome(parametri):  ...  return risultato
# ? INPUT -> parametri;  ELABORAZIONE -> corpo;  OUTPUT -> return
# ? Definire una funzione NON la esegue: bisogna chiamarla.
# ? Parametro = nome nella definizione; argomento = valore passato nella chiamata.

def quadrato(x):
    return x ** 2
print(quadrato(5))

# ! print() mostra a schermo, return RESTITUISCE il valore a chi chiama.
# ! Se la consegna dice "ritorna"/"restituisce" serve return.
# ! Una funzione senza return restituisce None.
# ! return termina subito la funzione (utile per i controlli anticipati)

def doppio_stampa(x):
    print(x * 2)
a = doppio_stampa(5)
print(a)                         # None

# * Restituire direttamente una condizione
def pari(n):
    return n % 2 == 0
print(pari(8), pari(5))

# * return di più valori = tupla
def somma_e_prodotto(a, b):
    return a + b, a * b
s, p = somma_e_prodotto(3, 4)
print(s, p)


# ###############################################################################
# 8. CONTENITORI (Lezione 4)
# ###############################################################################

# * LISTA [ ]  - ordinata, indicizzata, MUTABILE
voti = [28, 30, 25, 27]
print(voti[0], voti[-1], voti[1:3], voti[::-1], len(voti))
voti[0] = 29                     # modifica diretta
# ! voti[10] -> IndexError

# * Metodi delle liste (modificano la lista!)
L = [1, 2, 3]
L.append(4)                      # aggiunge in fondo
L.insert(1, 99)                  # inserisce in posizione 1
L.remove(99)                     # elimina la prima occorrenza
ultimo = L.pop()                 # elimina e restituisce l'ultimo
print(L, ultimo)
# * pop(i) elimina e restituisce l'elemento in posizione i

# ! append() restituisce None: NON scrivere  L = L.append(x)
A, B = ["Harry", "Hermione"], ["Ron", "Luna"]
A.append(B)                      # B diventa UN elemento: [.., .., ['Ron','Luna']]
print(A, len(A))
A = ["Harry", "Hermione"]
A.extend(B)                      # aggiunge gli elementi uno a uno
print(A, len(A))

# * in / not in funzionano anche sulle liste
print("Lumos" in ["Lumos", "Accio"], "x" not in ["a"])

# * Pattern ACCUMULATORE
somma = 0
for v in [28, 30, 25, 27]:
    somma += v
print(somma, somma / 4)          # somma e media

# * Pattern FILTRO: for -> if -> append -> nuova lista
sufficienti = []
for v in [12, 18, 25, 16, 30]:
    if v >= 18:
        sufficienti.append(v)
print(sufficienti)

# ! Non modificare una lista mentre la attraversi (remove dentro un for):
# ! costruisci una nuova lista

# * ALIASING: B = A NON copia, crea un secondo nome per la STESSA lista
A = [1, 2, 3]
B = A
B[0] = 99
print(A)                         # [99, 2, 3]
# * Copia indipendente: A.copy() oppure A[:]
C = A.copy()
C[0] = 0
print(A, C)
# * == confronta i valori, is confronta se è lo STESSO oggetto
print([1, 2] == [1, 2], [1, 2] is [1, 2])

# * TUPLA ( ) - ordinata, indicizzata, IMMUTABILE
studente = ("Hermione", 17, "Grifondoro")
nome, eta, casa = studente       # unpacking: n. variabili = n. elementi
# ! studente[1] = 18 -> TypeError

# * SET { } - elementi UNICI, non indicizzato, mutabile
case = {"Grifondoro", "Serpeverde", "Grifondoro"}
case.add("Corvonero")
print(len(case))                 # 3
print(set([1, 1, 2, 3, 3]))      # elimina i duplicati
# ! {} vuoto è un dizionario, non un set: set() per il set vuoto

# * DIZIONARIO { chiave: valore } - chiavi uniche, accesso per chiave
d = {"Harry": 28, "Hermione": 30}
d["Ron"] = 25                    # aggiunge
d["Harry"] = 29                  # modifica
print(d["Hermione"])
for chiave in d:
    print(chiave, d[chiave], end=" | ")
print()
for chiave, valore in d.items():
    print(chiave, valore, end=" | ")
print()

# * Riepilogo
# *   tipo    | ordinato | per posizione | modificabile
# *   str     |   sì     |     sì        |    NO
# *   list    |   sì     |     sì        |    sì
# *   tuple   |   sì     |     sì        |    NO
# *   set     |   no     |     no        |    sì
# *   dict    | inserim. |  per chiave   |    sì
# ? Scelta: sequenza modificabile -> list; non modificabile -> tuple;
# ? elementi unici/appartenenza -> set; associazioni chiave->valore -> dict


# ###############################################################################
# 9. ERRORI E TRACEBACK
# ###############################################################################

# ? Tre tipi di errore:
# ?  1. SyntaxError   -> il programma non parte (sintassi sbagliata)
# ?  2. Runtime error -> il programma parte e si interrompe
# ?  3. Errore logico -> nessun messaggio, ma il risultato è sbagliato
# * Il traceback si legge dal BASSO verso l'alto: tipo di errore, riga, causa.

# * NameError            variabile/nome non definito (anche print(xy) senza xy)
# * ValueError           valore non accettabile: int("ciao"), "abc".index("z")
# * TypeError            tipo sbagliato: "età: " + 20 ; s[0] = "h" su stringa
# * ZeroDivisionError    10 / 0, 10 // 0, 10 % 0 (NON è un ValueError!)
# * IndexError           indice fuori intervallo (stringhe e liste)
# * IndentationError     indentazione mancante o errata
# * SyntaxError          stringa non chiusa, parentesi mancanti, "42 = n", "02"...

# * try / except per gestire un errore
try:
    risultato = 10 / 0
except ZeroDivisionError:
    risultato = None
print(risultato)

# ! Controllo parentesi: parti da 0, +1 per ogni (, -1 per ogni ).
# ! Alla fine devi tornare a 0 e non scendere mai sotto 0.


# ###############################################################################
# 10. FORMULE UTILI
# ###############################################################################

# * Sconto percentuale:    prezzo - (prezzo * sconto / 100)
# *                  oppure prezzo * (100 - sconto) / 100
# ! prezzo - sconto / 100 è SBAGLIATO (la divisione si fa prima)

# * Equazione di 2° grado a*x**2 + b*x + c = 0
# *   delta = b**2 - 4*a*c
# *   x1 = (-b + delta ** 0.5) / (2*a)
# *   x2 = (-b - delta ** 0.5) / (2*a)
# ! Servono le parentesi sul NUMERATORE: (-b + radice) / (2*a)
# ? delta < 0 -> radici complesse (Python restituisce numeri complessi con ** 0.5)

# * Radice cubica: n ** (1/3); per n negativo: -((-n) ** (1/3))

# * Conversione secondi -> ore:min:sec
# *   ore = tot // 3600;  resto = tot % 3600;  minuti = resto // 60;  sec = resto % 60

# * Velocità media = spazio / tempo        (km/h, miglia/h)
# * Cadenza (passo) media = tempo / spazio (min/km, sec/miglio)
# * 1 miglio = 1.61 km  ->  km / 1.61 = miglia

# * Volume sfera = 4/3 * 3.14 * r**3
# ! Nel file di laboratorio B.4 è scritto con 5^3: va corretto in 5**3
volume = 4 / 3 * 3.14 * 5 ** 3
print(volume)

# * Riporto ore/minuti: calcola le ore dal TOTALE dei minuti, poi riduci con %
# ! Se riduci prima con % 60 perdi il riporto verso le ore
tot_min = 91
print(tot_min // 60, tot_min % 60)    # 1 ora e 31 minuti


# ###############################################################################
# 11. ESERCIZI SVOLTI (versioni corrette)
# ###############################################################################

# * ------------------------------------------------------------------------------
# * somma_cifre
# * ------------------------------------------------------------------------------
# TODO Funzione somma_cifre(s): somma le cifre di una stringa. "85721" -> 23
def somma_cifre(s):
    somma = 0
    for c in s:
        somma += int(c)
    return somma
# ? "cifre decimali" = cifre in base 10 (0-9), non numeri con la virgola.
# ? int(c) converte il carattere in numero; float darebbe 23.0.

# * ------------------------------------------------------------------------------
# * bin_str_to_dec
# * ------------------------------------------------------------------------------
# TODO Funzione bin_str_to_dec(s): da stringa binaria a decimale. "00101" -> 5
# ! Suggerimento: nuovo_valore = vecchio_valore * 2 + nuova_cifra
def bin_str_to_dec(s):
    risultato = 0
    for c in s:
        risultato = risultato * 2 + int(c)
    return risultato
# ? Come in base 10 (3 -> 34 -> 345 con *10 + cifra), in base 2 si raddoppia
# ? il valore accumulato e si somma la nuova cifra. Gli zeri iniziali non contano.

# * ------------------------------------------------------------------------------
# * cubic_root
# * ------------------------------------------------------------------------------
# TODO Funzione cubic_root(n): radice cubica, anche per numeri negativi.
def cubic_root(n):
    if n < 0:
        return -round((-n) ** (1/3), 10)
    return round(n ** (1/3), 10)
# ? (-8) ** (1/3) dà un numero complesso: il segno va gestito a parte.
# ? round(..., 10) pulisce le imprecisioni dei float (es. 3.0000000000000004).

# * ------------------------------------------------------------------------------
# * even_minus_odd (senza liste)
# * ------------------------------------------------------------------------------
# TODO Funzione even_minus_odd(a, b, c, d, e): somma dei pari - somma dei dispari.
def even_minus_odd(a, b, c, d, e):
    somma_pari = 0
    somma_dispari = 0
    if a % 2 == 0:
        somma_pari += a
    else:
        somma_dispari += a
    if b % 2 == 0:
        somma_pari += b
    else:
        somma_dispari += b
    if c % 2 == 0:
        somma_pari += c
    else:
        somma_dispari += c
    if d % 2 == 0:
        somma_pari += d
    else:
        somma_dispari += d
    if e % 2 == 0:
        somma_pari += e
    else:
        somma_dispari += e
    return somma_pari - somma_dispari
# ? Cinque if/else INDIPENDENTI (non elif), così ogni numero viene valutato.
# ? In Python -3 % 2 vale 1: i dispari negativi sono riconosciuti correttamente.

# * Versione con lista (più breve)
def even_minus_odd_lista(a, b, c, d, e):
    risultato = 0
    for n in [a, b, c, d, e]:
        if n % 2 == 0:
            risultato += n
        else:
            risultato -= n
    return risultato

# * ------------------------------------------------------------------------------
# * check_grade
# * ------------------------------------------------------------------------------
# TODO check_grade(a, b, c): somma dei voti se tutti in [0, 30], altrimenti -1
def check_grade(a, b, c):
    if 0 <= a <= 30 and 0 <= b <= 30 and 0 <= c <= 30:
        return a + b + c
    return -1

# * ------------------------------------------------------------------------------
# * check_date
# * ------------------------------------------------------------------------------
# TODO check_date(d, m, y): True se la data è valida (anni bisestili ignorabili)
def check_date(d, m, y):
    if m < 1 or m > 12:
        return False
    if d < 1:
        return False
    if m == 2:
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            return d <= 29
        return d <= 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return d <= 30
    return d <= 31
# ? Bisestile: divisibile per 400, oppure per 4 ma non per 100.

# * ------------------------------------------------------------------------------
# * chiedi_voto
# * ------------------------------------------------------------------------------
# TODO chiedi_voto(): chiede un voto finché non è tra 0 e 30, poi lo ritorna
# ! Non lo eseguo qui perché usa input()
def chiedi_voto():
    while True:
        voto = int(input("Che voto hai? "))
        if 0 <= voto <= 30:
            return voto
# ? while True + return: la riga con input compare una volta sola.

# * ------------------------------------------------------------------------------
# * strip_spazi (senza strip)
# * ------------------------------------------------------------------------------
# TODO strip_spazi(s): elimina gli spazi a inizio e fine, senza str.strip()
def strip_spazi(s):
    x = 0
    while x < len(s) and s[x] == " ":
        x += 1
    y = len(s) - 1
    while y >= 0 and s[y] == " ":
        y -= 1
    return s[x:y + 1]
# ? x avanza sul primo carattere non-spazio, y retrocede sull'ultimo.
# ? L'ordine "x < len(s) and s[x]" evita l'IndexError (short-circuit).
# ? +1 perché l'end dello slicing è ESCLUSO.
# ? Stringa vuota o di soli spazi -> x supera y -> slicing vuoto -> "".

# * ------------------------------------------------------------------------------
# * roots / root_max
# * ------------------------------------------------------------------------------
# TODO roots(a, b, c): ritorna entrambe le radici di a*x**2 + b*x + c
def roots(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    return x1, x2

# TODO root_max(a, b, c): ritorna la maggiore (se complesse, una qualsiasi)
def root_max(a, b, c):
    x1, x2 = roots(a, b, c)
    if b ** 2 - 4 * a * c >= 0:
        return max(x1, x2)
    return x2
# ! max() tra numeri complessi dà TypeError: serve il controllo su delta.

# * ------------------------------------------------------------------------------
# * dec_frac_str_to_dec (stringa "52.29")
# * ------------------------------------------------------------------------------
def dec_frac_str_to_dec(s):
    return float(s)               # 52.29 come numero
def dec_frac_str_to_decs(s):
    return int(s[3:])             # 29: solo le cifre dopo il punto
# ? Il punto è in posizione 2, le cifre decimali iniziano in posizione 3.
# ! s[2:] includerebbe il punto: int(".29") -> ValueError

# * ------------------------------------------------------------------------------
# * print_hello
# * ------------------------------------------------------------------------------
def print_hello():
    nome = input("Come ti chiami? ")
    return f"Ciao {nome}. Buona giornata!"

# * ------------------------------------------------------------------------------
# * Esercizi con numeri (Optional B)
# * ------------------------------------------------------------------------------
# * B.1 secondi in 42 min e 42 s:   42 * 60 + 42
# * B.2 miglia in 10 km:            10 / 1.61
# * B.3 velocità media (miglia/s):  (10/1.61) / (42*60+42)   (x 3600 per miglia/h)
# *     cadenza media (s/miglio):   (42*60+42) / (10/1.61)  -> // 60 minuti, % 60 secondi
# * B.4 volume sfera r=5:           4/3 * 3.14 * 5**3
# * B.5 60 libri, sconto 40%, spedizione 3 + 0.75 per le altre 59:
# *     (24.95*60) - (((24.95*60)*40)/100) + 3 + (0.75*59)    -> 945.45
# ! La spedizione aggiuntiva si applica a (copie - 1) = 59 copie, non a 60.
# * B.6 rientro (esce alle 6:52; 8:15 + 3*7:12 + 9:45):
secondi = 15 + (3 * 12) + 45
secondi_rimasti = secondi % 60
min_aggiuntivi = secondi // 60
min_per_ora = min_aggiuntivi + 8 + (3 * 7) + 9 + 52
ore = (min_per_ora // 60) + 6
minuti = min_per_ora % 60
print(f"Rientro: {ore}:{minuti:02d}:{secondi_rimasti:02d}")     # 7:31:36
# ! "min" è il nome di una funzione di Python: meglio usare "minuti".


# ###############################################################################
# 12. RISPOSTE AGLI ESPERIMENTI (Optional A)
# ###############################################################################

# ? A.1 Apici non chiusi: SyntaxError (unterminated string literal), sulla stessa riga.
# ?     Solo con """ ... """ la stringa può continuare sulle righe successive.
# ? A.2 Divisione per 0: ZeroDivisionError (anche con // e %).
# ? A.3 print senza parentesi: SyntaxError (Missing parentheses in call to 'print');
# ?     "print" da solo non fa nulla; con una parentesi sola: SyntaxError.
# ? A.4 +2 vale 2; 2++2 vale 4 (2 + (+2)).
# ? A.5 02: SyntaxError in Python 3.
# ? A.6 xy non è x*y: è il nome di una variabile (NameError se non definita).
# ? A.7 42 = n: SyntaxError (cannot assign to literal).
# ? A.8 x = y = 1: assegnamento multiplo, entrambe valgono 1.
# ? A.9 ";" è permesso (separa istruzioni sulla stessa riga); "." dà SyntaxError.


# ###############################################################################
# 13. ERRORI TIPICI EMERSI NEGLI ESERCIZI
# ###############################################################################

# ! 1. ^ al posto di **                       (potenza)
# ! 2. delta ** 1/2 al posto di delta ** 0.5  (radice quadrata)
# ! 3. Numeratore senza parentesi             (-b + r) / (2*a)
# ! 4. i == 0 con i carattere                 -> confrontare con '0' (stringa)
# ! 5. s[x:y] invece di s[x:y + 1]            (end escluso)
# ! 6. s.len(-1)                              -> len(s) - 1  (len è una funzione)
# ! 7. Parentesi sbilanciate nelle espressioni lunghe: spezza in variabili
# ! 8. Virgola decimale (24,95) al posto del punto
# ! 9. /100 messo fuori posto nello sconto: va solo sulla parte percentuale
# ! 10. Oltre fine stringa nei while: prima l'indice (x < len(s)), poi s[x]
# ! 11. Riporto ore/minuti: calcola le ore PRIMA di ridurre i minuti con %
# ! 12. print al posto di return nelle funzioni
# ! 13. Dimenticare di riassegnare: s.lower() da solo non cambia s
# ! 14. L = L.append(x) -> L diventa None


# ###############################################################################
# TEST AUTOMATICI (se nessun assert fallisce, tutto è ok)
# ###############################################################################

assert somma_cifre("85721") == 23
assert bin_str_to_dec("00101") == 5 and bin_str_to_dec("1111") == 15
assert cubic_root(8) == 2.0 and cubic_root(-8) == -2.0
assert even_minus_odd(1, 2, 3, 4, 5) == -3
assert even_minus_odd_lista(2, 2, 2, 2, 2) == 10
assert check_grade(21, 18, 2) == 41 and check_grade(21, 32, 2) == -1
assert check_date(30, 2, 2017) is False and check_date(1, 1, 1111) is True
assert check_date(31, 4, 2011) is False
assert strip_spazi("   ciao mondo   ") == "ciao mondo"
assert strip_spazi("     ") == "" and strip_spazi("") == ""
assert roots(1, -3, 2) == (2.0, 1.0)
assert root_max(1, -3, 2) == 2.0
assert dec_frac_str_to_dec("52.29") == 52.29
assert dec_frac_str_to_decs("52.29") == 29
print("\nTutti i test sono passati.")