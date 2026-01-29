# Retrieval-Augmented Generation (RAG) Project

This project demonstrates a simple Retrieval-Augmented Generation (RAG) system using OpenAI's embeddings and chat models along with FAISS for fast similarity search.

## Project Structure

```
generativeAI/
|
├── main.py              # Main RAG script
├── API.txt              # API configuration and documentation
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignored files and folders
└── README.md            # Project documentation


##Areas for Improvement 
1.Dynamic Document loading
-Righ now doucments are hardcoded and also in data.tx 
-Could load from multiple  files or automatically split paragraphs  for large documents
2. Interactive User Experience
-currently, only a single question is asked 
- Could add an inter active loop or CLi Input for multiple questions

##Future project :
1. I really wanna make gen AI APP using langgraph and langchain 
more like all the architecture based. first i will make prototype and i will make an app.

## Features

- Embedding generation using OpenAI's text-embedding-3-small model
- Fast similarity search using FAISS (Facebook AI Similarity Search)
- Context-aware question answering with GPT-4o-mini
- Document retrieval based on semantic similarity

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Set your OpenAI API key:

On Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```

On macOS/Linux:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

Run the main script:

```bash
python main.py
```

The script will:
1. Initialize the FAISS vector store with document embeddings
2. Process a sample question ("What is RAG?")
3. Retrieve relevant documents based on semantic similarity
4. Generate an answer using the retrieved context and GPT-4o-mini

## Requirements

- Python 3.10+
- OpenAI API key (with valid billing)
- Dependencies listed in requirements.txt:
  - openai
  - numpy
  - faiss-cpu

## How It Works

1. **Embedding Generation**: Document text is converted to embeddings using OpenAI's text-embedding-3-small model
2. **Indexing**: Embeddings are indexed using FAISS for efficient similarity search
3. **Retrieval**: For a given query, the top-k most similar documents are retrieved
4. **Generation**: Retrieved documents are provided as context to GPT-4o-mini for answering the question

## Configuration

- API Key: Set the `OPENAI_API_KEY` environment variable with your OpenAI API key
- Model: Currently uses "text-embedding-3-small" for embeddings and "gpt-4o-mini" for chat completions
- Top-K: Default retrieval returns top 2 most relevant documents (configurable)

## Troubleshooting

If you encounter "insufficient_quota" errors:
1. Check your OpenAI account billing at https://platform.openai.com/account/billing/overview
2. Ensure you have a valid payment method
3. Verify you have sufficient API credits

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions.
