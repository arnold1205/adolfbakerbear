# Archivo: adolfbaker/main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import random 

app = FastAPI()

# Configuración de CORS para desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar los directorios estáticos y de plantillas
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")

# ===================================================================
# LÓGICA DE DATOS
# ===================================================================
MAX_MCAP_GOAL = 6_000_000 
MAX_COOKIES_GOAL = 6_000_000 

def get_real_market_cap():
    """
    IMPORTANTE: Esta función debe simular un Market Cap de 0 para pre-lanzamiento.
    
    PARA ACTIVAR SIMULACIÓN ALEATORIA (POST-LANZAMIENTO), descomenta la línea de abajo.
    return random.uniform(10000, 5000000)
    """
    # Valor fijo de 0 para la fase de pre-lanzamiento
    return 0.0

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Renderiza la página principal."""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "Adolff the Baker Bear",
    })

@app.get("/api/get-progress")
async def get_progress_data():
    """Endpoint llamado por script.js para obtener el progreso en tiempo real."""
    current_mcap = get_real_market_cap()
    
    # Calcular el Porcentaje de Progreso
    percentage = min(100, (current_mcap / MAX_MCAP_GOAL) * 100)
    
    # Calcular las galletas horneadas (proporcional al MCAP)
    current_cookies = (current_mcap / MAX_MCAP_GOAL) * MAX_COOKIES_GOAL

    return {
        "currentMCAP": round(current_mcap, 2),
        "percentage": round(percentage, 2),
        "currentCookies": int(current_cookies)
    }