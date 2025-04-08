from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


def generator(input):
    loader=PyPDFLoader("Attention.pdf")
    docs=loader.load()
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    documents=text_splitter.split_documents(docs)
    db=Chroma.from_documents(documents[ :10], OpenAIEmbeddings())
    retriever=db.as_retriever()

    llm=ChatOpenAI(model="gpt-3.5-turbo")


    prompt=ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context.
    Think step by step before providing a detailed answer.
    <context>
    {context}
    </context>
    Question:{input}""")


    document_chain=create_stuff_documents_chain(llm,prompt)


    retrieval_chain=create_retrieval_chain(retriever, document_chain)
    response=retrieval_chain.invoke({"input" : input })
    
    return response