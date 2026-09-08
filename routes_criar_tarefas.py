from fastapi import APIRouter
from conexao_banco import ConectarBanco

router = APIRouter( prefix = '/tarefas', tags = ['tarefas'])
@router.post("/criar")
async def criar_tarefas(titulo: str, descricao: str, status: str):
    try:
        Banco = ConectarBanco()
        Banco.conectar()

        comando = ("insert into tarefas (titulo, descricao, status)" 
                     "values (%s, %s, %s)")
        Banco.cursor.execute(comando, (titulo, descricao, status))
        Banco.conexao.commit()
        return {"mensagem": "CRIAÇÃO DE TAREFA REALIZADA"}
    except Exception as erro:
        return {"erro": str(erro)}


@router.get("/{titulo}")
async def listar_tarefas(titulo: str):
    try:
        Banco = ConectarBanco()
        Banco.conectar()
        comando = ("select titulo from tarefas where titulo = %s")
        Banco.cursor.execute(comando, (titulo,))
        resultado = Banco.cursor.fetchone()
        return {"mensagem": resultado}
    except Exception as erro:
        return {"erro": str(erro)}

@router.get("/listar_todas_tarefas")
async def listar_todas_tarefas():
    try:
        Banco = ConectarBanco()
        Banco.conectar()
        comando = ("select * from tarefas")
        Banco.cursor.execute(comando,)
        resultado = Banco.cursor.fetchall()
        return {"mensagem": resultado}
    except Exception as erro:
        return {"erro": str(erro)}



@router.put("/{titulo}")
async def atualizar_tarefa(titulo: str, novo_titulo: str = None, nova_descricao: str = None, novo_status:str = None):
    try:
        Banco = ConectarBanco()
        Banco.conectar()

        campo = []
        valores = []
        if novo_titulo is not None:
            campo.append("titulo = %s")
            valores.append(novo_titulo)
        if nova_descricao is not None:
            campo.append("descricao = %s")
            valores.append(nova_descricao)
        if novo_status is not None:
            campo.append("status = %s")
            valores.append(novo_status)

        comando = ("update tarefas set " + ", ".join(campo) + " where titulo = %s")
        valores.append(titulo)
        Banco.cursor.execute(comando, tuple(valores))
        Banco.conexao.commit()
        return{"mensagem": "ATUALIZAÇÃO REALIZADA"}

    except Exception as erro:
        return {"erro": str(erro)}


@router.delete("/{titulo}")
async def deleter_tarefa(titulo: str):
    try:
        Banco = ConectarBanco()
        Banco.conectar()
        comando = ("delete from tarefas where titulo = %s")
        Banco.cursor.execute(comando, (titulo,))
        Banco.conexao.commit()
        return{"mensagem": "REMOÇÃO REALIZADA."}
    except Exception as erro:
        return {"erro": str(erro)}









