from langgraph import Agent
from tavily import TavilyClient
import config

class AuthorizationAgent(Agent):
    def __init__(self, name):
        super().__init__(name)
        self.tavily_client = TavilyClient(api_key=config.TAVILY_API_KEY)

    def execute(self, transaction):
        card_number = transaction["card_number"]
        amount = transaction["amount"]

        valid_card = self.tavily_client.verify_card(card_number)
        sufficient_funds = self.tavily_client.check_funds(card_number, amount)

        if valid_card and sufficient_funds:
            print("Transaction authorized.")
            transaction["status"] = "authorized"
        else:
            print("Transaction declined")
            transaction["status"] = "declined"