from .json_transformer import JSONTransformer


class TransformerFactory:

    @staticmethod
    def create_transformer(transformer_type: str):

        if transformer_type == "json":
            return JSONTransformer()

        else:
            raise ValueError(f"Unsupported transformer type: {transformer_type}")