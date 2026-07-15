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

