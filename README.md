# LANGCHAIN-CHAT-PDF-TUTORIAL



## Libraries Used

* **LangChain:** For building language model applications.
* **PyPDF2:** For reading and extracting text from PDF documents.
* **python-dotenv:** For loading environment variables from a `.env` file.
* **Streamlit:** For creating interactive web applications.
* **FAISS (faiss-cpu):** For efficient similarity search and vector storage.
* **LangChain Community (langchain-community):** Provides community contributed tools and integrations for LangChain.
* **OpenAI:** For accessing OpenAI's language models.
* **tiktoken:** For fast BPE tokenization.


# Ask Your PDF 📄💬

This project is a **PDF-based Question Answering System** built using **LangChain, FAISS, OpenAI embeddings, and Streamlit**. It allows users to upload a PDF file, extract its text, convert it into embeddings, and then ask questions about the content.

## 🚀 Features
- **Upload PDF Files** 📂
- **Extract Text from PDFs** 📝
- **Chunk and Process Text** ⚡
- **Convert Text into Embeddings using OpenAI** 🧠
- **Store and Search Using FAISS Vector Database** 🔍
- **Answer User Questions Based on PDF Content** 🤖
- **Streamlit UI for User Interaction** 🎨

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd your-repo-name
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
```
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project root and add your **OpenAI API Key**:
```env
OPENAI_API_KEY=your-api-key-here
```

## ▶️ Usage
Run the Streamlit app:
```bash
streamlit run app.py
```

## 📌 How It Works
1. Upload a **PDF file**.
2. Extracts text from the PDF.
3. Splits the text into **chunks**.
4. Converts chunks into **embeddings** using OpenAI.
5. Stores embeddings in **FAISS Vector Database**.
6. Accepts user questions and retrieves the most relevant chunks.
7. Uses **OpenAI's LLM** to generate an answer.

## 📦 Dependencies
- **Python** (>=3.8)
- **Streamlit**
- **PyPDF2**
- **LangChain**
- **OpenAI API**
- **FAISS**

## 🤝 Contributing
Feel free to contribute by creating **issues** or **pull requests**!

## 📜 License
This project is licensed under the **MIT License**.

---

### ✨ Future Improvements
- Support for **multiple PDFs**.
- Option to select **different LLM models**.
- Improved **UI and user experience**.
- Caching mechanism for **faster responses**.

---
## 🔹 OpenAI Callback Output Example
```
response = chain.run(input_documents = docs, question=user_question)
Tokens Used: 1027
        Prompt Tokens: 980
                Prompt Tokens Cached: 0
        Completion Tokens: 47
                Reasoning Tokens: 0
Successful Requests: 1
Total Cost (USD): $0.0015639999999999999
```


