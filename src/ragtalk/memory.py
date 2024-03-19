from settings import DATABASE_URL
from langchain.memory import PostgresChatMessageHistory

def get_message_history(session_id: str):
    return PostgresChatMessageHistory(session_id=session_id, connection_string=DATABASE_URL)