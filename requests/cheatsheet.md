## 1. Metodi Principali (Verbi HTTP)

Tutti questi metodi accettano un URL e restituiscono un oggetto **Response**.

| Metodo | Utilizzo Tipico | Esempio Sintassi |
| --- | --- | --- |
| **GET** | Recuperare dati | `requests.get(url)` |
| **POST** | Inviare/Creare dati | `requests.post(url, data=dict)` |
| **PUT** | Aggiornare dati (integrale) | `requests.put(url, data=dict)` |
| **PATCH** | Modificare dati (parziale) | `requests.patch(url, data=dict)` |
| **DELETE** | Eliminare dati | `requests.delete(url)` |
| **HEAD** | Leggere solo gli header | `requests.head(url)` |

---

## 2. Gestione della Risposta (`Response`)

Quando esegui `res = requests.get(url)`, l'oggetto `res` contiene tutto ciò che serve:

* **`res.status_code`**: Il codice di stato HTTP (es. 200, 404).
* **`res.text`**: Il contenuto della risposta come stringa (decodificato automaticamente).
* **`res.json()`**: Metodo che trasforma un corpo JSON direttamente in un dizionario/lista Python.
* **`res.content`**: Il contenuto in formato binario (utile per immagini o PDF).
* **`res.headers`**: Un dizionario con gli header della risposta.
* **`res.ok`**: Ritorna `True` se lo status code è tra 200 e 299.

---

## 3. Invio di Parametri e Dati

### Query Parameters (URL)

Per aggiungere `?chiave=valore` all'URL:

```python
params = {'q': 'python', 'page': 2}
res = requests.get('https://api.example.com/search', params=params)

```

### Body Data (Form o JSON)

* **Form data**: Usa `data` (invia come `application/x-www-form-urlencoded`).
* **JSON data**: Usa `json` (imposta automaticamente l'header su `application/json`).

```python
payload = {'username': 'admin', 'password': '123'}

# Come Form
res = requests.post(url, data=payload)

# Come JSON
res = requests.post(url, json=payload)

```

---

## 5. Header e Autenticazione

Personalizzare l'invio per simulare browser o passare token:

```python
headers = {'User-Agent': 'MioApp/1.0', 'Authorization': 'Bearer TOKEN'}
res = requests.get(url, headers=headers)

```

**Autenticazione Base:**

```python
from requests.auth import HTTPBasicAuth
res = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))
# Oppure più semplicemente:
res = requests.get(url, auth=('user', 'pass'))

```

---

## 6. Timeout e Controllo Errori

È buona pratica impostare sempre un **timeout** per evitare che il programma resti appeso all'infinito.

```python
try:
    res = requests.get(url, timeout=5) # secondi
    res.raise_for_status() # Solleva un'eccezione se lo status è 4xx o 5xx
except requests.exceptions.HTTPError as err:
    print(f"Errore HTTP: {err}")
except requests.exceptions.ConnectionError:
    print("Errore di connessione")
except requests.exceptions.Timeout:
    print("La richiesta è andata in timeout")

```

---

## 7. Sessioni

Usa `requests.Session()` per mantenere i cookie tra più richieste (es. dopo un login) e migliorare le performance.

```python
with requests.Session() as s:
    s.get('https://example.com/login')
    res = s.get('https://example.com/dashboard') # Mantiene i cookie del login

```