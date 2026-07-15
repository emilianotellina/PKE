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


