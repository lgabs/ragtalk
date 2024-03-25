# ragtalk
ragtalk is a Q&amp;A Chatbot with LLM, made with Langchain and LangServe.

## TODOs

- [ ] Update this readme with project idea and main components
- [x] Add docker compose with services for db (postgrest with pgvector) and api
- [x] Add memory
- [x] Add example dataset helpers
- [ ] Add dataset (csv) loader and embedd into the vectordb
- [ ] Add retriever with pgvector
- [ ] Add basic unit tests
- [ ] Add support to evaluate answers (e.g [deepeval](https://github.com/confident-ai/deepeval))

# Example files

The `examples` folder contains some example files to run the application locally. To get an example of a Q&A dataset, download this [Question-Answer Dataset](https://www.kaggle.com/datasets/rtatman/questionanswer-dataset?resource=download&select=S08_question_answer_pairs.txt) into `examples/qa_example.csv` path and run `python examples/make_qa_example.py` to build a simple knowledge base with question and answer together (the result will be embedded together).
# References
- [LangChain Template - RAG Conversation](https://github.com/langchain-ai/langchain/tree/master/templates/rag-conversation)
- [Langchain Template - Chat with Persistence](https://github.com/langchain-ai/langserve/blob/main/examples/chat_with_persistence/server.py)
- [Langchain Conversation with Retrieval Chain](https://github.com/langchain-ai/langserve/blob/main/examples/conversational_retrieval_chain/server.py)
- [langchain-cli](https://github.com/langchain-ai/langchain/blob/master/libs/cli/DOCS.md)
