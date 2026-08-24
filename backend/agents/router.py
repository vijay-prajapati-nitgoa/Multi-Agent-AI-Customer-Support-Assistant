from agents.billing import BillingAgent
from agents.technical import TechnicalAgent
from agents.product import ProductAgent
from agents.complaint import ComplaintAgent
from agents.faq import FAQAgent
from agents.intent_detector import IntentDetector
from agents.response_aggregator import ResponseAggregator


class AgentRouter:

    def __init__(self, rag_pipeline):

        self.detector = IntentDetector()

        self.billing = BillingAgent(rag_pipeline)
        self.technical = TechnicalAgent(rag_pipeline)
        self.product = ProductAgent(rag_pipeline)
        self.complaint = ComplaintAgent(rag_pipeline)
        self.faq = FAQAgent(rag_pipeline)

        self.aggregator = ResponseAggregator()

    def route(self, query):

        intents = self.detector.detect(query)

        responses = []

        for intent in intents:

            if intent == "Billing Agent":

                responses.append(
                    self.billing.process(query)
                )

            elif intent == "Technical Agent":

                responses.append(
                    self.technical.process(query)
                )

            elif intent == "Product Agent":

                responses.append(
                    self.product.process(query)
                )

            elif intent == "Complaint Agent":

                responses.append(
                    self.complaint.process(query)
                )

            elif intent == "FAQ Agent":

                responses.append(
                    self.faq.process(query)
                )

        return self.aggregator.combine(
            query,
            responses
        )