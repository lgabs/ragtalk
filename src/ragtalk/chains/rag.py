import os
from operator import itemgetter
from typing import List, Tuple, TypedDict

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

from langchain.schema.runnable.utils import ConfigurableFieldSpec

from memory import get_message_history

template = """You are a helpful assistant. Answer the question:"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        MessagesPlaceholder(variable_name="history", optional=True),
        ("user", "{human_input}"),
    ]
)


chain = prompt | ChatOpenAI() | StrOutputParser()


class InputChat(TypedDict):
    """Input for the chat endpoint."""

    human_input: str
    """Human input"""


rag_chain_with_history = RunnableWithMessageHistory(
    chain,
    get_message_history,
    input_messages_key="human_input",
    history_messages_key="history",
    history_factory_config=[
        ConfigurableFieldSpec(
            id="session_id",
            annotation=str,
            name="Session ID",
            description="Unique identifier for the conversation.",
            default="",
            is_shared=True,
        ),
    ],
).with_types(input_type=InputChat)
