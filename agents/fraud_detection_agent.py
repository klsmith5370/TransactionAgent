import pickle
from langgraph import Agent
from tavily import TavilyClient
import config

class FraudDetectionAgent(Agent):
    def __init__(self, name):
        super().__init__(name)
        self.tavily_client = TavilyClient(api_key=config.TAVILY_API_KEY)
        self.model = pickle.load(open("models/fraud_detection_model.pkl", "rb"))

    def execute(self, transaction):
        features = [transaction["amount"], transaction["currency"], transaction["card_number"]]

        enriched_data = self.tavily_client.enrich_data(features)
        prediction = self.model.predict([enriched_data])

        if prediction[0] == 1:
            print("Fraud detected.")
            transaction["fraud"] = True
        else:
            print("No fraud detected.")
            transaction["fraud"] = False