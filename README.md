# Intelli PDF: AI-Powered PDF Querying App

Intelli PDF is a modern web application that enables users to upload one or more PDF documents and ask natural language questions about them. Leveraging the power of **OpenAI's language models** and **Retrieval-Augmented Generation (RAG)** through **LangChain** and **Chroma**, DocuQuery provides intelligent, context-aware answers along with source references.

## ✨ Features

* 📥 Upload and process multiple PDFs
* 💬 Ask questions in plain English
* 🧠 Context-aware responses using OpenAI + Chroma
* 🗃️ Source citations included in answers
* ⚡ Sleek, responsive frontend with Tailwind CSS
* 🛠️ Modular, scalable Python backend using Flask

## 📁 Project Structure

```
DocuQuery/
├── app.py                       # Flask application entry point
├── requirements.txt             # Python dependencies
├── .env                         # API keys and config variables
│
├── templates/
│   └── index.html               # HTML template (Tailwind-based UI)
│
├── static/
│   ├── script.js                # Frontend logic
│   └── styles.css               # Custom styling (chat bubbles, animations)
│
├── services/
│   ├── pdf_service.py           # Handles PDF loading, splitting, embedding
│   └── query_service.py         # Handles semantic search and prompting
│
├── utils/
│   └── helpers.py               # Utility functions (e.g., file validation)
│
├── uploads/                    # Temporary uploaded files (auto-created)
├── data/                       # Temporary processing area for PDFs
├── chroma/                     # Chroma vector store (auto-generated)
```

## 🧪 Technologies Used

* **Python 3.9+**
* **Flask** – lightweight backend server
* **OpenAI API** – GPT model for responses
* **LangChain** – RAG implementation
* **Chroma** – vector store for document chunks
* **Tailwind CSS** – modern utility-first UI styling
* **HTML/CSS/JS** – responsive and accessible frontend

## ⚙️ Setup Instructions

1. Clone the Repo

```bash
git clone https://github.com/your-username/docuquery.git
cd docuquery
```

2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Set Up Environment Variables
Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key_here
```

5. Run the App

```bash
python app.py
```

Then go to `http://127.0.0.1:5000` in your browser.

## 📤 Deployment

You can deploy this app on platforms like:
* **Render** (easy Flask deployment)
* **Railway / Heroku** (add `Procfile` if needed)
* **Docker** (optional Dockerfile support)

Let me know if you need deployment support scripts!

## ✅ Roadmap / Possible Enhancements

* 🔐 User authentication & chat history
* 🌗 Light/dark mode toggle
* 🧠 Local LLM support (e.g., Ollama, GPT4All)
* 📜 Downloadable response logs
* 📱 Mobile-first UX polish

## 🙌 Acknowledgements

* LangChain
* Chroma
* OpenAI

## 📬 Contact

Have feedback or want to collaborate? Feel free to connect with me on LinkedIn or open an issue!
