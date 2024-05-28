from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
import os
import shutil


DATA_PATH = 'data/'
CHROMA_PATH = 'chroma/'

def load_documents():
    #carregando os documentos, somente aqueles que sao markdown
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    #criando chunks de 1000 caracteres com overlap de 500, dividindo meus textos em pedaços menores
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True,
    )
    chuncks = text_splitter.split_documents(documents)
    return chuncks

def save_chroma(chunks: list[Document]):
    #excluindo o bd antigo com o mesmo nome (CHROMA_PATH)
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    #criando um novo bd
    db = Chroma.from_documents(
        chunks,
        OpenAIEmbeddings(),
        persist_directory = CHROMA_PATH
    )
    db.persist()

def main():
    documents = load_documents()
    chunks = split_text(documents)
    save_chroma(chunks)

if __name__ == '__main__':
    main() 
