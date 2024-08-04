# from constants import STOCKS
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage


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
        llm = Ollama(model=model_name, request_timeout=120.0)
        return llm

    def prompting(self, llm, user_input):
        messages = [ChatMessage(
            role="system", content = "You are an expert Stock Analyst. Find the puts/calls ratio for the given stock from user input. ONLY output the ratio: puts/calls."
        ),
        ChatMessage(role="user", content=user_input)
        ]
        response = llm.chat(messages)
        return response



if __name__ == "__main__":
    sentiment = sentiment_analysis()
    models = ["phi3:3.8b", "llama3.1:8b"]
    llm = sentiment.setup(models[0])

    # resp = llm.complete("Who is Paul Graham?")
    resp = sentiment.prompting(llm, "What is the puts/calls ratio for Nasdaq on August 2nd, 2024?")
    print(resp)

    





