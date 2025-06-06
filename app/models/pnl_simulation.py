from pydantic import BaseModel
from typing import List

class PnLSimulationInput(BaseModel):
    hedge_structure: List[dict]
    historical_prices: List[float]

class PnLSimulationOutput(BaseModel):
    pnl_with_hedge: float
    pnl_without_hedge: float
    protection_summary: str
    average_difference: float
