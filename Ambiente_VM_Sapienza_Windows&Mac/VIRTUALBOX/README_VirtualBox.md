# 📦 Come scaricare e installare VirtualBox

Guida per installare **VirtualBox**, il programma gratuito che serve per far partire la macchina virtuale del corso. Ci sono le istruzioni per **Mac** e per **Windows**.

> 🔗 Scarica VirtualBox **solo dal sito ufficiale**: <https://www.virtualbox.org/wiki/Downloads>

---

## 📑 Indice

- [Prima di iniziare](#-prima-di-iniziare)
- [Installazione su Mac](#-installazione-su-mac)
- [Installazione su Windows](#-installazione-su-windows)
- [Verifica dell'installazione](#-verifica-dellinstallazione)
- [Problemi comuni](#%EF%B8%8F-problemi-comuni)
- [Prossimo passo](#-prossimo-passo)

---

## ✅ Prima di iniziare

| Requisito | Consigliato |
|---|---|
| Memoria RAM | almeno 8 GB |
| Spazio libero su disco | almeno 20 GB |
| Connessione a internet | sì, per il download |
| Permessi di amministratore | sì, per installare il programma |

---

## 🍎 Installazione su Mac

### 1. Scopri che Mac hai

I Mac hanno due tipi di processore e il download è diverso per ciascuno.

1. Clicca sul menu  **Apple** in alto a sinistra.
2. Scegli **Informazioni su questo Mac**.
3. Guarda la voce **Chip** oppure **Processore**:

| Se leggi... | Il tuo Mac è | Scarica la versione |
|---|---|---|
| `Apple M1`, `M2`, `M3`, `M4`... | **Apple Silicon** | *macOS / Apple Silicon hosts* |
| `Intel` | **Intel** | *macOS / Intel hosts* |

> ⚠️ **Mac con Apple Silicon:** VirtualBox funziona, ma può far partire soltanto macchine virtuali costruite per processori ARM. Controlla nel README della macchina virtuale per Mac che il file sia quello giusto per il tuo Mac.

### 2. Scarica VirtualBox

1. Vai su <https://www.virtualbox.org/wiki/Downloads>.
2. Clicca su **macOS / Apple Silicon hosts** oppure **macOS / Intel hosts**, in base al tuo Mac.
3. Aspetta la fine del download del file `.dmg`.

### 3. Installa

1. Apri il file `.dmg` appena scaricato (di solito in **Download**).
2. Fai doppio clic su **VirtualBox.pkg**.
3. Segui la procedura guidata cliccando su **Continua** e poi su **Installa**.
4. Inserisci la **password del Mac** quando richiesto.

### 4. Autorizza il software

Al primo avvio macOS può bloccare i componenti di VirtualBox.

1. Apri **Impostazioni di Sistema** → **Privacy e sicurezza**.
2. Scorri fino al messaggio che parla di software dello sviluppatore **Oracle**.
3. Clicca su **Consenti** e inserisci la password.
4. Se richiesto, **riavvia il Mac**.

> 💡 Se non compare nessun messaggio, passa direttamente alla [verifica](#-verifica-dellinstallazione).

---

## 🪟 Installazione su Windows

### 1. Controlla i requisiti

- Windows 10 o Windows 11, a 64 bit.
- La **virtualizzazione** attiva sul computer (di solito lo è già). Per controllare: apri il **Task Manager** (`Ctrl + Maiusc + Esc`), vai nella scheda **Prestazioni** → **CPU** e guarda che accanto a *Virtualizzazione* ci sia scritto **Abilitato**.

### 2. Scarica VirtualBox

1. Vai su <https://www.virtualbox.org/wiki/Downloads>.
2. Clicca su **Windows hosts**.
3. Aspetta la fine del download del file `.exe`.

### 3. Installa

1. Fai doppio clic sul file `.exe` scaricato.
2. Se Windows chiede il permesso di apportare modifiche, clicca su **Sì**.
3. Nella procedura guidata clicca su **Next** e lascia le opzioni predefinite.
4. Appare un avviso che la **connessione di rete verrà interrotta per un momento**: clicca su **Yes**.
5. Clicca su **Install** e attendi.
6. Alla fine clicca su **Finish**. Se richiesto, **riavvia il PC**.

---

## 🔍 Verifica dell'installazione

1. Apri **VirtualBox** dal Launchpad (Mac) o dal menu Start (Windows).
2. Se si apre la finestra **Oracle VirtualBox Manager**, l'installazione è riuscita. 🎉

---

## ⚠️ Problemi comuni

| Problema | Cosa provare |
|---|---|
| **Mac:** VirtualBox non parte o chiede di autorizzare il software | Ripeti il passaggio *Autorizza il software* e riavvia il Mac |
| **Windows:** la macchina virtuale non si avvia, errore sulla virtualizzazione | Attiva la virtualizzazione (*Intel VT-x* o *AMD-V*) dal BIOS/UEFI del PC |
| **Windows:** errore di conflitto con altri programmi di virtualizzazione | Chiudi gli altri programmi di virtualizzazione e riavvia il PC |
| L'installazione si blocca o fallisce | Riscarica il file dal sito ufficiale e riprova |

---

## ➡️ Prossimo passo

Dopo aver installato VirtualBox, passa al README della **macchina virtuale** per il tuo sistema (Mac o Windows) e segui le istruzioni per importarla.

<p align="center">Buon lavoro! 🚀</p>
