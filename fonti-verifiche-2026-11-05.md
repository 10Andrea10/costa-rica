# Fonti e verifiche - 5 novembre 2026

Ricerca per il nuovo piano in auto. Prezzi pubblicati, non preventivi né posti confermati. Nessuna telefonata, prenotazione o messaggio ad operatori effettuati.

| Fonte | Risultato utile | Limite |
|---|---|---|
| [SINAC Irazú](https://www.sinac.go.cr/ES/ac/accvc/pnvi/Paginas/default.aspx) | US$16,95 IVA inclusa, 08:00-16:00, ultimo ingresso Cráteres 14:00; online SINAC; parcheggio auto CRC 2.500 | Reperito da ricerca indicizzata; apertura diretta andata in timeout; nessuno slot verificato |
| [SINAC Braulio Carrillo](https://www.sinac.go.cr/ES/ac/accvc/pnbc/Paginas/default.aspx/) | US$13,56 IVA inclusa; 08:00-15:30; settori Quebrada González e Barva distinti | Apertura operativa, sentieri e condizioni Ruta 32 del giorno non verificati |
| [SINAC modalità biglietti](https://www.sinac.go.cr/ES/servlin/Paginas/default.aspx) | Elenco SICORE include Irazú Cráteres/Prusia e Braulio Barva | Non equivale a disponibilità o modalità identica per Quebrada González |
| [ADIFORT cascata](https://www.cataratalafortuna.com/la-fortuna-waterfall-hike) e [FAQ](https://www.cataratalafortuna.com/es/faq) | Autoguidata, circa 530 gradini, parcheggio gratuito; US$20 stranieri; 07:00-17:00, ingresso raccomandato entro 16:00 | Bagno e apertura effettiva da controllare al momento |
| [SINAC Arenal](https://www.sinac.go.cr/ES/ac/acahn/pnva/Paginas/default.aspx) | Testo ufficiale indicizzato riconfermato oggi: US$16,95 IVA inclusa e 08:00-16:00 | Apertura diretta in timeout; nessuna verifica operativa o posto garantito |
| [Mistico autonomo](https://misticopark.com/tours/self-guided-hanging-bridges/) | 3,2 km, sei ponti sospesi, circa 2 ore; da US$32 + tasse AM / US$28 + tasse PM | Prezzi iniziali, totale adulto e turno del 6 non verificati |
| [Mistico guidato](https://misticopark.com/tours/natural-history-walk/) | Da US$44 + tasse; circa 2,5 ore, ingresso + guida | Nessuna disponibilità verificata; non include automaticamente trasporto |
| [Don Olivo sito principale](https://donolivochocolatetour.net/) | US$30/adulto; sito specifica US$33,90 con carta; circa 2h; 08/10/13/15; arrivo 15 minuti prima, pagamento sul posto | Calendario non accessibile, nessun posto confermato per il 7; verificare totale di pagamento |
| [Kayak Paradise](https://kayakparadiseandtours.com/) | Per persona: US$25/1h, US$35/2h, US$40/3h; istruzioni e attrezzatura; politiche senza rimborso | Tasse, giubbotto, assistenza, fascia e condizioni del 7 da confermare |
| [Del Toro prezzi](https://www.catarata-del-toro.com/prices/) | US$15 cascata, US$20 Blue Falls, US$25 combo; parcheggio incluso; acquisto sul posto, no prenotazione | Accesso e condizioni acqua del giorno non verificati; domenica chiuso |
| [Del Toro accesso](https://www.catarata-del-toro.com/how-to-reach-us/) | Gestore indica strade asfaltate e nessun obbligo 4x4; ingresso via Bajos del Toro | Non prova fondo stradale attuale; preferire fonte del gestore rispetto a vecchie guide che raccomandano 4x4 |
| [Blue Falls avviso](https://www.catarata-del-toro.com/ticket/blue-falls-of-costa-rica/) | Ancora presente avviso ponte Las Gemelas dopo piogge agosto 2026 | Nessuna prova di ripristino, verificare direttamente se si sceglie |
| [Mytanfeet SJO-La Fortuna](https://mytanfeet.com/costa-rica-travel-tips/driving-san-jose-la-fortuna/comment-page-1/) | Confronto strada diretta, La Paz e Del Toro; trasferimento diretto circa 2,5-3h senza soste/traffico | Per il piano adottati margini più ampi; guida non è bollettino stradale live |
| [IMN 5 novembre](https://imn.ac.cr/es/web/imn/reporte-pronostico-regional) | Bollettino valido giovedì 5; rovesci pomeridiani possibili; tramonto San José 17:12 | Previsione regionale, non punto esatto né garanzia per 6-12 |

## Plugin richiesti: esito effettivo
- Klook: chiamata eseguita per Irazú, Braulio Carrillo, natura e trekking 5-12 novembre; primo risultato vuoto (`NO_EXACT_MATCH`). Non è prova di indisponibilità dell'attrazione né esaurimento biglietti.
- GetYourGuide: chiamata eseguita per lo stesso viaggio; errore `Cannot read properties of undefined (reading 'toLowerCase')`. Nessun prodotto o disponibilità confermato.
- Gli operatori ufficiali e SINAC restano la fonte utile per ingressi autonomi; non fingere risultati del plugin quando si usa il web.

## Mappe e artefatti
- Leaflet 1.9.4, ultima versione stabile indicata dal registro npm; 2.0.0-beta.1 è una beta. Versione esplicitamente fissata, nessuna installazione npm. [Registro ufficiale](https://registry.npmjs.org/leaflet/latest), [istruzioni ufficiali](https://leafletjs.com/install.html).
- HTML: libreria incorporata, basemap OpenStreetMap via rete, schema geografico offline sempre disponibile; nessuna posizione dell'utente richiesta. Non è navigazione turn-by-turn e non contiene traffico live.
- Coordinate orientative per visualizzazione, non tutte verificate come ingresso/parcheggio. Navigazione tramite ricerca del nome della struttura su Google Maps; Don Olivo senza pin finché non verificato. Per Del Toro punto d'interesse [OSM/Mapcarta](https://mapcarta.com/es/N1156198839), non coordinate della cascata da usare per la guida.
- PDF: generazione e rendering con framework di sistema macOS (CoreGraphics/CoreText/PDFKit) per non installare pacchetti; Podman non accessibile dal sandbox, nessuna VM avviata o modificata. Cache/build solo temporanei. Nessun volume Podman creato.
- Browser di controllo non disponibile (`browser access host unavailable`): verificare HTML con controlli statici e interazioni DOM simulate, dichiarando il limite; PDF da rendere e ispezionare visivamente prima della consegna.

## Backup intatti
SHA-256 al primo controllo del nuovo ciclo:
- `costa-rica-4-11-novembre-2026.md`: `7cb2b46d9aff4dc35046e6916ce731ff28c06e4962c1ad576fa43675375fa8f9`
- `handoff-costa-rica-2026-nuova-chat.md`: `dd647c34e13179e749eff4802423c95e313b798b6a96ccf1880cd4156154acfc`

## Revisione del 5: soste gratuite e GitHub Pages
- Fonte primaria delle nuove preferenze: utente in chat. Anche US$20 per la cascata sono rifiutati oggi; chiedere prima di fissare attività costose. Accettato arrivo in ostello dopo il buio o check-in e nuova uscita. Queste dichiarazioni supersedono le precedenti alternative a pagamento del 5 e l'obiettivo di arrivo prima delle 17.
- Proposta SJO → Grecia → Sarchí → Zarcero → La Fortuna, con passeggiate nei luoghi pubblici. Non un trekking di foresta. Orari stimati, non navigazione/traffico live; accesso operativo e limite check-in non verificati.
- ICT / Visit Costa Rica menziona Sarchí e Zarcero lungo il viaggio San José-La Fortuna: https://www.visitcostarica.com/sites/default/files/2024-10/INGLES_FORTUNA.pdf
- Municipio Sarchí, carro nel parco centrale: https://www.munisarchi.go.cr/articulo/17/carreta%2C-simbolo-de-trabajo
- Riscontro sulle cinque soste gratuite nei tre paesi: https://costaricatravelblog.com/grecia-sarchi-zarcero-costa-rica/
- Laboratorio Eloy Alfaro: il municipio riporta parcheggio gratuito e orari, ma non prova tour gratuito; nessuna visita guidata inclusa automaticamente: https://www.munisarchi.go.cr/Store/store/40/fabrica-de-carretas-eloy-alfaro
- Repo verificata tramite connettore GitHub: pubblica, branch predefinito main, Pages abilitato. Il connettore non supporta l'endpoint Pages; fallback CLI `gh api repos/10Andrea10/costa-rica/pages` in sola lettura: build_type=workflow, URL https://10andrea10.github.io/costa-rica/. Nessuna impostazione remota modificata.
- Workflow locale: rigenera HTML, pubblica soltanto HTML/PDF e .nojekyll; PDF rigenerato localmente prima del push. Nessun commit, push o deploy eseguito dall'assistente.
- Versioni Actions stabili verificate dalle release ufficiali: checkout v7.0.1, configure-pages v6.0.0, upload-pages-artifact v5.0.0, deploy-pages v5.0.1. Link alle release in README.md. Documentazione ufficiale: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- Storico Basic Memory non raggiungibile in questa sessione (Transport closed su recent_activity e search_notes). Preferenze e decisioni mantenute nei file locali.

### Verifica locale dopo la revisione
- YAML del workflow analizzato con Psych e comandi run verificati con bash -n; nessun errore.
- Build locale equivalente allo staging CI: solo index.html, PDF e .nojekyll. Nessun deploy eseguito: validazione end-to-end Actions ancora da effettuare dopo il push.
- JavaScript eseguito in Node VM con DOM simulato: sei schede, selezione iniziale del 5, cambio giorno, schema, fallback senza Leaflet e collegamenti Google Maps/PDF verificati. Non è un test in browser reale.
- PDF rigenerato: sei pagine, controllo estrazione testo e margini superati; PNG e foglio di contatto ispezionati. Il primo tentativo segnalava troppo contenuto sul 5: accorpata la cena alla scheda ostello, poi rigenerato con esito positivo.
- Uso nativo di Python/Node/Ruby e binario Swift già disponibile, senza installare pacchetti. Intermedi e cache di verifica in /private/tmp; nessun volume Podman creato. Podman non accessibile in questo ambiente come già verificato nella precedente generazione.
- git diff --check superato. Il vecchio Markdown risulta già modificato dall'utente rispetto al commit init: non modificato né ripristinato dall'assistente.

## Conferma successiva dell’utente
- Risposta alla scelta iterativa: «Tre paesi e La Fortuna». Confermato il giro del 5, mantenuti orari stimati ed El Salto facoltativo. Aggiornati registro, piano, lista idee, dati mappa e guida; HTML/PDF rigenerati. Nessuna nuova ricerca necessaria per registrare questa decisione. Giorni successivi e relative spese restano da approvare.

## Portabilità Linux / OpenClaw - 5 novembre 2026
Questa revisione supersede la generazione Swift/macOS e le precedenti indicazioni secondo cui la CI copiava soltanto il PDF già presente.
- Richiesta utente: aggiornamenti futuri tramite OpenClaw via Telegram su server Linux di base; scelta implementata: Python per entrambi i formati, senza Docker obbligatorio.
- Rimosso `strumenti/genera-pdf.swift`; aggiunti `strumenti/genera-pdf.py`, `strumenti/aggiorna.py` e `requirements.txt`. Percorsi risolti rispetto agli script, non alla directory corrente. PDF con font Vera inclusi in ReportLab e pagine di continuazione automatiche. Scrittura del PDF tramite file temporaneo e sostituzione solo a generazione completata.
- Requisito Python 3.11+ (dovuto a Pillow 13). Ubuntu 24.04 con Python 3.12 compatibile con i requisiti pubblicati; non testato su un host Ubuntu reale in questa sessione.
- Versioni stabili verificate sul registro ufficiale PyPI il 5 novembre: reportlab 5.1.0, pillow 13.0.0, charset-normalizer 3.5.2; tutte fissate, incluse dipendenze transitive obbligatorie. Per i controlli temporanei usato pypdf 6.21.4, non richiesto in produzione.
- Fonti versioni e requisiti: https://pypi.org/pypi/reportlab/json ; https://pypi.org/pypi/pillow/json ; https://pypi.org/pypi/charset-normalizer/json ; https://pypi.org/pypi/pypdf/json
- Test eseguito con Podman dopo l'avvio da parte dell'utente, su container Linux Python ufficiale `3.14.6-slim-bookworm`, digest `sha256:4c92ffcde4dd6f1ff72a24518f49fd4990b27134987dfa31a733badde66df9f8`, verificato tramite https://hub.docker.com/v2/repositories/library/python/tags/3.14.6-slim-bookworm . Repository montata in sola lettura, copia di test in /tmp del container, dipendenze in venv. Container rimossi con --rm, nessun volume nominato creato.
- Generazione Linux eseguita anche da directory diversa dalla repository. HTML e PDF identici byte per byte alla generazione macOS. PDF finale 6 pagine: titoli e tutte le tappe estratti, 19 link Google Maps verificati contro il JSON. Dodici tappe aggiuntive solo nei dati di prova producono 8 pagine, tutte presenti senza perdita di contenuto.
- Sei pagine renderizzate e ispezionate visivamente; corretti i caratteri freccia non presenti nel font sostituendoli nel PDF con simboli ASCII/NORD. La verifica grafica locale usa strumenti temporanei Apple soltanto come lettore, non come parte della generazione o del progetto.
- Aggiornati README, guida mappe, AGENTS e preferenze per OpenClaw. CI crea venv, installa requirements e rigenera entrambi i formati prima del deploy. YAML e shell del workflow verificati, controllo HTML e git diff --check superati. Nessun nuovo workflow remoto eseguito, commit o push effettuato dall'assistente.
