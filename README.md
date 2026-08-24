🤖 Multi-Agent AI Customer Support Assistant using RAG and LLMs

An AI-powered customer support assistant that combines Retrieval-Augmented Generation (RAG), multi-agent routing, FAISS vector search, and LLMs to provide accurate and context-aware responses from uploaded PDF knowledge bases.

✨ Features
📄 PDF Upload — Upload customer-support knowledge-base PDFs.
🔍 PDF Text Extraction — Extracts text from standard PDFs.
🖼️ OCR Support — Uses Tesseract OCR for scanned/image-based PDFs.
✂️ Text Chunking — Splits documents into overlapping chunks for better retrieval.
🧠 Embeddings — Converts document chunks into vector representations.
🔎 FAISS Vector Search — Retrieves relevant information from the knowledge base.
🤖 RAG Pipeline — Provides retrieved context to the LLM before generating an answer.
🎯 Intent Detection — Identifies the type of customer query.
👥 Multi-Agent System — Routes queries to specialized agents.
💳 Billing Agent — Handles payments, invoices, refunds, and subscriptions.
🛠️ Technical Agent — Handles login, password, installation, and technical issues.
📦 Product Agent — Handles products, features, specifications, pricing, and comparisons.
😟 Complaint Agent — Handles customer complaints professionally.
❓ FAQ Agent — Handles frequently asked questions.
💬 Chat History — Stores and retrieves previous conversations using MongoDB.
🗑️ Chat Management — Create, open, and delete conversations.
🌐 Modern Web Interface — Built using Next.js.
⚡ FastAPI Backend — Provides REST APIs for the application.
🏗️ Architecture
                    ┌──────────────────────┐
                    │      Next.js         │
                    │    Frontend UI       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │       Backend        │
                    └──────────┬───────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌─────────────────┐          ┌─────────────────┐
       │ Intent Detector │          │   RAG Pipeline  │
       └────────┬────────┘          └────────┬────────┘
                │                            │
                ▼                            ▼
       ┌─────────────────┐          ┌─────────────────┐
       │  Multi-Agent    │          │ FAISS Vector DB │
       │     Router      │          └────────┬────────┘
       └────────┬────────┘                   │
                │                            ▼
      ┌─────────┼─────────┐          ┌─────────────────┐
      ▼         ▼         ▼          │    Retriever    │
   Billing  Technical  Product       └────────┬────────┘
      │         │         │                   │
      ├─────────┼─────────┤                   ▼
      │    Complaint      │          ┌─────────────────┐
      │       FAQ         │          │      LLM        │
      └───────────────────┘          │     Ollama      │
                                     └─────────────────┘
🔄 How It Works
1. Upload Knowledge Base

The user uploads a PDF containing company/customer-support information.

2. Extract Text

The backend first attempts normal PDF text extraction.

If the PDF is scanned or image-based, Tesseract OCR is used.

3. Split Documents

The extracted content is divided into smaller overlapping chunks using a recursive text splitter.

4. Generate Embeddings

The chunks are converted into embeddings.

5. Store in FAISS

The embeddings are stored in a FAISS vector database.

6. Ask a Question

The user asks a question through the chat interface.

Example:

What is your refund policy?
7. Retrieve Relevant Information

The RAG retriever searches FAISS for the most relevant document chunks.

8. Detect Intent

The Intent Detector determines the appropriate agent.

For example:

"What is your refund policy?"
        ↓
Billing Agent
9. Generate Response

The relevant knowledge-base context and agent instructions are passed to the LLM.

10. Return Answer

The generated answer is displayed in the Next.js chat interface and saved to chat history.

🤖 Agents
Agent	Responsibility
💳 Billing Agent	Payments, refunds, invoices, subscriptions
🛠️ Technical Agent	Login, password, installation, errors
📦 Product Agent	Products, features, specifications, pricing
😟 Complaint Agent	Customer complaints and dissatisfaction
❓ FAQ Agent	Working hours, contact, location, FAQs
🧠 General/RAG	General knowledge-base questions

The system also supports multiple intents in a single query.

Example:

I paid yesterday but my premium is still locked.

Possible intents:

Billing Agent
Technical Agent
🛠️ Tech Stack
Frontend
Next.js
JavaScript / TypeScript
HTML
CSS
Backend
Python
FastAPI
AI / RAG
LangChain
Retrieval-Augmented Generation (RAG)
Embeddings
FAISS
Ollama
LLMs
Document Processing
PyMuPDF
Tesseract OCR
PyTesseract
Recursive Character Text Splitter
Database
MongoDB
📁 Project Structure
Multi-Agent-AI-Customer-Support-Assistant/
│
├── backend/
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── billing.py
│   │   ├── complaint.py
│   │   ├── faq.py
│   │   ├── intent_detector.py
│   │   ├── product.py
│   │   ├── response_aggregator.py
│   │   ├── response_generator.py
│   │   ├── router.py
│   │   └── technical.py
│   │
│   ├── api/
│   ├── database/
│   ├── models/
│   │
│   ├── rag/
│   │   ├── document_loader.py
│   │   ├── embeddings.py
│   │   ├── prompt.py
│   │   ├── rag_pipeline.py
│   │   ├── retriever.py
│   │   ├── text_splitter.py
│   │   └── vector_store.py
│   │
│   ├── services/
│   │   └── llm_service.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Multi-Agent-AI-Customer-Support-Assistant.git

cd Multi-Agent-AI-Customer-Support-Assistant
2. Backend Setup

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r backend/requirements.txt
3. Install and Run Ollama

Install Ollama and download the model used by your project.

For example:

ollama pull gemma3:4b

Start Ollama:

ollama run gemma3:4b
4. Configure Environment Variables

Create a .env file if required by your configuration.

Example:

MONGODB_URL=your_mongodb_connection_string
DATABASE_NAME=your_database_name
OLLAMA_MODEL=gemma3:4b

Never commit .env files or API keys to GitHub.

5. Start FastAPI

From the project directory:

uvicorn backend.main:app --reload

Backend:

http://localhost:8000

API documentation:

http://localhost:8000/docs
6. Start Next.js

Open another terminal:

cd frontend
npm install
npm run dev

Then open:

http://localhost:3000
💬 Example Queries
FAQ
What are your working hours?
Billing
What is your refund policy?
Technical
I cannot login to my account.
Product
What features does your product provide?
Complaint
I am unhappy with your service.
Multiple Intent
I paid yesterday but my premium subscription is still locked.

The system can identify both Billing and Technical intents.

🔐 Security

The following files should not be uploaded to GitHub:

.env
.env.local
node_modules/
.venv/
venv/
__pycache__/
.next/
uploaded PDFs containing private information
API keys
database credentials

These are excluded using .gitignore.

🚀 Future Improvements
Cloud-based LLM deployment
Streaming responses
Authentication and authorization
Multiple knowledge bases
Source citations in responses
Improved intent classification using an LLM
Conversation memory
Analytics dashboard
Cloud vector database
Production deployment
Automated RAG evaluation
🎯 Project Goal

The goal of this project is to build a scalable AI customer-support assistant that combines:

Multi-Agent Architecture
        +
RAG
        +
Vector Search
        +
LLMs
        +
FastAPI
        +
Next.js

to provide reliable and context-aware customer support using information from a company's knowledge base.

👨‍💻 Author

Vijay Prajapati

B.Tech – Electrical & Electronics Engineering
National Institute of Technology, Goa
