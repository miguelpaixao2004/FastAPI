from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ReservaInput(BaseModel):
    mesa: int = Field(ge=1, le=20, description="Número da mesa de 1 a 20")
    nome_cliente: str = Field(min_length=2, max_length=100)
    data_hora: datetime
    quantidade_pessoas: int = Field(ge=1, le=10)

class ReservaOutput(BaseModel):
    id: int
    mesa: int
    nome_cliente: str
    data_hora: datetime
    quantidade_pessoas: int
    status: str # Ex: "confirmada", "cancelada"
    criada_em: str