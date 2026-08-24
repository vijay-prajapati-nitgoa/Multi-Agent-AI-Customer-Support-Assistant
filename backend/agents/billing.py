from agents.base_agent import BaseAgent


class BillingAgent(BaseAgent):

    def process(self, query):

        prompt = """
You are a Billing Support Expert.

Answer only billing related questions.

Topics:
- Payments
- Refunds
- Invoice
- Subscription
"""

        return self.ask(prompt, query)