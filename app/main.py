from fastapi import FastAPI
from app.routes import hedge_strategy, pnl_simulation

app = FastAPI(
    title="Sistema de Hedge Institucional",
    description="APIs para recomendação de estratégias de hedge e simulação de PnL",
    version="1.0.0"
)

# Incluindo as rotas
app.include_router(hedge_strategy.router, prefix="/hedge")
app.include_router(pnl_simulation.router, prefix="/pnl")