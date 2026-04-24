from langchain_community.document_loaders import TextLoader

# document objects  ?
# Document objects are a data structure used to represent the content and metadata of a document. 
# They typically contain the text content of the document, as well as any relevant metadata such as the source, 
# author, or other attributes. In the context of the TextLoader, each document object would represent a portion 
# of the text file that has been loaded, allowing for easier manipulation and analysis of the text data.

loader = TextLoader("Document_Loaders/cricket.txt", encoding='utf-8')
# specify encoding as there are some special characters in the text file which are not supported by default encoding

docs = loader.load()
# docs is a list of DOCUMENT OBJECTS, each containing the text content and metadata (if any) from the loaded file.

print(type(docs))
# <class 'list'>
print(type(docs[0]))
# <class 'langchain_core.documents.base.Document'>

print(docs)
# print(docs[0])
# print(docs[0].page_content)

# The structure of the docs list is as follows:
# docs is a list of document objects, where each document object has the following attributes:
# - page_content: This attribute contains the actual text content of the document. It is a string that represents the text extracted from the loaded file.
# - metadata: This attribute contains any additional information about the document, such as the source, author, or other relevant details. It is typically



# for using with a model

# chain = prompt | model | parser
# print(chain.invoke({'poem':docs[0].page_content}))