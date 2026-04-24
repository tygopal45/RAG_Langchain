from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Document_Loaders/Social_Network_Ads.csv")

docs = loader.load()

print(len(docs))
# every row in the csv file is converted to a document object and stored in a list

print(docs[0].page_content)