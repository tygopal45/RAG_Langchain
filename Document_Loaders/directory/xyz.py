from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="./Document_Loaders/directory", 
    # globe pattern to specify which files to load, here we are loading all PDF files in the directory
    glob="*.pdf",
    loader_cls=PyPDFLoader
    # loader_cls is used to specify which loader to use for the files, here we are using PyPDFLoader to load PDF files
)

docs = loader.load()

print(len(docs))
# sum of total pages in all the PDF files in the directory

print(docs[0].page_content)
print(docs[0].metadata)

print(docs[325].page_content)
print(docs[325].metadata)