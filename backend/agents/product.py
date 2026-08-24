from agents.base_agent import BaseAgent


class ProductAgent(BaseAgent):

    def process(self, query):

        prompt = """
You are a Product Expert.

Explain products, features, specifications,
pricing and comparisons.
"""

        return self.ask(prompt, query)