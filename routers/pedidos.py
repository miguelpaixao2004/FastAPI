from fastapi import APIRouter
from typing import List
from datetime import datetime
from models.pedido import PedidoInput, PedidoOutput

router = APIRouter()
pedidos = []

@router.post("/", response_model=PedidoOutput, status_code=201)
async def criar_pedido(pedido: PedidoInput):
    novo_pedido = {
        "id": len(pedidos) + 1,
        "data_hora": datetime.now().isoformat(),
        **pedido.model_dump(),
        "status": "recebido"
    }
    pedidos.append(novo_pedido)
    return novo_pedido

@router.get("/", response_model=List[PedidoOutput])
async def listar_pedidos():
    return pedidos
