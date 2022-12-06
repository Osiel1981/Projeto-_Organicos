from decimal import Decimal
from bson.decimal128 import Decimal128
from bson.codec_options import CodecOptions, TypeCodec, TypeRegistry
from pymongo import MongoClient


class DecimalCodec(TypeCodec):
    python_type = Decimal
    bson_type = Decimal128

    def transform_python(self, value: Decimal) -> Decimal128:
        return Decimal128(value)

    def transform_bson(self, value: Decimal128) -> Decimal:
        return value.to_decimal()

codec_options = CodecOptions(type_registry=TypeRegistry([DecimalCodec()]))

class DatabaseConnection:
    def __init__(self,
                 connection_string: str = "mongodb+srv://gama:gama@cluster0.rmcucbo.mongodb.net",
                 database_name: str = "gama",
                 collection_name: str = "produtos"):
        self.client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
        self.db = self.client.get_database(database_name)
        self.coll = self.db.get_collection(collection_name, codec_options=codec_options)

mongo = DatabaseConnection()