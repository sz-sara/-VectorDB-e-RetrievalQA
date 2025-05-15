from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama.llms import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter


try:
    file_path = "C:/Users/saraa/geral/TSI/GIT/Conteúdo 1 _ Projetos.pdf"
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
except:
    print("Erro na análise do arquivo")


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50,
    length_function=len,
)

texts = text_splitter.split_documents(pages)

print (f"Foram criados: {len(texts)} chunks a partir de {file_path}")

print("--"*100)

db = FAISS.from_documents(texts,  OllamaEmbeddings(model="mxbai-embed-large"))
while True:
    query = input("Qual a sua pergunta?(Para interromper, digite: sair): ")
    if query.lower() == 'sair':
        print("Encerrando")
        break
    else:
        docs = db.similarity_search(query)
        print("Aguarde...")

        try:
            model = OllamaLLM(model="llama3.2:latest")
            retriever = db.as_retriever(search_kwargs={"k": 5})
            qa_chain = RetrievalQA.from_chain_type(llm=model, retriever=retriever, chain_type="stuff")
            response = qa_chain.invoke(query)
            print("\nResposta gerada pelo modelo:\n", response["result"])
        except:
            print("Resposta não foi gerada com êxito")
        
    

    