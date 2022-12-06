from fastapi import APIRouter, HTTPException

from database import mongo
from models import Produto

router = APIRouter(tags=["Produtos"])

@router.post("/cadastrar/", status_code=201, response_model=Produto)
def cadastrar_produto(produto: Produto):
    pass

@router.get("/produtos/", status_code=200, response_model=list[Produto])
def listar_produtos():
    pass

@router.get("/produtos/{doc_id}", status_code=200, response_model=Produto)
def listar_um_produto(doc_id: int):
    pass

@router.put("/atualizar/", status_code=501)
def atualizar_produto():
    pass

@router.delete("/deletar/", status_code=501)
def deletar_produto():
    pass