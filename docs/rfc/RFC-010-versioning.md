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

