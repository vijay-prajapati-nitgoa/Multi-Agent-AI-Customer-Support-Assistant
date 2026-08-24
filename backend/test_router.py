from agents.intent_detector import IntentDetector

detector = IntentDetector()

tests = [
    "I want a refund",
    "I cannot login",
    "What is the product price?",
    "I am unhappy with your service",
    "What are your working hours?",
    "I paid yesterday but my premium is still locked"
]

for query in tests:
    print("\nQuery:", query)
    print("Agents:", detector.detect(query))