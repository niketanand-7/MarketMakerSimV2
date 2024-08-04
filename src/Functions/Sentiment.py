from constants import STOCKS
from llama_index.llms.ollama import Ollama

'''
Sentiment indicators gauge market psychology in the form of investor or consumer behavior and beliefs that may influence the market.
'''

# First we will try to leverage LLM without calling RAG or giving it a Database

# Develop prompt for different stocks

# load model

# invoke model with prompt

# Next steps: use another model to analyze the sentiment of the stock data
class sentiment_analysis:
    def setup(self, model_name):
        llm = Ollama(model=model_name, request_timeout=30.0)
        return llm



if __name__ == "__main__":
    sentiment = sentiment_analysis()
    llm = sentiment.setup("llama3.1:latest")

    





