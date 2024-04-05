import logging
import csv

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores.pgvector import PGVector

from ragtalk.settings import config

EMBEDDING_COLUMNS = ["Document"]


def _get_csv_cols(path: str):
    with open(path) as f:
        reader = csv.DictReader(f)
        return reader.fieldnames


def make_embeddings(
    path: str, embedding_columns=EMBEDDING_COLUMNS, metadata_columns=None
):
    metadata_columns = metadata_columns or [
        col for col in _get_csv_cols(path) if col not in embedding_columns
    ]
    logging.info(
        f"Metadata columns: {metadata_columns}\nEmbedding columns: {embedding_columns}"
    )
    loader = CSVLoader(path, metadata_columns=metadata_columns)
    docs = loader.load()

    store = PGVector(
        connection_string=str(config.database_url),
        embedding_function=OpenAIEmbeddings(),
        pre_delete_collection=True,
    )
    store.add_documents(docs)
    logging.info(f"Added {len(docs)} documents to the store.")


if __name__ == "__main__":
    make_embeddings(path=str(config.knowledge_base_path))
