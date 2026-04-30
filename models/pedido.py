from pydantic import BaseModel, Field
from typing import List

class ItemPedido(BaseModel):
    prato_id: int
    quantidade: int = Field(ge=1)

class PedidoInput(BaseModel):
    mesa: int = Field(ge=1, le=20)
    itens: List[ItemPedido]

class PedidoOutput(BaseModel):
    id: int
    data_hora: str
    mesa: int
    itens: List[ItemPedido]
    status: str