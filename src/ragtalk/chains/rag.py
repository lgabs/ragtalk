from typing import TypedDict
from ragtalk.settings import config
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain.schema.runnable.utils import ConfigurableFieldSpec

from ragtalk.memory import get_message_history

from ragtalk.settings import chain_params

prompt_template = chain_params.get("llm").get("prompt_template")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", prompt_template),
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
).with_types(input_type=InputChat)
