import os
import shutil
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from typing import List

load_dotenv()

CHROMA_PATH = "chroma"
DATA_PATH = "data"


def process_pdf(file_path: str) -> None:
    """Process a single PDF and update the Chroma DB."""
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
    
    temp_path = os.path.join(DATA_PATH, os.path.basename(file_path))
    shutil.copy(file_path, temp_path)

    documents = load_documents(DATA_PATH)
    chunks = split_text(documents)
    save_to_chroma(chunks, CHROMA_PATH)

    os.remove(temp_path)


def load_documents(data_path: str) -> List:
    """Load all PDFs in the directory."""
    documents = []
    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            loader = PyMuPDFLoader(os.path.join(data_path, file))
            documents.extend(loader.load())
    return documents


def split_text(documents: List) -> List:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    return splitter.split_documents(documents)


def save_to_chroma(chunks: List, chroma_path: str) -> None:
    if os.path.exists(chroma_path):
        shutil.rmtree(chroma_path)
    
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=chroma_path
    )
    db.persist()
