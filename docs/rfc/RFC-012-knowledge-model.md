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

