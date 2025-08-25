from fastapi import FastAPI
from src.auth.router import router as auth_router
from src.users.router import router as users_router
from src.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Proyecto Integrador")

app.include_router(auth_router)
app.include_router(users_router)
