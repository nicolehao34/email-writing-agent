# email-writing-agent
AI agent that write emails for you based on natural language instructions, using langraph

Through this project, I wanted to learn

- langgraph, Langchain: for developing AI agents workflow.
- Langserve: simplify API development & deployment (using FastAPI).
- Google Gmail API, useful for workflow + productivity tools

# How It Works
- Email Monitoring: The system constantly checks for new emails in the agency's Gmail inbox using the Gmail API.
- Email Categorization: AI agents sort each email into predefined categories.
- Response Generation:
    - For complaints or feedback: The system quickly drafts a tailored email response.
    - For service/product questions: The system uses RAG to retrieve accurate information from agency documents and generates a response.
- Quality Assurance: Each draft email undergoes AI quality and formatting checks.
- Sending: Approved emails are sent to the client promptly, ensuring timely communication.


# Prerequisites

Prerequisites
Python 3.7+
Groq api key
Google Gemini api key (for embeddings)
Gmail API credentials