class IntentDetector:
    
    def detect(self, query):

        query = query.lower()

        billing = [
            "payment",
            "paid",
            "pay",
            "invoice",
            "refund",
            "subscription",
            "bill",
            "charge",
            "transaction",
            "premium"
        ]

        technical = [
            "error",
            "login",
            "password",
            "bug",
            "install",
            "installation",
            "locked",
            "not working",
            "unable",
            "crash",
            "failed",
            "failure"
        ]

        product = [
            "product",
            "price",
            "feature",
            "specification"
        ]

        complaint = [
            "complaint",
            "bad",
            "dissatisfied",
            "unhappy"
        ]

        faq = [
            "faq",
            "working hours",
            "contact",
            "location"
        ]

        agents = []

        if any(x in query for x in billing):
            agents.append("Billing Agent")

        if any(x in query for x in technical):
            agents.append("Technical Agent")

        if any(x in query for x in product):
            agents.append("Product Agent")

        if any(x in query for x in complaint):
            agents.append("Complaint Agent")

        if any(x in query for x in faq):
            agents.append("FAQ Agent")

        if not agents:
            agents.append("General Agent")

        return agents