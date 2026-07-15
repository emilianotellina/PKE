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

