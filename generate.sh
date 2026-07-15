#!/usr/bin/env bash

set -e

ROOT="$(pwd)"

create_dirs() {
    mkdir -p \
        "$ROOT/docs/rfc" \
        "$ROOT/docs/milestones/M1" \
        "$ROOT/docs/milestones/M2" \
        "$ROOT/docs/milestones/M3" \
        "$ROOT/docs/milestones/M4" \
        "$ROOT/docs/milestones/M5" \
        "$ROOT/docs/milestones/M6" \
        "$ROOT/docs/milestones/M7"
}

write_file() {
    local file="$1"

    mkdir -p "$(dirname "$file")"

    cat > "$file"
}

write_roadmap() {

write_file "docs/ROADMAP.md" <<'EOF'
# Project Knowledge Engine (PKE)

## Roadmap

Versione documento: 1.0

---

# Visione

Project Knowledge Engine (PKE) è un motore locale di conoscenza del codice
progettato per fornire agli agenti AI una rappresentazione semantica,
strutturata e navigabile di un progetto software.

PKE non sostituisce il codice sorgente.

PKE crea un livello intermedio tra repository e AI:
Repository
|
|
PKE Knowledge Layer
|
|
AI Agent
---

# Obiettivi principali

- Ridurre il consumo di token durante lo sviluppo AI assisted.
- Fornire contesto preciso agli agenti.
- Mantenere una memoria strutturata del progetto.
- Analizzare automaticamente architettura, file e funzioni.
- Supportare più linguaggi tramite plugin.
- Essere indipendente dall'IDE.

---

# Architettura generale
             AI Agent

                |
                |

          Context Engine

                |

          Knowledge Graph

                |

          Semantic Database

                |

          Parser Plugins

                |

          Source Repository

---

# Milestone

## Fase 0 - Specifica

### M0.0.0 - RFC Foundation

Obiettivo:

Definire architettura, principi e contratti fondamentali.

Deliverable:

- RFC architetturali
- Modello dati
- Sistema plugin
- Storage
- API
- Formati conoscenza


---

# Fase 1 - Core Engine

## M1.0.0 - Core Framework

Obiettivo:

Creare il framework base.

Include:

- Plugin manager
- Event bus
- Scheduler
- Configurazione
- Logging
- CLI


## M1.1.0 - Repository Scanner

Include:

- Scanner filesystem
- Git integration
- Change detection
- File hashing


## M1.2.0 - Parser SDK

Include:

- API parser
- AST abstraction
- Symbol model


## M1.3.0 - Java Parser Plugin

Supporto:

- package
- classi
- metodi
- import
- dipendenze


## M1.4.0 - Storage Engine

Include:

- SQLite
- repository layer
- indice simboli


## M1.5.0 - Graph Engine

Include:

- dependency graph
- call graph
- package graph


## M1.6.0 - REST API


## M1.7.0 - CLI completa


---

# Fase 2 - Semantic Engine

## M2.0.0

AI Provider Framework


## M2.1.0

File Analyzer


## M2.2.0

Function Analyzer


## M2.3.0

Package Analyzer


## M2.4.0

Architecture Analyzer


## M2.5.0

Knowledge Database


## M2.6.0

Semantic Search


---

# Fase 3 - Context Engine

## M3.0.0

Context Builder


## M3.1.0

Impact Analyzer


## M3.2.0

Token Optimizer


## M3.3.0

Prompt Builder


## M3.4.0

Session Memory


---

# Fase 4 - AI Agents

## M4.0.0

Architecture Agent


## M4.1.0

Package Agent


## M4.2.0

File Agent


## M4.3.0

Function Agent


## M4.4.0

Dependency Agent


## M4.5.0

Context Agent


## M4.6.0

Documentation Agent


## M4.7.0

Decision Agent


---

# Fase 5 - IDE Integration

- Roo Code
- VSCode
- JetBrains
- Neovim
- Claude Code
- Cline


---

# Fase 6 - Collaboration

- Shared knowledge
- Decision history
- Architecture evolution


---

# Fase 7 - Enterprise

- Multi repository
- Distributed workers
- PostgreSQL
- Dashboard
- Authentication


---

# Release target

## PKE 1.0

Comprende:

- Core Engine
- Semantic Engine
- Context Engine
- AI Agents

A partire dalla versione 1.0 PKE è utilizzabile come backend AI per sviluppo software.

EOF

}

write_rfc001() {

write_file "docs/rfc/RFC-001-vision.md" <<'EOF'
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

EOF

}

write_rfc002() {

write_file "docs/rfc/RFC-002-domain-model.md" <<'EOF'
# RFC-002 - PKE Domain Model

Status: Draft

---

# Obiettivo

Definire il modello dati interno indipendente dal linguaggio.

---

# Entità principali

## Project

Rappresenta un repository.

Attributi:

- id
- name
- path
- git_branch
- git_commit


---

## File

Rappresenta un file sorgente.

Attributi:

- id
- path
- language
- hash


---

## Package

Contenitore logico di file.


---

## Symbol

Elemento dichiarato nel codice.

Tipologie:

- class
- interface
- enum
- function
- method
- field


---

## Dependency

Relazione tra elementi.

Esempi:

- import
- call
- inheritance
- composition


---

# Modello concettuale
Project
|
+-- Package
   |
   +-- File

          |
          +-- Symbol

                |
                +-- Dependency
                ---

# Requisiti

Il modello deve:

- essere estendibile;
- non dipendere da Tree-sitter;
- supportare più linguaggi.

EOF
}

write_rfc003() {

write_file "docs/rfc/RFC-003-plugin-system.md" <<'EOF'
# RFC-003 - Plugin System

Status: Draft

---

# Obiettivo

Definire il sistema di estensione di PKE.

---

# Principio

Il core non implementa parser specifici.

Ogni linguaggio è un plugin.

---

# Plugin Interface

Ogni plugin deve fornire:


language()

extensions()

parse()

extract_symbols()

extract_dependencies()


---

# Plugin lifecycle


Install

|

Load

|

Initialize

|

Execute

|

Unload


---

# Plugin esempio


plugins/

java/

python/

rust/

javascript/


---

# Requisiti

Un plugin non deve:

- accedere direttamente al database;
- modificare il core;
- dipendere da altri plugin.

EOF

}


write_rfc004() {

write_file "docs/rfc/RFC-004-event-bus.md" <<'EOF'
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

EOF

}

write_rfc005() {

write_file "docs/rfc/RFC-005-storage.md" <<'EOF'
# RFC-005 - Storage Architecture

Status: Draft

Version: 1.0

---

# Obiettivo

Definire il livello di persistenza della conoscenza PKE.

---

# Scelta iniziale

Database:

SQLite


Motivazioni:

- locale;
- zero configurazione;
- veloce;
- facilmente distribuibile.

---

# Principio Repository Pattern

Il codice applicativo non deve conoscere SQL.

Architettura:


Service

|

Repository

|

Database Adapter

|

SQLite


---

# Entità principali

## projects


id
name
path
branch
commit
created_at
updated_at



## files


id
project_id
path
language
hash
modified_at



## packages


id
project_id
name
path



## symbols


id
file_id
name
type
signature
line_start
line_end



## dependencies


id
source_id
target_id
type



## embeddings


id
entity_id
vector
model



---

# Strategie aggiornamento

PKE non rigenera tutto il database.

Flusso:


File modificato

   |

Calcolo hash

   |

Reparse file

   |

Aggiorna simboli

   |

Aggiorna grafo


---

# Migrazione database

Obbligatoria.

Formato:


migrations/

001_initial.sql

002_add_embeddings.sql


---

# Evoluzione futura

Supporto:

- PostgreSQL;
- database distribuiti;
- vector database.

EOF

}

write_rfc006() {

write_file "docs/rfc/RFC-006-api.md" <<'EOF'
# RFC-006 - API Architecture

Status: Draft

Version: 1.0

---

# Obiettivo

Definire l'interfaccia di accesso ai dati PKE.

---

# Tecnologia iniziale

FastAPI


---

# Endpoint progetto

## GET /projects

Lista progetti indicizzati.


## GET /projects/{id}

Dettaglio progetto.


---

# Endpoint file

## GET /files

Ricerca file.


Parametri:


language
package
path



## GET /files/{id}

Dettaglio file.


---

# Endpoint simboli

## GET /symbols


Ricerca:


name
type
language



---

# Endpoint dipendenze

## GET /graph


Restituisce:

- nodi;
- archi;
- relazioni.


---

# Endpoint analisi

## POST /scan

Avvia scansione.


## POST /reindex/{file}

Rigenera un singolo file.


---

# Endpoint AI futuri

## POST /context/build

Input:


task



Output:


context package



---

# Requisiti

L'API deve essere:

- locale;
- documentata OpenAPI;
- versionata.


Formato:


/api/v1/


EOF

}

write_rfc007() {

write_file "docs/rfc/RFC-007-ai-provider.md" <<'EOF'
# RFC-007 - AI Provider Architecture

Status: Draft

Version: 1.0

---

# Obiettivo

Definire il livello di astrazione per l'integrazione dei modelli AI.

---

# Principio

PKE non deve dipendere da un singolo provider.

Il sistema deve supportare:

- modelli locali;
- API cloud;
- modelli custom.

---

# Architettura

          AI Engine

              |

       AI Provider API

              |

+-------------+-------------+

|             |             |

Ollama OpenAI OpenRouter


---

# Provider Interface

Ogni provider deve implementare:

```python
class AIProvider:

    name()

    models()

    complete()

    embed()

    health()
Operazioni supportate
Completion

Generazione testo.

Utilizzo:

analisi file;
descrizione funzioni;
documentazione.
Embedding

Generazione vettori semantici.

Utilizzo:

ricerca;
similarità;
clustering.
Health Check

Verifica disponibilità modello.

Provider iniziali
Ollama

Supporto:

Qwen;
Llama;
Mistral.
OpenAI Compatible

Supporto API compatibili.

OpenRouter

Supporto modelli remoti.

Prompt Management

I prompt devono essere versionati.

Struttura:

prompts/

 architecture/

 package/

 file/

 function/

 context/
Cache

Le richieste AI devono essere cacheabili.

Chiave:

hash(input)+model+prompt_version
Requisiti

Il layer AI deve essere:

sostituibile;
testabile;
indipendente dal modello.

EOF

}



write_rfc008() {

write_file "docs/rfc/RFC-008-context-engine.md" <<'EOF'
# RFC-008 - Context Engine

Status: Draft

Version: 1.0

---

# Obiettivo

Definire il sistema che costruisce il contesto ottimizzato
da fornire agli agenti AI.

---

# Problema

Un repository può contenere:

- migliaia di file;
- milioni di righe;
- informazioni irrilevanti.

L'AI non deve ricevere tutto.

---

# Pipeline


User Task

|

Task Analyzer

|

Impact Analyzer

|

Knowledge Search

|

Context Builder

|

Optimized Prompt


---

# Livelli conoscenza

PKE utilizza una gerarchia:


Architecture

|

Package

|

File

|

Class

|

Function


---

# Context Selection

Il sistema deve selezionare:

- file direttamente coinvolti;
- dipendenze;
- chiamanti;
- chiamati;
- documentazione collegata.

---

# Token Budget

Il Context Engine deve conoscere:

- dimensione contesto;
- token disponibili;
- priorità informazioni.


Esempio:


Architecture 10%

Package 20%

Files 40%

Functions 30%


---

# Output

Il Context Builder produce:

```json
{
 "task": "",
 "files": [],
 "symbols": [],
 "dependencies": [],
 "summary": ""
}```
Evoluzione futura

Supporto:

agent planning;
automatic reasoning;
multi agent context.

EOF

}

write_rfc009() {

write_file "docs/rfc/RFC-009-knowledge-format.md" <<'EOF'
# RFC-009 - Knowledge Format

Status: Draft

Version: 1.0

---

# Obiettivo

Definire il formato della conoscenza generata da PKE.

---

# Principio

La conoscenza deve essere:

- leggibile dagli umani;
- leggibile dalle AI;
- versionabile con Git.

---

# Formati principali

## ARCHITECTURE.md

Descrive:

- struttura generale;
- componenti;
- flussi;
- decisioni.


---

## PACKAGE.md

Descrive:

- responsabilità package;
- file contenuti;
- dipendenze.


---

## FILE.md

Descrive:

- responsabilità file;
- classi;
- metodi;
- API.


---

## FUNCTION.md

Descrive:

- input;
- output;
- algoritmo;
- side effects.


---

# Metadata

Ogni documento deve contenere:

```yaml
---
pke_version: 1
generated_at:
source_hash:
model:
---
Aggiornamento

La documentazione non viene riscritta completamente.

Viene aggiornata solo quando:

cambia il codice;
cambia l'architettura;
cambia il modello AI.
Storage

La conoscenza può essere:

nel repository:
docs/pke/
nel database PKE.

EOF

}


write_rfc010() {

write_file "docs/rfc/RFC-010-versioning.md" <<'EOF'
# RFC-010 - Versioning Strategy

Status: Draft

Version: 1.0

---

# Obiettivo

Definire la strategia di compatibilità del progetto.

---

# Versioning principale

PKE utilizza Semantic Versioning:


MAJOR.MINOR.PATCH


---

# Core Version

Controlla:

- database;
- API;
- plugin interface;
- knowledge format.


---

# Plugin Version

Ogni plugin dichiara:

```yaml
name:
version:
pke_min_version:
languages:
RFC Version

Ogni RFC possiede:

RFC-ID
Version
Status

Stati:

Draft
Accepted
Deprecated
Replaced
Migrazione

Ogni modifica incompatibile richiede:

nuovo RFC;
migration;
periodo compatibilità.
Database

Schema versionato:

schema_version

migration_history
API

Le API sono versionate:

/api/v1/

/api/v2/
Obiettivo

Garantire che:

vecchi progetti siano leggibili;
plugin vecchi possano essere migrati;
agenti AI conoscano sempre il formato corretto.

EOF

}

write_m100() {

write_file "docs/milestones/M1/M1.0.0-core-framework.md" <<'EOF'
# M1.0.0 - Core Framework

Status: Planned

Version: 1.0

---

# Obiettivo

Realizzare il nucleo base di Project Knowledge Engine.

Al termine della milestone PKE deve essere in grado di:

- avviarsi;
- caricare configurazione;
- gestire plugin;
- emettere e ricevere eventi;
- eseguire task;
- esporre una CLI base;
- registrare informazioni di sistema.

---

# Scope

Incluso:

- struttura progetto Python;
- configurazione;
- logging;
- dependency injection;
- plugin manager;
- event bus;
- scheduler;
- CLI;
- test framework.

Escluso:

- parsing codice;
- database;
- AI;
- REST API.

---

# Struttura progetto

La struttura iniziale:


pke/

├── src/

│ └── pke/

│ ├── core/

│ │ ├── config/
│ │ ├── events/
│ │ ├── plugins/
│ │ ├── scheduler/
│ │ └── logging/

│ ├── cli/

│ ├── models/

│ └── services/

├── tests/

├── plugins/

├── docs/

├── pyproject.toml

└── README.md


---

# Componenti

## Config Manager

Responsabilità:

- caricare configurazione YAML;
- validare parametri;
- fornire accesso centralizzato.

Esempio:


pke.yaml


Contiene:

- progetto;
- database;
- plugin;
- logging.

---

# Logging System

Requisiti:

- livelli log;
- output console;
- output file;
- formato strutturato.

Livelli:

- DEBUG
- INFO
- WARNING
- ERROR


---

# Plugin Manager

Responsabilità:

- discovery plugin;
- caricamento;
- lifecycle.

Lifecycle:


DISCOVER

LOAD

INIT

START

STOP


---

# Event Bus

Implementazione iniziale:

- sincrona;
- memoria locale.

Interfaccia:

```python
publish(event)

subscribe(type, handler)
Scheduler

Responsabilità:

eseguire task;
gestire queue;
preparare future esecuzioni asincrone.
Dependency Injection

Il core non deve creare direttamente componenti.

Esempio:

Service

  riceve

Repository
CLI

Comando principale:

pke

Comandi iniziali:

pke version

pke doctor

pke config

pke plugin list
Doctor Command

Il comando deve verificare:

versione Python;
dipendenze installate;
configurazione;
directory progetto;
plugin caricabili.

Output:

PKE Doctor

Python       OK

Config       OK

Plugins      OK

Database     N/A
Modello configurazione

File:

pke.yaml

Esempio:

project:
  name: example
  path: .

logging:
  level: INFO

plugins:
  enabled: []
Test

La milestone è completata quando:

Core
PKE si avvia.
CLI
pke version funziona.
pke doctor funziona.
Plugin
un plugin demo viene caricato.
Event Bus
un evento viene pubblicato e ricevuto.
Config
YAML viene letto e validato.
Deliverable

Produrre:

repository Python funzionante;
CLI installabile;
plugin demo;
test automatici;
documentazione.
Dipendenze

RFC richiesti:

RFC-001 Vision
RFC-003 Plugin System
RFC-004 Event Bus
RFC-010 Versioning
Success criteria

M1.0.0 è completata quando il core PKE può essere installato
ed eseguito senza nessun parser o componente AI.

EOF

}

write_rfc011() {

write_file "docs/rfc/RFC-011-runtime-architecture.md" <<'EOF'
# RFC-011 - Runtime Architecture

Status: Accepted

Version: 1.0

---

# Obiettivo

Definire il runtime centrale di PKE.

Il Runtime è il componente responsabile del ciclo di vita
dell'applicazione e dei componenti interni.

---

# Motivazione

PKE sarà composto da molti moduli indipendenti:

- scanner;
- parser;
- storage;
- AI provider;
- knowledge generator;
- API.

Ogni componente deve poter essere caricato, avviato e fermato
senza creare dipendenze rigide.

---

# Architettura

             Runtime

                |

 +--------------+--------------+

 |              |              |

Service Event Bus Lifecycle

Container

                |

          Components

                |

           Plugins

---

# Runtime Responsibilities

Il Runtime gestisce:

- configurazione;
- servizi;
- eventi;
- componenti;
- lifecycle;
- stato applicazione.

Il Runtime non deve contenere logica di business.

---

# Component Model

Ogni componente PKE implementa:

```python
configure(runtime)

initialize()

start()

stop()

destroy()
Lifecycle

Gli stati possibili:

CREATED

 |

INITIALIZED

 |

STARTED

 |

STOPPING

 |

STOPPED
Service Container

Il Runtime espone un container per la gestione dei servizi.

API:

register()

resolve()

exists()

unregister()
Event Bus

Tutti i componenti comunicano tramite eventi.

API:

publish(event)

subscribe(type, handler)

unsubscribe(type, handler)
Component Registry

Il Runtime mantiene il registro dei componenti attivi.

Utilizzato per:

discovery;
lifecycle;
diagnostica.
Bootstrap

L'avvio segue questo ordine:

Load Configuration

        |

Initialize Logging

        |

Create Runtime

        |

Register Services

        |

Load Plugins

        |

Start Components
Principi architetturali
Nessun singleton globale

Tutti i servizi passano dal Runtime.

Nessuna dipendenza concreta

I componenti devono dipendere da interfacce.

Estensibilità

Nuovi moduli devono essere aggiungibili come componenti.

Evoluzioni future

Possibili estensioni:

runtime distribuito;
componenti remoti;
hot reload;
dependency graph;
startup parallelo.

EOF

}

write_rfc012() {

write_file "docs/rfc/RFC-012-knowledge-model.md" <<'EOF'
# RFC-012 - Knowledge Model

Status: Draft

Version: 1.0

---

# Obiettivo

Definire il modello dati comune utilizzato da tutti i componenti
di analisi del codice.

---

# Principio

Il Knowledge Model è indipendente dal linguaggio.

Un parser Java, Python o Rust deve produrre lo stesso modello.

---

# Pipeline


Source Code

 |

Language Plugin

 |

Knowledge Model

 |

Knowledge Producers

 |

Knowledge Storage


---

# Entità principali

## Project

Rappresenta un progetto software.

Campi:


id

name

path

language

version


---

## Package

Rappresenta un contenitore logico.

Esempio:


com.company.service


Campi:


id

name

path

description

files[]


---

## File

Rappresenta un file sorgente.

Campi:


id

path

language

hash

package

imports[]


---

## Symbol

Entità generica del codice.

Tipi:


CLASS

FUNCTION

METHOD

VARIABLE

CONSTANT


Campi:


name

type

visibility

location

documentation


---

## Class

Campi:


name

package

extends

implements

methods[]

fields[]


---

## Function / Method

Campi:


name

signature

parameters[]

return_type

visibility

complexity

calls[]

called_by[]


---

## Parameter

Campi:


name

type

default_value


---

## Dependency

Rappresenta una relazione.

Tipi:


IMPORT

CALL

EXTEND

IMPLEMENT

REFERENCE


---

# Knowledge Graph

Il modello viene rappresentato come un grafo.

Esempio:


Package

|

contains

|

File

|

contains

|

Class

|

contains

|

Method


---

# Relazioni

Principali:


Project
|
+-- Package
|
+-- File
|
+-- Symbol

Symbol
|
+-- calls
|
+-- depends_on


---

# Language Independence

I plugin linguaggio devono trasformare:


AST specifico


in:


Knowledge Model


---

# Knowledge Producer

I producer generano rappresentazioni diverse.

Esempi:


Knowledge Model

   |

   +--> PACKAGE.md

   +--> FILE.md

   +--> FUNCTION.md

   +--> Embeddings

   +--> Context

---

# Versioning

Il modello deve essere versionato.

Esempio:

```yaml
knowledge_schema: 1

Modifiche incompatibili richiedono:

nuovo schema;
migration;
RFC.
Obiettivi futuri

Il Knowledge Model permetterà:

ricerca semantica;
generazione automatica documentazione;
context building;
AI coding assistant.

EOF

}

main() {
    
    create_dirs

    write_roadmap

    write_rfc001
    write_rfc002
    write_rfc003
    write_rfc004
    write_rfc005
    write_rfc006
    write_rfc007
    write_rfc008
    write_rfc009
    write_rfc010
    write_rfc011
    write_rfc012

    echo "PKE M0 documentation generated."
}

main "$@"