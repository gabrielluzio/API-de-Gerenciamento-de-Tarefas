from fastapi import FastAPI
from routes_criar_tarefas import router


app = FastAPI()

@app.get("/")
async def mensagem():
    return{"mensagem": "api funcionando"}
print('registrando router')
app.include_router(router)
print('router registrado')
print(app.routes)

