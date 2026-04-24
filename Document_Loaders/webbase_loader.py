# Web Base Loader uses -> Request to fetch the content of a web page and 
# then uses BeautifulSoup to parse the HTML and extract the text content. 
# It also handles pagination by following "Next" links if they are present.

from langchain_community.document_loaders import WebBaseLoader

url = "https://www.geeksforgeeks.org/computer-networks/arp-protocol/"

loader = WebBaseLoader(url)
# we can pass multiple urls as well, it will return a list of documents for each url

docs = loader.load()

print(docs[0].page_content)  
# Print the first 500 characters of the page content

# use your model to ask questions about the content of the page
