# Costa Rica, giorno per giorno

Mappa per telefono, con tappe per giornata, schema offline, mappa stradale online e link Google Maps. Le proposte restano distinte dalle decisioni confermate.

Sito previsto dopo il primo deploy riuscito: https://10andrea10.github.io/costa-rica/

## Pubblicazione al push

Il workflow `.github/workflows/pages.yml` parte ad ogni push su `main` e può essere avviato manualmente da Actions. Rigenera l'HTML dai dati, poi pubblica soltanto:

- `index.html`: mappa interattiva autonoma.
- `costa-rica-giorno-per-giorno.pdf`: versione offline scaricabile dalla mappa.

GitHub Pages risulta già configurato con sorgente **GitHub Actions**, verificato in sola lettura il 5 novembre 2026. Il workflow non cambia le impostazioni della repository. La pubblicazione avverrà quando i file saranno committati e inviati dall'utente; non è stato eseguito un deploy in questa sessione.

Le Actions sono fissate a release stabili verificate sui repository ufficiali il 5 novembre 2026: [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1), [configure-pages v6.0.0](https://github.com/actions/configure-pages/releases/tag/v6.0.0), [upload-pages-artifact v5.0.0](https://github.com/actions/upload-pages-artifact/releases/tag/v5.0.0), [deploy-pages v5.0.1](https://github.com/actions/deploy-pages/releases/tag/v5.0.1).

## Aggiornare il programma

1. Leggere `AGENTS.md` e allineare preferenze, piano e `mappe/attivita.json` dopo le decisioni dell'utente.
2. Eseguire `python3 strumenti/genera-mappa.py` per aggiornare il file HTML locale.
3. Rigenerare il PDF con `strumenti/genera-pdf.swift` su macOS (comando nello script) e controllare i PNG prodotti.
4. Includere anche il PDF aggiornato nel prossimo push: il workflow lo pubblica senza rigenerarlo, mentre l'HTML è sempre ricostruito dai dati.

Nessun pacchetto da installare per l'HTML. Leaflet 1.9.4 e licenza sono inclusi. Lo schema e i testi funzionano offline; mappa stradale e navigazione richiedono rete. Dettagli in `mappe/LEGGIMI.md`.

La directory di pubblicazione esclude preferenze, backup e strumenti; la repository è comunque pubblica, quindi i file committati sono consultabili su GitHub.
