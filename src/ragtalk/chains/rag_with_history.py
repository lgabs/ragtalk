from operator import itemgetter

from typing import TypedDict, List, Tuple
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts.prompt import PromptTemplate
from langchain_core.prompts import (
    ChatPromptTemplate,
)

from langchain.schema.runnable import RunnableMap, RunnablePassthrough

from langchain_core.runnables.history import RunnableWithMessageHistory

from ragtalk.settings import chain_params
from ragtalk.memory import get_message_history, format_chat_history
from ragtalk.retriever import get_retriever, combine_documents

STANDALONE_QUESTION_TEMPLATE = chain_params.get("prompts").get(
    "standalone_question_template"
)
STANDALONE_QUESTION_PROMPT = PromptTemplate.from_template(STANDALONE_QUESTION_TEMPLATE)

RAG_ANSWER_TEMPLATE = chain_params.get("prompts").get("rag_answer_template")
RAG_ANSWER_PROMPT = ChatPromptTemplate.from_template(RAG_ANSWER_TEMPLATE)

_inputs = RunnableMap(
    standalone_question=RunnablePassthrough.assign(
        chat_history=lambda x: format_chat_history(x["chat_history"])
    )
    | STANDALONE_QUESTION_PROMPT
    | ChatOpenAI(temperature=0)
    | StrOutputParser(),
)
retriever = get_retriever()
_context = {
    "context": itemgetter("standalone_question") | retriever | combine_documents,
    "question": lambda x: x["standalone_question"],
}


conversational_qa_chain = (
    _inputs | _context | RAG_ANSWER_PROMPT | ChatOpenAI() | StrOutputParser()
)


class InputChat(TypedDict):
    """Input for the chat endpoint."""

    human_input: str
    """Human input"""


rag_with_history_chain = RunnableWithMessageHistory(
    conversational_qa_chain,
    get_message_history,
    input_messages_key="human_input",
    history_messages_key="history",
).with_types(input_type=InputChat)
