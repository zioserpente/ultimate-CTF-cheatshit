import requests as req
import base64
lista=[200,201,400,402,401,404,403,300]
#res= req.get("http://httpmemes.com/codice.jpg")

for i in range(0, len(lista)):
    res=req.get(f"http://httpmemes.com/{lista[i]}.jpg")
    if(res.status_code==200):
        try:
            with open(f"{lista[i]}.jpg","wb") as f:
                f.write(res.content)
                print(f"Salvato {lista[i]}.jpg")
        except Exception as e:
            print(f"C'è stato un errore con {lista[i]}: {e}")
    else:
        print("!200")