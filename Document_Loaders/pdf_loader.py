from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Document_Loaders/dl-curriculum.pdf")
# mainly used for textual data


docs = loader.load()

print(len(docs))
# 23 for 23 pages in the PDF

# print(docs)
# define the structure of docs sections in crisp manner
# [Document(page_content='Page 1 content', metadata={'source': 'dl-curriculum.pdf', 'page': 1}),
#  Document(page_content='Page 2 content', metadata={'source': 'dl-curriculum.pdf', 'page': 2}), ...]

print(docs[0].page_content)
print(docs[0].metadata)