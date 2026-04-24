from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Text_Splitters/dl-curriculum.pdf")
docs = loader.load()



text = """Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0,
    separator=" "
)

result = splitter.split_text(text)

print(result)
print(len(result))


# For dicument splitting, you can use the same splitter to split the loaded documents. 
# The `split_documents` method will apply the splitting logic to each document in the list.

result_doc = splitter.split_documents(docs)
# for first chunk of the first document
print(result_doc[0])


