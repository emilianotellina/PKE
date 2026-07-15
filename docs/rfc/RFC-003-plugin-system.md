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

