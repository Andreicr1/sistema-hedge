from fastapi import APIRouter, HTTPException
from typing import List
from app.models.hedge_strategy import HedgeStrategyInput, HedgeStrategyOutput

router = APIRouter()

@router.post("/recommendations", response_model=List[HedgeStrategyOutput])
def recommend_strategies(input_data: HedgeStrategyInput):
    # Mock de lógica: substituir por lógica robusta
    if input_data.volume <= 0:
        raise HTTPException(status_code=400, detail="Volume deve ser maior que zero.")
    
    return [
        HedgeStrategyOutput(
            strategy_description="Buy AVG Jan / Sell Fix 25/Jan",
            technical_justification="Proteção contra variações extremas de preço.",
            complexity_level="Médio"
        ),
        HedgeStrategyOutput(
            strategy_description="Rolling Hedge semanal",
            technical_justification="Flexibilidade para ajustar conforme mercado.",
            complexity_level="Alto"
        )
    ]
