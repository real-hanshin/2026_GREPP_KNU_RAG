import csv
from langchain_community.vectorstores import FAISS
from langchain_core.documents.base import Document
from embeddings import get_embeddings
from typing import List

def load_documents() -> List[Document]:
    docs = []
    
    with open('dataset.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            docs.append(
                Document(
                    page_content=f"규정명: {row.get('title', '')}\n내용: {row.get('content', '')}",
                    metadata={
                        'id': row.get('id', ''),
                        'category': row.get('category', 'KBO규정'),
                        'title': row.get('title', '')
                    }
                )
            )
    return docs

def init_vectorstore():
    docs = load_documents()
    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(
        documents=docs,
        embedding=embeddings
    )
    save_vector_to_local(vectorstore)
    return vectorstore

def save_vector_to_local(vectorstore):
    path_str = './kbo-faiss'    
    vectorstore.save_local(path_str)

def load_vector_from_local():
    path_str = './kbo-faiss'
    return FAISS.load_local(
        path_str,
        get_embeddings(),
        allow_dangerous_deserialization=True
    )