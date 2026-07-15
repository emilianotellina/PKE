# RFC-001 - PKE Vision

Status: Draft

Version: 1.0

---

# Obiettivo

Definire la visione generale di Project Knowledge Engine.

PKE nasce per creare un livello di conoscenza strutturata tra
repository software e agenti AI.

---

# Problema

Gli agenti AI hanno tre problemi principali:

- contesto limitato;
- difficoltà nel comprendere architetture complesse;
- elevato consumo di token.

PKE risolve questi problemi costruendo una rappresentazione
semantica del progetto.

---

# Principi

## Local first

Il sistema deve funzionare completamente in locale.

Supporto:

- Ollama
- modelli locali
- database locali


## Incrementale

Le modifiche devono aggiornare solamente gli elementi coinvolti.


## Linguaggio indipendente

Il core non deve conoscere linguaggi specifici.


## Estendibile

Ogni nuova funzionalità deve poter essere aggiunta tramite plugin.


---

# Obiettivo finale

PKE deve permettere ad un agente AI di:

- comprendere un progetto;
- modificare codice;
- mantenere coerenza architetturale;
- ricordare decisioni progettuali.

