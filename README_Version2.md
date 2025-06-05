# Sistema de Hedge Institucional

## Descrição
Este projeto é composto por dois módulos principais desenvolvidos em FastAPI:
1. **Recomendação de Estratégias de Hedge**: Gera estratégias de hedge com base em parâmetros fornecidos.
2. **Simulação de PnL**: Calcula o PnL com e sem hedge utilizando dados históricos.

## Requisitos
- Python 3.10+
- FastAPI para APIs RESTful
- Pydantic para validações

## Estrutura
```plaintext
sistema_hedge/
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── tests/
```

## Como Rodar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```