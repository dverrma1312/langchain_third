from langchain_community.retrievers import WikipediaRetriever, Multiqueryretriever
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstore import chroma

retriever = WikipediaRetriever(
    top_k_results= 3, lang= "en"
)

db = chroma.from_documents(
        documents = documents,
        embeddings = OpenAIEmbeddings,
        collection_name = "new_collection"
)

retriver = db.as_retriever(search_type = 'mmr' ,search_kargs= {'k':3})

query = "what is the query"

db.invovke(query)

mq = Multiqueryretriever.from_llm(
    retriever = retreiver,
    llm = 'jdjd'
)

