import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import router as v1_router
from app.api.v1.endpoints.customer import router as customer_router
from app.api.v1.endpoints.vehicle import router as vehicle_router
from app.api.v1.endpoints.mechanic import router as mechanic_router
from app.db.session import engine
from app.db.base import Base

#Configuração básica do logging
logging.basicConfig(
    level=logging.INFO, #Nível de log (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Formato da mensagem
    handlers=[
        logging.FileHandler("app.log"), #Salva logs em um arquivo
        logging.StreamHandler() #Exibe logs no console
    ]
    )

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine) # Cria tabelas (apenas para desenvolvimento)


app = FastAPI(title = "Oficina Mecânica")
app.include_router(v1_router)
app.include_router(customer_router, prefix="/api/v1")
app.include_router(vehicle_router, prefix="/api/v1")
app.include_router(mechanic_router, prefix="/api/v1")

#Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    logger.info("Acesso à roda raiz") 
    return {"message" :"Mechanical WorkShop System - API"}