# Mappe Costa Rica - da condividere su Telegram

- **costa-rica-giorno-per-giorno.html**: file unico, selezione del giorno, tappe numerate, schema offline, mappa stradale online e link Google Maps. Inviare come DOCUMENTO su Telegram; scaricarlo e aprirlo in un browser. Alcune anteprime interne non eseguono JavaScript: in tal caso usare il PDF.
- **costa-rica-giorno-per-giorno.pdf**: versione leggibile offline con una pagina per giornata/alternativa e link alle tappe. Per la navigazione i link richiedono rete o mappe scaricate nell'app.
- **attivita.json**: dati della mappa. Uso tecnico, non necessario da inviare all'amica. Non contiene dati sensibili, contratti o conferme di prenotazione.

Le proposte sono marcate; i giorni 8-11 restano aperti. Il giro del 5 con soste gratuite a Grecia, Sarchí e Zarcero è stato scelto dall’utente; attività a pagamento dei giorni seguenti da riconfermare. Le linee congiungono le tappe in ordine: **non sono le strade da percorrere**. I pin sono orientativi e non sostituiscono la verifica dell'ingresso. Per guidare usare i pulsanti che cercano il nome corretto in Google Maps.

La base stradale usa OpenStreetMap online, con attribuzione; il file non scarica mappe per uso offline. Lo schema geografico e tutti i testi sono incorporati e leggibili senza rete. Workflow GitHub Pages preparato: al push su main pubblica HTML e PDF su https://10andrea10.github.io/costa-rica/. Nessun deploy o invio Telegram effettuato dall’assistente. Il link al PDF è incluso nella mappa.

## Aggiornare
1. Aggiornare il piano Markdown dopo una decisione dell'utente.
2. Allineare `attivita.json` (proposte/conferme, orari e budget).
3. `python3 strumenti/genera-mappa.py` rigenera l'HTML usando Leaflet fissato 1.9.4.
4. Compilare/eseguire `strumenti/genera-pdf.swift` secondo il comando riportato nello script; genera PDF e PNG di controllo. Ispezionare i PNG prima di consegnare.
5. Non installare dipendenze globali né modificare i backup.

## GitHub Pages
Il workflow `.github/workflows/pages.yml` ricostruisce l’HTML e pubblica il PDF presente nella repository. Dopo modifiche al piano rigenerare anche il PDF localmente e includerlo nel push; la CI non lo rigenera. Non pubblica dati JSON, strumenti o registri come pagine del sito. La repository è pubblica: i file committati rimangono comunque accessibili su GitHub.
