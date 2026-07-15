# RFC-004 - Event Bus Architecture

Status: Draft

Version: 1.0

---

# Obiettivo

Definire il sistema di comunicazione interno tra componenti PKE.

---

# Motivazione

I componenti PKE devono essere disaccoppiati.

Un modulo non deve conoscere l'implementazione degli altri moduli.

Il sistema deve comunicare attraverso eventi.

---

# Architettura

            Event Bus

                |

+---------------+---------------+

|               |               |

Scanner Parser Storage

|               |               |

FileChanged SymbolFound DataUpdated


---

# Eventi principali

## ProjectInitialized

Generato quando un progetto viene caricato.


## FileCreated

Nuovo file individuato.


Payload:


path
language
hash



## FileModified

File modificato.


Payload:


path
old_hash
new_hash



## FileDeleted

File rimosso.


## SymbolsExtracted

Il parser ha terminato l'analisi.


Payload:


file
symbols[]



## DependenciesExtracted

Sono state trovate nuove dipendenze.


---

# API concettuale

```python
event_bus.publish(event)

event_bus.subscribe(
    event_type,
    handler
)
Requisiti

L'Event Bus deve:

essere asincrono;
supportare code;
permettere retry;
permettere logging degli eventi.
Implementazione iniziale

Versione M1:

event bus in memoria;
code locali;
esecuzione single process.

Evoluzioni future:

Redis;
RabbitMQ;
Kafka.

