from langgraph import Agent
from tavily import TavilyClient
import config

class SummaryGenerationAgent(Agent):
    def __init__(self, name):
        super().__init__(name)
        self.tavily_client = TavilyClient(api_key=config.TAVILY_API_KEY)

    def execute(self, transaction):
       summary = f"Transaction of {transaction["amount"]} {transaction["currency"]} was {"authorized" if transaction["status"] == "authorized" else "declined"}."

       enhanced_summary = self.tavily_client.generate_summary(summary)

       print(enhanced_summary)
       transaction["summary"] = enhanced_summary