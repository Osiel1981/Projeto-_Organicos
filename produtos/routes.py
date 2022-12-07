from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder as json

from database import mongo
from models import ProdutoIn, ProdutoOut


router = APIRouter(tags=["Produtos"])


@router.post("/cadastrar/", status_code=201, response_model=ProdutoOut)
def cadastrar_produto(produto: ProdutoIn):
    produto = json(produto)
    
    if mongo.coll.find_one(produto):
        raise HTTPException(400, "Este produto já está cadastrado")

    new_doc = ProdutoOut(**produto)
    result = mongo.coll.insert_one(json(new_doc))

    return mongo.coll.find_one({"_id": result.inserted_id})


@router.get("/produtos/", status_code=200, response_model=list[ProdutoOut])
def listar_produtos():
    return list(mongo.coll.find())


@router.get("/produtos/{doc_id}", status_code=200, response_model=ProdutoOut)
def listar_um_produto(doc_id: str):
    return mongo.coll.find_one({"_id": doc_id})


@router.patch("/atualizar/", status_code=501)
def atualizar_produto():
    pass


@router.delete("/deletar/", status_code=501)
def deletar_produto():
    pass