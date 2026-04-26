import os
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_chroma import Chroma
from langchain_core.documents import Document


load_dotenv()

docs = [
    Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history.",
        metadata={"team": "Royal Challengers Bangalore"}
    ),
    Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles.",
        metadata={"team": "Mumbai Indians"}
    ),
    Document(
        page_content="MS Dhoni has led Chennai Super Kings to multiple IPL titles. His leadership is legendary.",
        metadata={"team": "Chennai Super Kings"}
    ),
    Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket.",
        metadata={"team": "Mumbai Indians"}
    ),
    Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder representing Chennai Super Kings.",
        metadata={"team": "Chennai Super Kings"}
    )
]

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory='my_chroma_db',
    collection_name='sample'
)

uuids = vector_store.add_documents(docs)


# to see the metadata, documents and embeddings stored in the vector store
met = vector_store.get(include=["embeddings", "metadatas", "documents"])
print(f"\nMetadata: {met['metadatas']}")
print(f"\nDocuments: {met['documents']}")
print(f"\nEmbeddings: {met['embeddings']}")
print(f"\nIDs: {met['ids']}")


# add
print(f"Added {len(uuids)} documents to the vector store.")

# search
# similarity search
query = "Who is the captain of Mumbai Indians?"
results = vector_store.similarity_search(query=query, k=1)
# k - number of similar documents to retrieve

query_bowler = "Who among these are a bowler ?"
results_bow = vector_store.similarity_search(query=query_bowler, k=2)

# we can also search by score -> the less the score, the more similar the document is to the query
results_score = vector_store.similarity_search_with_score(query=query_bowler, k=2)


for doc in results:
    print(f"\nResult: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")

print(results_bow)

print(results_score)

# filter
# metadata filtering

res = vector_store.similarity_search_with_score(
    query=" ",
    filter={"team": "Mumbai Indians"}
)
print(res)


# update
target_id = uuids[0] 

updated_doc1 = Document(
    page_content="Virat Kohli is the former captain of Royal Challengers Bangalore in IPL.",
    metadata={"team": "Royal Challengers Bangalore"}
)

# 2. Use the dynamic ID instead of a hardcoded string
vector_store.update_document(
    document_id=target_id, 
    document=updated_doc1
)

# 3. Verify the change
met = vector_store.get(include=["embeddings", "metadatas", "documents"])
print("\n--- Updated Data ---")
print(f"Metadata: {met['metadatas']}")
print(f"Documents: {met['documents']}")


# delete
vector_store.delete(ids=[uuids[0]])  # Deleting the second document
met = vector_store.get(include=["embeddings", "metadatas", "documents"])
print("\n--- Deleted Data ---")
print(f"Metadata: {met['metadatas']}")
print(f"Documents: {met['documents']}")