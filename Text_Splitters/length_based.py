from langchain_text_splitters import CharacterTextSplitter

text = """Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0,
    # what is chunk overlap? 
    # Chunk overlap refers to the number of characters that are shared between consecutive chunks when splitting a text. It helps to maintain context and continuity between chunks, especially when the text is split at natural breakpoints. For example, if you have a chunk size of 100 characters and a chunk overlap of 20 characters, the first chunk would contain characters 0-99, the second chunk would contain characters 80-179, and so on. This way, the last 20 characters of the first chunk are included in the second chunk, providing some overlap for better understanding and coherence when processing the chunks separately.
    separator=" "
)

result = splitter.split_text(text)

print(result)

print(len(result))



