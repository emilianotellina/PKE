# RFC-011 - Runtime Architecture

Status: Accepted

Version: 1.0

---

# Obiettivo

Definire il runtime centrale di PKE.

Il Runtime è il componente responsabile del ciclo di vita
dell'applicazione e dei componenti interni.

---

# Motivazione

PKE sarà composto da molti moduli indipendenti:

- scanner;
- parser;
- storage;
- AI provider;
- knowledge generator;
- API.

Ogni componente deve poter essere caricato, avviato e fermato
senza creare dipendenze rigide.

---

# Architettura

             Runtime

                |

 +--------------+--------------+

 |              |              |

Service Event Bus Lifecycle

Container

                |

          Components

                |

           Plugins

---

# Runtime Responsibilities

Il Runtime gestisce:

- configurazione;
- servizi;
- eventi;
- componenti;
- lifecycle;
- stato applicazione.

Il Runtime non deve contenere logica di business.

---

# Component Model

Ogni componente PKE implementa:

```python
configure(runtime)

initialize()

start()

stop()

destroy()
Lifecycle

Gli stati possibili:

CREATED

 |

INITIALIZED

 |

STARTED

 |

STOPPING

 |

STOPPED
Service Container

Il Runtime espone un container per la gestione dei servizi.

API:

register()

resolve()

exists()

unregister()
Event Bus

Tutti i componenti comunicano tramite eventi.

API:

publish(event)

subscribe(type, handler)

unsubscribe(type, handler)
Component Registry

Il Runtime mantiene il registro dei componenti attivi.

Utilizzato per:

discovery;
lifecycle;
diagnostica.
Bootstrap

L'avvio segue questo ordine:

Load Configuration

        |

Initialize Logging

        |

Create Runtime

        |

Register Services

        |

Load Plugins

        |

Start Components
Principi architetturali
Nessun singleton globale

Tutti i servizi passano dal Runtime.

Nessuna dipendenza concreta

I componenti devono dipendere da interfacce.

Estensibilità

Nuovi moduli devono essere aggiungibili come componenti.

Evoluzioni future

Possibili estensioni:

runtime distribuito;
componenti remoti;
hot reload;
dependency graph;
startup parallelo.

