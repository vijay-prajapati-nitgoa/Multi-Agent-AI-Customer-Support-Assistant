from agents.base_agent import BaseAgent


class FAQAgent(BaseAgent):

    def process(self, query):

        prompt = """
You are an FAQ Expert.

Answer frequently asked questions.
"""

        return self.ask(prompt, query)