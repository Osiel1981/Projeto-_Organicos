from bson.objectid import ObjectId
from decimal import Decimal
from pydantic import BaseModel, Field


class Produto(BaseModel):
    id: str = Field(default_factory=ObjectId, alias="_id", example="666f6f2d6261722d71757578")
    nome: str = Field(..., example="Banana")
    preco: Decimal = Field(..., ge=0, decimal_places=2, example=Decimal("4.18"))
    descricao: str = Field(..., example="Uma dúzia de bananas.")

    class Config:
        anystr_strip_whitespace = True
        extra = "allow"
        allow_population_by_field_name = True