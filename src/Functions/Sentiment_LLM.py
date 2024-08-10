# from constants import STOCKS
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from Functions.OptionsData import OptionsData

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

    def prompting(self, llm, user_input, p_o_ratio):
        messages = [ChatMessage(
            role="system", content = "You are an expert Stock Analyst. Given the Puts/Call ratio and the current news. Don't give an explanation. The answer should be one word response: bullish, bearish, or neutral. Answer: _______"
        ),
        ChatMessage(role="user", content=f"{user_input} Puts/Call ratio: {p_o_ratio}")
        ]
        response = llm.chat(messages).message.content

        # if str(response).lower() not in ["bullish", "bearish", "neutral"]:
        #     return "neutral"
        return response




if __name__ == "__main__":
    sentiment = sentiment_analysis()
    options_data = OptionsData()
    p_o_ratio = options_data.get_put_call_ratio('TSLA')


    models = ["phi3:3.8b", "llama3.1:8b"]
    llm = sentiment.setup(models[0])
    
    resp = sentiment.prompting(llm, "What is the sentiment of TSLA?", p_o_ratio)
    print(resp)

    





