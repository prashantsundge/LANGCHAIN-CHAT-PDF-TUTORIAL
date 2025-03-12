from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback



def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬 ")

    #uploading pdf files 

    pdf = st.file_uploader("Upload your PDF", type ="pdf")

    #extract the text of the file
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        #look through the pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        #split into chunks 
        text_spliter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len

        )
        #chunk created
        chunks = text_spliter.split_text(text)
        
        # convert our chunks to Embeddings 
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        #show user input
        user_question = st.text_input("Ask Question about your PDF:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            
            #large Language model 
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents = docs, question=user_question)
                print(cb)
            st.write(response)





    








if __name__ == "__main__":
    main()