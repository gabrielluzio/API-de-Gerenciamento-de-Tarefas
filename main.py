from fastapi import FastAPI
from routes_criar_tarefas import router
from routes_auth import auth_router


app = FastAPI()

@app.get("/")
async def mensagem():
    return{"mensagem": "api funcionando"}

app.include_router(router)
app.include_router(auth_router)



