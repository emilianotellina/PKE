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

