import os
from operator import itemgetter
from typing import List, Tuple

from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    format_document,
)
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import (
    RunnableBranch,
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_core.runnables.history import RunnableWithMessageHistory

# from memory import get_message_history

template = """You are a helpful assistant. Answer the question:"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        MessagesPlaceholder(variable_name="history", optional=True),
        ("user", "{question}"),
    ]
)

chain = prompt | ChatOpenAI() | StrOutputParser()

# chain_with_history = RunnableWithMessageHistory(
#     chain,
#     get_message_history,
#     input_messages_key="input",
#     history_messages_key="history",
# )