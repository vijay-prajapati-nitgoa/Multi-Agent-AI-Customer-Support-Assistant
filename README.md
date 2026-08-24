# 🤖 Multi-Agent AI Customer Support Assistant

An AI-powered customer support assistant that combines **Retrieval-Augmented Generation (RAG)**, **multi-agent routing**, **FAISS vector search**, and **LLMs** to provide accurate and context-aware responses from uploaded PDF knowledge bases.

---

## ✨ Features

- 📄 PDF Upload
- 🔍 PDF Text Extraction
- 🖼️ OCR Support for scanned PDFs
- ✂️ Text Chunking
- 🧠 Document Embeddings
- 🔎 FAISS Vector Search
- 🤖 Retrieval-Augmented Generation (RAG)
- 🎯 Intent Detection
- 👥 Multi-Agent Query Routing
- 💳 Billing Agent
- 🛠️ Technical Agent
- 📦 Product Agent
- 😟 Complaint Agent
- ❓ FAQ Agent
- 💬 Chat History
- 🗑️ Chat Management
- 🌐 Next.js Web Interface
- ⚡ FastAPI Backend
- 🦙 Ollama LLM Integration
- 🗄️ MongoDB Database

---

## 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │      Next.js        │
                         │    Frontend UI      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       FastAPI       │
                         │      Backend        │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
          ┌──────────────────┐            ┌──────────────────┐
          │ Intent Detector  │            │   RAG Pipeline   │
          └────────┬─────────┘            └────────┬─────────┘
                   │                               │
                   ▼                               ▼
          ┌──────────────────┐            ┌──────────────────┐
          │   Agent Router   │            │ FAISS Vector DB  │
          └────────┬─────────┘            └────────┬─────────┘
                   │                               │
        ┌──────────┼──────────┐                    ▼
        │          │          │            ┌──────────────────┐
        ▼          ▼          ▼            │    Retriever     │
     Billing   Technical   Product         └────────┬─────────┘
        │          │          │                     │
        └──────────┼──────────┘                     ▼
                   │                       ┌──────────────────┐
              Complaint                    │  Ollama / LLM    │
                   │                       └──────────────────┘
                  FAQ
🔄 How It Works
1. Upload PDF

The user uploads a customer-support knowledge-base PDF.

2. Extract Text

The system first attempts normal PDF text extraction.

If the PDF is scanned or image-based, Tesseract OCR is used.

3. Split Documents

The extracted text is divided into smaller overlapping chunks.

4. Create Embeddings

The document chunks are converted into vector embeddings.

5. Store in FAISS

The embeddings are stored in a FAISS vector database.

6. Ask a Question

The user asks a question through the chat interface.

Example:

What is the refund policy?
7. Retrieve Relevant Information

The retriever searches the FAISS database and finds the most relevant information.

8. Detect Intent

The Intent Detector identifies the type of customer query.

Example:

"What is the refund policy?"
             ↓
       Billing Agent
9. Route to Agent

The Agent Router sends the query to the appropriate specialized agent.

10. Generate Response

The selected agent uses the RAG pipeline and Ollama LLM to generate the answer.

11. Display Response

The response is displayed in the Next.js chat interface.

🤖 Multi-Agent System
Agent	Responsibility
💳 Billing Agent	Payments, refunds, invoices and subscriptions
🛠️ Technical Agent	Login, password, installation and technical issues
📦 Product Agent	Products, features, specifications and pricing
😟 Complaint Agent	Customer complaints and dissatisfaction
❓ FAQ Agent	Frequently asked questions and general information

The system can also handle queries containing multiple intents.

Example:

I paid yesterday but my premium subscription is still locked.

The system can identify:

Billing Agent
+
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
RAG
FAISS
Embeddings
Ollama
LLMs
Document Processing
PyMuPDF
PyTesseract
Tesseract OCR
Recursive Character Text Splitter
Database
MongoDB
📁 Project Structure
Multi-Agent-AI-Customer-Support-Assistant/
│
├── backend/
│   │
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
│   │
│   ├── database/
│   │
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
│   │
│   ├── app/
│   ├── components/
│   ├── public/
│   ├── services/
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md
⚙️ Installation
1. Clone the Repository
git clone https://github.com/vijay-prajapati-nitgoa/Multi-Agent-AI-Customer-Support-Assistant.git

cd Multi-Agent-AI-Customer-Support-Assistant
2. Backend Setup

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r backend/requirements.txt
3. Install Ollama

Install Ollama and download the required model.

Example:

ollama pull gemma3:4b

Run Ollama:

ollama run gemma3:4b
4. Configure Environment Variables

Create a .env file if required:

OLLAMA_MODEL=gemma3:4b
MONGODB_URL=your_mongodb_connection_string
DATABASE_NAME=your_database_name

Do not commit .env files or API keys to GitHub.

5. Start the Backend
uvicorn backend.main:app --reload

Backend:

http://localhost:8000

FastAPI documentation:

http://localhost:8000/docs
6. Start the Frontend

Open another terminal:

cd frontend
npm install
npm run dev

Open:

http://localhost:3000
💬 Example Questions
FAQ
What are your working hours?
Billing
What is the refund policy?
Technical
I cannot login to my account.
Product
What features does your product provide?
Complaint
I am unhappy with your service.
Multiple Intent
I paid yesterday but my premium subscription is still locked.
🔐 Security

Do not upload sensitive files or credentials to GitHub.

The following should remain excluded:

.env
.env.local
node_modules/
.next/
venv/
.venv/
__pycache__/
API keys
Database credentials
Private customer documents

These files should be handled using .gitignore.

🚀 Future Improvements
Streaming LLM responses
User authentication
Multiple knowledge bases
Source citations
Improved intent classification
Conversation memory
Analytics dashboard
Cloud vector database
Production deployment
Automated RAG evaluation
🎯 Project Objective

The objective of this project is to build a scalable AI customer-support system that combines:

Multi-Agent Architecture
        +
Retrieval-Augmented Generation
        +
Vector Search
        +
Large Language Models
        +
FastAPI
        +
Next.js

to provide accurate and context-aware customer support using information from a company's knowledge base.

👨‍💻 Author

Vijay Prajapati

B.Tech – Electrical & Electronics Engineering
National Institute of Technology, Goa

