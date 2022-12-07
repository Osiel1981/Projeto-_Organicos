from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder as json

from database import mongo
from models import ProdutoIn, ProdutoOut, ProdutoUpdate


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


@router.patch("/atualizar/{doc_id}", status_code=200)
def atualizar_produto(doc_id: str, produto: ProdutoUpdate):
    produto = json(produto, exclude={"_id": True, "id": True}, exclude_unset=True)

    if doc_before := mongo.coll.find_one_and_update({"_id": doc_id}, {"$set": produto}):
        doc_after = mongo.coll.find_one({"_id": doc_id})
        return {"antes": doc_before, "depois": doc_after}
    
    return HTTPException(404, f"Produto com o ID {doc_id} não existe")


@router.delete("/deletar/{doc_id}", status_code=200)
def deletar_produto(doc_id: str):
    deleted_doc = mongo.coll.find_one_and_delete({"_id": doc_id})

    return {"documento deletado": deleted_doc}

# TODO: handle errors properly
# TODO: structure things so that the OpenAPI docs are created correctly