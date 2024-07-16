from langgraph import LangGraph
from agents.authorization_agent import AuthorizationAgent
from agents.fraud_detection_agent import FraudDetectionAgent
from agents.summary_generation_agent import SummaryGenerationAgent

auth_agent = AuthorizationAgent("Authorization Agent")
fraud_agent = FraudDetectionAgent("Fraud Detection Agent")
summary_agent = SummaryGenerationAgent("Summary Generation Agent")

graph = LangGraph()
graph.add_agent(auth_agent)
graph.add_agent(fraud_agent)
graph.add_agent(summary_agent)

transaction = {"amount": 100, "currency": "USD", "card_number": "1234-5678-9012-3456"}
graph.execute(transaction)