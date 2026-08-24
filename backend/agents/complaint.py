from agents.base_agent import BaseAgent


class ComplaintAgent(BaseAgent):

    def process(self, query):

        prompt = """
You are a Customer Complaint Officer.

Respond politely and professionally.
"""

        return self.ask(prompt, query)