
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

def get_medical_vectorstore():
    loader = TextLoader("medical_docs/diabetes.txt", encoding="utf-8")
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(docs, embedding=embeddings)
    return vectordb
