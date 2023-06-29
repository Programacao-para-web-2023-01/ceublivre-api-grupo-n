from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

import os
import requests

load_dotenv()
from deta import Deta  # Import Deta

deta = Deta(os.environ["e07Q4nfCBj22_vpm4egCYGPYkvQ2TD587C26ZsmuznHeM"])

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

@app.post("/comentarios/{id}/resposta")
async def create_resposta(resposta: Resposta):
    new_reply = db.insert(resposta.dict())

    return new_resposta


@app.delete("/resposta/{id}")
async def delete_resposta(id: str):
    db.delete(id)

    return {"detail": "Resposta deletada com sucesso."}