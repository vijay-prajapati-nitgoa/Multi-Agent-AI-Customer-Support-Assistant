from langchain_ollama import ChatOllama

from config import OLLAMA_MODEL, TEMPERATURE


class LLMService:

    def __init__(self):

        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            temperature=TEMPERATURE
        )

    def generate(self, prompt: str) -> str:

        response = self.llm.invoke(prompt)

        content = response.content

        # -----------------------------------------
        # Convert response to string
        # -----------------------------------------

        if isinstance(content, str):

            text = content

        elif isinstance(content, list):

            parts = []

            for item in content:

                if isinstance(item, str):

                    parts.append(item)

                elif isinstance(item, dict):

                    if "text" in item:
                        parts.append(
                            str(item["text"])
                        )

            text = "".join(parts)

        else:

            text = str(content)

        # -----------------------------------------
        # Fix character-by-character newlines
        # -----------------------------------------

        lines = text.splitlines()

        if len(lines) > 5:

            non_empty = [
                line.strip()
                for line in lines
                if line.strip()
            ]

            # Detect:
            # C
            # u
            # s
            # t
            # o
            # m
            # e
            # r

            if all(
                len(line) <= 2
                for line in non_empty
            ):

                text = "".join(
                    non_empty
                )

        # -----------------------------------------
        # Normal cleanup
        # -----------------------------------------

        text = text.strip()

        return text