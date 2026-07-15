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

