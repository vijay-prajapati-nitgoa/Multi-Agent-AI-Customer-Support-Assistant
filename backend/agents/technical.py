from agents.base_agent import BaseAgent


class TechnicalAgent(BaseAgent):

    def process(self, query):

        prompt = """
You are a Technical Support Engineer.

Help users solve technical issues.

Topics:
- Login problems
- Installation
- Password
- Errors
"""

        return self.ask(prompt, query)