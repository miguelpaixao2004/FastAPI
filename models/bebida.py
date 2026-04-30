from pydantic import BaseModel, Field

class BebidaInput(BaseModel):
    nome: str = Field(min_length=2)
    preco: float = Field(gt=0)
    alcoolica: bool

class BebidaOutput(BaseModel):
    id: int
    nome: str
    preco: float
    alcoolica: bool