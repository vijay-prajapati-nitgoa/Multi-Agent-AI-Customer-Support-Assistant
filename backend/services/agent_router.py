from agents.general_agent import GeneralAgent
from agents.billing_agent import BillingAgent
from agents.technical_agent import TechnicalAgent
from agents.product_agent import ProductAgent
from agents.faq_agent import FAQAgent


class AgentRouter:

    def __init__(self):
        self.general = GeneralAgent()
        self.billing = BillingAgent()
        self.technical = TechnicalAgent()
        self.product = ProductAgent()
        self.faq = FAQAgent()

    def route(self, question):

        question = question.lower()

        # Billing
        if any(word in question for word in
               ["payment", "bill", "invoice", "refund", "subscription"]):
            return self.billing.handle(question)

        # Technical
        elif any(word in question for word in
                 ["error", "bug", "issue", "crash", "install"]):
            return self.technical.handle(question)

        # Product
        elif any(word in question for word in
                 ["product", "price", "feature", "specification"]):
            return self.product.handle(question)

        # FAQ
        elif any(word in question for word in
                 ["policy", "return", "shipping", "delivery"]):
            return self.faq.handle(question)

        # General
        else:
            return self.general.handle(question)