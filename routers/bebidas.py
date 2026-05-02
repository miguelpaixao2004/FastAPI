from fastapi import APIRouter
from typing import List
from models.bebida import BebidaInput, BebidaOutput

router = APIRouter()

bebidas = [
    {"id": 1, "nome": "Vinho Chianti Classico", "preco": 85.0, "alcoolica": True},
    {"id": 2, "nome": "Água com Gás", "preco": 6.5, "alcoolica": False},
]

@router.get("/", response_model=List[BebidaOutput])
async def listar_bebidas():
    return bebidas

@router.post("/", response_model=BebidaOutput, status_code=201)
async def adicionar_bebida(bebida: BebidaInput):
    nova = {"id": len(bebidas) + 1, **bebida.model_dump()}
    bebidas.append(nova)
    return nova