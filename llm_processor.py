from llama_index import SimpleWebPageReader, GPTListIndex


def summarize_with_llm(text):
    """
    Summarize the given text using an LLM.
    """
    try:

        index = GPTListIndex.from_documents([SimpleWebPageReader.load_data(text)])
        query_engine = index.as_query_engine()
        summary = query_engine.query("Summarize the following text:")
        return summary.response
    except Exception as e:
        return f"An error occurred while summarizing: {str(e)}"