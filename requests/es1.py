import requests as req

res= req.get("http://www.example.com")

try:
    with open("response.txt","w") as f:
        f.write(str(res.status_code))
except FileNotFoundError:
    print("File non trovato")


roba={
    "userId":"123",
    "title":"ciao!",
    "completed":True
}

res=req.post("http://jsonplaceholder.typicode.com/todos",roba)

req.delete(f"http://jsonplaceholder.typicode.com/todos/{str(res.json()["id"])}")
