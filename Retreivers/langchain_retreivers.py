import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.retrievers import WikipediaRetriever
from langchain_community.vectorstores import Chroma, FAISS
from langchain_core.documents import Document

from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors.chain_extract import LLMChainExtractor

# Load environment variables from .env
load_dotenv()

# Initialize Gemini Models
# Using gemini-1.5-flash for speed/cost, or gemini-1.5-pro for complex reasoning
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

"""## 1. Wikipedia Retriever"""
retriever = WikipediaRetriever(top_k_results=2, lang="en", wiki_client="wikipedia")
query_wiki = "the geopolitical history of india and pakistan"
docs_wiki = retriever.invoke(query_wiki)

print("\n--- Wikipedia Results ---")
for i, doc in enumerate(docs_wiki):
    print(f"Result {i+1}: {doc.page_content[:200]}...")

"""## 2. Vector Store Retriever (Chroma)"""
source_docs = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="Gemini provides powerful generative models."),
]

vectorstore_chroma = Chroma.from_documents(
    documents=source_docs,
    embedding=embeddings,
    collection_name="gemini_collection"
)

chroma_retriever = vectorstore_chroma.as_retriever(search_kwargs={"k": 2})
results_chroma = chroma_retriever.invoke("What is Chroma used for?")

print("\n--- Chroma Results ---")
for doc in results_chroma:
    print(f"- {doc.page_content}")


"""## 3. MMR (Maximum Marginal Relevance)"""
mmr_docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
]

vectorstore_faiss = FAISS.from_documents(documents=mmr_docs, embedding=embeddings)

mmr_retriever = vectorstore_faiss.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.5}
)

print("\n--- MMR Diverse Results ---")
for doc in mmr_retriever.invoke("What is langchain?"):
    print(f"- {doc.page_content}")


"""## 4. MultiQuery Retriever"""
health_docs = [
    Document(page_content="Regular walking boosts heart health.", metadata={"source": "H1"}),
    Document(page_content="Deep sleep is crucial for cellular repair.", metadata={"source": "H3"}),
    Document(page_content="Drinking water helps maintain metabolism.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system helps balance electricity.", metadata={"source": "I1"}),
]

vectorstore_health = FAISS.from_documents(documents=health_docs, embedding=embeddings)

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore_health.as_retriever(),
    llm=llm
)

print("\n--- MultiQuery Results ---")
mq_results = multiquery_retriever.invoke("How to maintain energy balance?")
for doc in mq_results:
    print(f"- {doc.page_content}")


"""## 5. Contextual Compression"""
comp_docs = [
    Document(page_content="The Grand Canyon is a natural wonder. Photosynthesis is how plants get energy. Tourists visit it yearly."),
    Document(page_content="Castles were built for defense. Chlorophyll captures sunlight for photosynthesis. Knights wore armor."),
]

vectorstore_comp = FAISS.from_documents(comp_docs, embeddings)

# Use Gemini to extract only relevant snippets
compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_retriever=vectorstore_comp.as_retriever(),
    base_compressor=compressor
)

print("\n--- Contextual Compression Results ---")
compressed_results = compression_retriever.invoke("What is photosynthesis?")
for doc in compressed_results:
    print(f"Compressed Content: {doc.page_content}")