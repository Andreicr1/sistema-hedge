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
│   └── routes/
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
O diretório `frontend/` não acompanha este repositório e deve ser criado 
separadamente. Para inicializar o ambiente:
1. Crie um projeto Next.js (caso ainda não exista):
   ```bash
   npx create-next-app@latest frontend
   ```
2. Instale as dependências e inicie o servidor de desenvolvimento:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
