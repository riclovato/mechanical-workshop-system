import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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
app = FastAPI()

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