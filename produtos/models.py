from decimal import Decimal
from pydantic import BaseModel, Field
from uuid import uuid4


class ProdutoIn(BaseModel):
    nome: str = Field(..., example="Banana")
    preco: Decimal = Field(..., ge=0, decimal_places=2, example=Decimal("4.18"))
    descricao: str = Field(..., example="Uma dúzia de bananas.")

    class Config:
        anystr_strip_whitespace = True
        extra = "allow"

class ProdutoOut(ProdutoIn):
    id: str = Field(default_factory=uuid4, alias="_id", example="12345678-1234-5678-1234-567812345678")

    class Config:
        allow_population_by_field_name = True