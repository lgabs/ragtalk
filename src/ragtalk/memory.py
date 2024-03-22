from ragtalk.settings import config
from langchain.memory import PostgresChatMessageHistory


def get_message_history(session_id: str):
    return PostgresChatMessageHistory(
        session_id=session_id, connection_string=str(config.database_url)
    )
