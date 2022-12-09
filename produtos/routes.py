from fastapi import APIRouter, HTTPException, Body
from fastapi.encoders import jsonable_encoder as json

from database import mongo
from models import Produto, ProdutoUpdate


router = APIRouter(tags=["Produtos"])


@router.post("/cadastrar/", status_code=201, response_model=Produto)
def cadastrar_produto(produto: Produto = Body(example={"nome": "Banana",
                                                       "preco": "4.18",
                                                       "descricao": "Uma dúzia de bananas."})):
    new_doc = produto.dict(by_alias=True)

    if mongo.coll.find_one({k:v for k,v in new_doc.items() if k != "_id"}):
        raise HTTPException(400, "Este produto já está cadastrado")

    result = mongo.coll.insert_one(new_doc)
    inserted_doc = mongo.coll.find_one({"_id": result.inserted_id})

    return inserted_doc


@router.get("/produtos/", status_code=200, response_model=list[Produto])
def listar_produtos():
    return list(mongo.coll.find())


@router.get("/produtos/{doc_id}", status_code=200, response_model=Produto)
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
# TODO: figure out how to forbid _id setting during requests to /cadastrar