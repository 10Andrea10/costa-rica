# Mappe Costa Rica - da condividere su Telegram

- **costa-rica-giorno-per-giorno.html**: file unico, selezione del giorno, tappe numerate, schema offline, mappa stradale online e link Google Maps. Inviare come DOCUMENTO su Telegram; scaricarlo e aprirlo in un browser. Alcune anteprime interne non eseguono JavaScript: in tal caso usare il PDF.
- **costa-rica-giorno-per-giorno.pdf**: versione leggibile offline per giornata, con pagine di continuazione se necessarie e link alle tappe. Per la navigazione i link richiedono rete o mappe scaricate nell'app.
- **attivita.json**: dati della mappa. Uso tecnico, non necessario da inviare all'amica. Non contiene dati sensibili, contratti o conferme di prenotazione.

Le proposte sono marcate; i giorni 8-11 restano aperti. Il giro del 5 con soste gratuite a Grecia, Sarchí e Zarcero è stato scelto dall’utente; attività a pagamento dei giorni seguenti da riconfermare. Le linee congiungono le tappe in ordine: **non sono le strade da percorrere**. I pin sono orientativi e non sostituiscono la verifica dell'ingresso. Per guidare usare i pulsanti che cercano il nome corretto in Google Maps.

La base stradale usa OpenStreetMap online, con attribuzione; il file non scarica mappe per uso offline. Lo schema geografico e tutti i testi sono incorporati e leggibili senza rete. Workflow GitHub Pages preparato: al push su main pubblica HTML e PDF su https://10andrea10.github.io/costa-rica/. Nessun deploy o invio Telegram effettuato dall’assistente. Il link al PDF è incluso nella mappa.

## Aggiornare
1. Aggiornare il piano Markdown dopo una decisione dell'utente.
2. Allineare `attivita.json` (proposte/conferme, orari e budget).
3. Preparare l'ambiente Python come descritto nel `README.md`: Python 3.11+, venv e `requirements.txt` con versioni fissate. Funziona su Ubuntu e macOS.
4. Eseguire `.venv/bin/python strumenti/aggiorna.py` dalla radice: genera HTML e PDF dagli stessi dati. Non servono Swift o Docker.
5. Controllare contenuti, link e impaginazione prima di consegnare. Non installare dipendenze globali né modificare i backup.

## GitHub Pages
Il workflow `.github/workflows/pages.yml` rigenera HTML e PDF dal JSON su Ubuntu ad ogni push su main. Pubblica i risultati senza committarli nella repository. Non pubblica dati JSON, strumenti o registri come pagine del sito. La repository è pubblica: i file committati rimangono comunque accessibili su GitHub. Commit/push richiedono l'autorizzazione esplicita dell'utente.
