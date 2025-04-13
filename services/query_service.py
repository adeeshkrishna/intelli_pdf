from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from typing import Dict

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def run_query(query_text: str) -> Dict[str, object]:
    embedding_fn = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_fn)

    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if not results or results[0][1] < 0.7:
        return {"response": "Unable to find matching results.", "sources": []}

    context = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE).format(
        context=context, question=query_text
    )

    model = ChatOpenAI()
    response_text = model.predict(prompt)
    sources = [doc.metadata.get("source", "Unknown") for doc, _ in results]

    return {"response": response_text, "sources": sources}
