# Sistema de Hedge Institucional

## Descrição
Este projeto é composto por dois módulos principais desenvolvidos em FastAPI:
1. **Recomendação de Estratégias de Hedge**: Gera estratégias de hedge com base em parâmetros fornecidos.
2. **Simulação de PnL**: Calcula o PnL com e sem hedge utilizando dados históricos.

Além do backend em FastAPI, agora o repositório contém também um frontend em Next.js na pasta `frontend/`.

## Requisitos
- Python 3.10+
- FastAPI para APIs RESTful
- Pydantic para validações
- Node.js e npm para o frontend

## Estrutura
```plaintext
sistema_hedge/
├── app/              # Código do backend
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── tests/
├── frontend/         # Projeto Next.js
└── requirements.txt
```

## Como Rodar
### Backend
1. Instale as dependências do Python:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o servidor com `uvicorn`:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend
1. Instale as dependências do projeto React:
   ```bash
   cd frontend
   npm install
   ```
2. Inicie o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```
