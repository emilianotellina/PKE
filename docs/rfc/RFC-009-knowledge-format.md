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

