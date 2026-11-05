# Costa Rica, giorno per giorno

Mappa per telefono, con tappe per giornata, schema offline, mappa stradale online e link Google Maps. Le proposte restano distinte dalle decisioni confermate.

Sito previsto dopo il primo deploy riuscito: https://10andrea10.github.io/costa-rica/

## Pubblicazione al push

Il workflow `.github/workflows/pages.yml` parte ad ogni push su `main` e può essere avviato manualmente da Actions. Rigenera HTML e PDF dagli stessi dati su Ubuntu, poi pubblica soltanto:

- `index.html`: mappa interattiva autonoma.
- `costa-rica-giorno-per-giorno.pdf`: versione offline scaricabile dalla mappa.

GitHub Pages risulta già configurato con sorgente **GitHub Actions**, verificato in sola lettura il 5 novembre 2026. Il workflow non cambia le impostazioni della repository. La pubblicazione avverrà quando i file saranno committati e inviati dall'utente; non è stato eseguito un deploy in questa sessione.

Le Actions sono fissate a release stabili verificate sui repository ufficiali il 5 novembre 2026: [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1), [configure-pages v6.0.0](https://github.com/actions/configure-pages/releases/tag/v6.0.0), [upload-pages-artifact v5.0.0](https://github.com/actions/upload-pages-artifact/releases/tag/v5.0.0), [deploy-pages v5.0.1](https://github.com/actions/deploy-pages/releases/tag/v5.0.1).

## Ubuntu / OpenClaw via Telegram

La generazione usa Python, senza Swift, framework Apple, browser o servizi esterni. Supportati Python 3.11 o superiore (Ubuntu 24.04 fornisce Python 3.12) e macOS. Docker/Podman sono facoltativi, non necessari sul server.

Preparazione una sola volta, dalla radice della repository:

```sh
# Solo se Python/venv non sono già disponibili su Ubuntu:
sudo apt-get update
sudo apt-get install python3 python3-venv

python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Non usare `sudo pip` né installare i pacchetti nel Python di sistema. `requirements.txt` fissa le versioni dirette e transitive. Font e licenza Bitstream Vera sono distribuiti da ReportLab: non servono font di sistema o download aggiuntivi durante la generazione.

Per ogni modifica, OpenClaw deve:

1. Leggere `AGENTS.md`, preferenze e piano corrente; rispettare conferme, budget e backup.
2. Aggiornare il piano, le decisioni e `mappe/attivita.json`. Per cambiare tappe, orari, prezzi o stati non serve toccare il codice.
3. Eseguire dalla radice:

```sh
.venv/bin/python strumenti/aggiorna.py
```

Il comando rigenera entrambi i file nella cartella `mappe/`. Funziona anche da altre directory usando il percorso assoluto dello script. Il PDF aggiunge pagine di continuazione quando servono; non tronca le tappe per mantenere una sola pagina al giorno.

4. Controllare HTML e PDF, inclusi link e impaginazione, e riassumere le modifiche all'utente. Per controllo visivo del PDF su Ubuntu si può usare `pdftoppm` del pacchetto `poppler-utils`; non è necessario per generarlo.
5. Commit e push richiedono l'autorizzazione esplicita per quella sequenza, secondo le regole Git dell'utente. La richiesta di modifica ricevuta via Telegram non va interpretata automaticamente come consenso al push.

Dopo il push autorizzato su `main`, GitHub Actions installa le stesse dipendenze in un ambiente virtuale e **rigenera entrambi i formati**, quindi pubblica il sito. Un PDF locale dimenticato non lascia online una versione vecchia rispetto al JSON. Controllare l'esito del workflow prima di dichiarare pubblicata la modifica; la CI non committa i file generati nel repository.

Nessun pacchetto da installare per l'HTML. Leaflet 1.9.4 e licenza sono inclusi. Lo schema e i testi funzionano offline; mappa stradale e navigazione richiedono rete. Dettagli in `mappe/LEGGIMI.md`.

La directory di pubblicazione esclude preferenze, backup e strumenti; la repository è comunque pubblica, quindi i file committati sono consultabili su GitHub.
