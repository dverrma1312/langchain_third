from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

load_dotenv()

id = "121212"

try:
    data = YouTubeTranscriptApi.get_transcript(id)
    documents = " ".join([doc['text'] for doc in data])
except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
chunks = splitter.split_text([documents])

embeddings = OpenAIEmbeddings()

store = FAISS.from_texts(chunks, embeddings)

query = "What is the video about?"

retrieved_docs = store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

context = retrieved_docs.invoke(query)


context_text = "\n\n".join(doc.page_content for doc in context )

prompt = PromptTemplate(template="Based on the following context: {context}, answer the question: {query}", input_variables=["context", "query"])

result = prompt | ChatOpenAI()

final = result.invoke({"context": context_text, "query": query})

print(final.content)







    

