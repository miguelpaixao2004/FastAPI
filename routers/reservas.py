from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from models.reserva import ReservaInput, ReservaOutput

router = APIRouter()

# Banco de dados simulado
reservas_db = []

@router.post("/", response_model=ReservaOutput, status_code=201)
async def criar_reserva(reserva: ReservaInput):
    # Regra de Negócio: Evitar Overbooking
    for r in reservas_db:
        if r["mesa"] == reserva.mesa and r["data_hora"] == reserva.data_hora and r["status"] == "confirmada":
            raise HTTPException(
                status_code=400, 
                detail=f"A mesa {reserva.mesa} já está ocupada neste horário."
            )

    nova_reserva = {
        "id": len(reservas_db) + 1,
        "criada_em": datetime.now().isoformat(),
        "status": "confirmada",
        **reserva.model_dump()
    }
    reservas_db.append(nova_reserva)
    return nova_reserva

@router.get("/", response_model=List[ReservaOutput])
async def listar_reservas():
    return reservas_db

@router.delete("/{reserva_id}", status_code=204)
async def cancelar_reserva(reserva_id: int):
    for r in reservas_db:
        if r["id"] == reserva_id:
            r["status"] = "cancelada"
            return
    raise HTTPException(status_code=404, detail="Reserva não encontrada")