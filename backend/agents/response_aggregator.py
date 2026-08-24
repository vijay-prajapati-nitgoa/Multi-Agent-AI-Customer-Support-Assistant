from services.llm_service import LLMService


class ResponseAggregator:

    def __init__(self):

        self.llm = LLMService()

    def combine(self, query, responses):

        if not responses:
            return "I am unable to answer your question."

        if len(responses) == 1:
            return responses[0]

        combined = "\n\n".join(
            responses
        )

        prompt = f"""
You are a customer support response coordinator.

The customer asked:

{query}

Multiple specialized support agents provided these responses:

{combined}

Create ONE clear and professional final answer for the customer.

Rules:
1. Combine the useful information from all agents.
2. Do not repeat the same information.
3. Do not mention agents or internal processing.
4. Do not invent information.
5. Use the knowledge provided by the agents.
6. Keep the answer concise and helpful.

Final Answer:
"""

        return self.llm.generate(prompt)