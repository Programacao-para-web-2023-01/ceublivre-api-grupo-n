# CeubLivre-API

## Interações

Este microsserviço gerencia as avaliações e comentários deixados pelos usuários sobre os produtos comprados, assim como
perguntas e repostas.


### #2 - Gerenciamento de comentários (2 pontos)

Permitir que os usuários possam comentar nas avaliações de outros usuários.

---

Necessidades: identificar comentário que vai receber a resposta, identificar usuário dono da resposta, resposta em si com limite de caracteres(?), data e hora da resposta

---

```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

import os
import requests

load_dotenv()
from deta import Deta  # Import Deta

deta = Deta(os.environ["PROJECT_KEY"])

db = deta.Base("interacoes")

app = FastAPI()


class Resposta(BaseModel):
    usuario: str
    corpo: str
    data: str


@app.get("/comentarios")
async def get_comentarios():
    res = db.fetch()
    all_items = res.items

    # fetch until last is 'None'
    while res.last:
        res = db.fetch(last=res.last)
        all_items += res.items

    return all_items

@app.post("/comentarios/resposta")
async def create_resposta(resposta: Resposta):
    new_reply = db.insert(resposta.dict())

    return new_resposta


@app.delete("/resposta/{id}")
async def delete_resposta(id: str):
    db.delete(id)

    return {"detail": "Resposta deletada com sucesso."}

```
