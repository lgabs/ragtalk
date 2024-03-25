from langchain.schema import format_document
from langchain.prompts.prompt import PromptTemplate
from langchain.embeddings import OpenAIEmbeddings

DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template="{page_content}")


def combine_documents(
    docs, document_prompt=DEFAULT_DOCUMENT_PROMPT, document_separator="\n\n"
):
    """Combine documents into a single string."""
    doc_strings = [format_document(doc, document_prompt) for doc in docs]
    return document_separator.join(doc_strings)


def get_retriever():
    pass
    # vectorstore = FAISS.from_texts(
    #     ["harrison worked at kensho"], embedding=OpenAIEmbeddings()
    # )
    # return vectorstore.as_retriever()
