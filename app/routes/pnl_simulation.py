from fastapi import APIRouter
from app.models.pnl_simulation import PnLSimulationInput, PnLSimulationOutput

router = APIRouter()

@router.post("/simulate", response_model=PnLSimulationOutput)
def simulate_pnl(input_data: PnLSimulationInput):
    # Mock de lógica: substituir por cálculos mais precisos
    pnl_with_hedge = sum(input_data.historical_prices) * 0.9  # Exemplo de lógica de hedge
    pnl_without_hedge = sum(input_data.historical_prices)
    average_diff = pnl_without_hedge - pnl_with_hedge
    
    return PnLSimulationOutput(
        pnl_with_hedge=pnl_with_hedge,
        pnl_without_hedge=pnl_without_hedge,
        protection_summary="90% de proteção atingida.",
        average_difference=average_diff
    )
