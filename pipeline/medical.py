from connectors.connector_factory import ConnectorFactory
from extractors.extractor_factory import ExtractorFactory
from transformers.transformer_factory import TransformerFactory
from loaders.loader_factory import LoaderFactory


def run_pipeline(input_data):
    """
    input_data example:
    {
        "connector": "postgres",
        "extractor": "user",
        "transformer": "json",
        "loader": "opensearch",
        "table": "students"
    }
    """

    # 1️⃣ Create connector
    connector = ConnectorFactory.create_connector(input_data["connector"])

    connection = connector.connect()

    # 2️⃣ Create extractor
    extractor = ExtractorFactory.create_extractor(
        input_data["extractor"], connection
    )

    extracted_data = extractor.extract(input_data["table"])

    print("Extracted:", extracted_data)

    # 3️⃣ Create transformer
    transformer = TransformerFactory.create_transformer(
        input_data["transformer"]
    )

    transformed_data = transformer.transform(extracted_data)

    print("Transformed:", transformed_data)

    # 4️⃣ Create loader
    loader = LoaderFactory.create_loader(input_data["loader"])

    response = loader.index_documents(transformed_data)

    print("Loaded to OpenSearch")
    print(response)


if __name__ == "__main__":

    input_config = {
        "connector": "postgres",
        "extractor": "user",
        "transformer": "json",
        "loader": "opensearch",
        "table": "students"
    }

    run_pipeline(input_config)