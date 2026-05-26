from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Linux Deploy Portfolio API",
    description="API simples para demonstrar deploy com Linux, Docker, Nginx e HTTPS.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "API online com FastAPI, Docker, Nginx e Linux",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "linux-deploy-portfolio",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/client-info")
def client_info():
    return {
        "project": "Deploy profissional em VPS Linux",
        "stack": ["Linux", "Docker", "FastAPI", "Nginx", "HTTPS"],
        "objective": "Simular um serviço real de publicação de aplicação para clientes."
    }
