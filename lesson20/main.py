from fastapi import FastAPI


app= FastAPI()

@app.get("/")

def root():
    return {
  "name":"Alice",
  "age":35,
  "adress":{
    "street":"pashkovasa",
    "city":"prishtine",
    "country":"Kosove"
  },
  "contacts": [
    {
      "type": "email",
      "value": "nili@gmail.com"
    },
    {
      "type": "phone",
      "value": "111-222-333"
    }
  ]
}


@app.get("/users/")
def read_root():
    return {
        "message":"hello there"
    }