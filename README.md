# CeubLivre-API

## Interações

Este microsserviço gerencia as avaliações e comentários deixados pelos usuários sobre os produtos comprados, assim como
perguntas e repostas.

### #1 - Gerenciamento de avaliações (2 pontos)

Permitir que os usuários possam avaliar os produtos comprados e deixar uma nota ou estrela e um comentário sobre sua
experiência.

* Permitir avaliações com foto (1 ponto)

---

Necessidades: nome do usuário, número do comentário, data e hora nos quais o comentário foi realizado, estrelas (de 0 à 5) dos produtos, upvote/downvote(?).

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


class Comentario(BaseModel):
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


@app.get("/comentarios/{id}")
async def get_comentarios_by_id(id: str):
    comentario = db.get(id)

    if comentario:
        return comentario

    raise HTTPException(status_code=404, detail="Comentário não encontrado.")


@app.post("/comentarios")
async def create_comentario(comentario: Comentario):
    new_comentario = db.insert(comentario.dict())

    return new_comentario


@app.put("/comentario/{id}")
async def update_comentario(id: str, comentario: Comentario):
    db.update(comentario.dict(), id)

    return comentario


@app.delete("/comentario/{id}")
async def delete_comentario(id: str):
    db.delete(id)

    return {"detail": "Comentário deletado com sucesso."}
```
