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

