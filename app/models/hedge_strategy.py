from pydantic import BaseModel

class HedgeStrategyInput(BaseModel):
    exposure_type: str
    volume: float
    start_date: str
    end_date: str
    protection_type: str
    price_variation_tolerance: float

class HedgeStrategyOutput(BaseModel):
    strategy_description: str
    technical_justification: str
    complexity_level: str
