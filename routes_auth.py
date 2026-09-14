from fastapi import APIRouter
from conexao_banco import ConectarBanco
from pwdlib import PasswordHash

auth_router = APIRouter( prefix = "/auth", tags = ['auth'])

def gerar_hash_senha(senha):
    senha_hash = PasswordHash.recommended()
    hash = senha_hash.hash(senha)
    return hash

@auth_router.post("/cadastro")
async def cadastro(nome: str, email, senha: str):

    try:
        Banco = ConectarBanco()
        Banco.conectar()

        senha_hash = gerar_hash_senha(senha)

        comando = ("insert into autentificacao (nome, email, senha)"
                   "values (%s, %s, %s)")

        Banco.cursor.execute(comando,(nome, email, senha_hash))
        Banco.conexao.commit()

        Banco.cursor.close()
        Banco.conexao.close()

        return {"mensagem": "USUARIO CADASTRADO"}
    except Exception as erro:
        Banco.cursor.close()
        Banco.conexao.close()
        return {"erro": str(erro)}





def verificar_senha_hash(senha, hash):
    password_hash = PasswordHash.recommended()
    return password_hash.verify(senha, hash)

@auth_router.get("/login")
async def login(email: str, senha: str):
    Banco = ConectarBanco()
    Banco.conectar()

    comando1 = ("select exists(select email from autentificacao where email = %s)")
    Banco.cursor.execute(comando1,(email,))
    resultado1 = Banco.cursor.fetchone()
    if resultado1[0] == True:
        comando = ("select senha from autentificacao where email = %s")

        Banco.cursor.execute(comando,(email,))
        resultado = Banco.cursor.fetchone()
        valido = verificar_senha_hash(senha, resultado[0])

        Banco.cursor.close()
        Banco.conexao.close()

        if valido == True:
            return {"mensagem": "Acesso liberado"}
        else:
            return{"mensagem": "acesso negado" }
    else:
        return {"mensagem": "usuario com email nao encontrado. "}


