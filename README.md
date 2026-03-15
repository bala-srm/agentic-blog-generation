# Agentic Blog Generation (LangGraph + LangChain + Groq)

This project builds a simple agentic workflow that generates:

1. A blog title from a topic
2. Full blog content from the generated title and topic

The workflow is implemented as a LangGraph state machine and uses Groq-hosted LLMs through LangChain.

## What This Project Does

- Accepts a `topic` as input
- Runs a `title_creation` node
- Runs a `content_generation` node
- Returns generated blog content in markdown style

## Tech Stack

- Python 3.13
- LangChain
- LangGraph
- LangChain Groq integration
- FastAPI and Uvicorn (included in dependencies for API use cases)

## Project Structure

```text
.
|- app.py
|- main.py
|- pyproject.toml
|- requirement.txt
|- src/
|  |- graphs/
|  |  |- graph_builder.py
|  |- llms/
|  |  |- groqllm.py
|  |- nodes/
|  |  |- blognode.py
|  |- states/
|  |  |- blogstate.py
```

## Setup

### 1) Clone and move into the project

```bash
git clone https://github.com/bala-srm/agentic-blog-generation.git
cd agentic-blog-generation
```

### 2) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

Option A (from `pyproject.toml` with `uv`):

```bash
uv sync
```

Option B (from `requirement.txt` with `pip`):

```bash
pip install -r requirement.txt
```

### 4) Add environment variables

Create a `.env` file in the root:

```env
GROQ_API_KEY="your_groq_api_key"
LANGCHAIN_API_KEY="your_langsmith_api_key_optional"
LANGCHAIN_PROJECT="BlogAgentic"
```

Important:

- Do not commit `.env`
- If you accidentally exposed any key, rotate it immediately

## How to Run

This repository currently provides the graph components. You can run a quick local test with a one-off Python command:

```bash
python - <<'PY'
from src.llms.groqllm import GroqLLM
from src.graphs.graph_builder import GraphBuilder

llm = GroqLLM().get_llm()
graph = GraphBuilder(llm).build_topic_graph()

result = graph.invoke({"topic": "Future of Agentic AI in Education"})
print(result)
PY
```

Expected flow:

1. `title_creation` generates a title
2. `content_generation` generates full blog content

## Core Components

- `GroqLLM` (`src/llms/groqllm.py`): initializes the Groq chat model
- `BlogState` (`src/states/blogstate.py`): defines state schema
- `BlogNode` (`src/nodes/blognode.py`): contains generation logic
- `GraphBuilder` (`src/graphs/graph_builder.py`): wires nodes and graph edges

## Troubleshooting

- Missing API key error:
	- Ensure `.env` exists and contains a valid `GROQ_API_KEY`
- Import errors:
	- Confirm virtual environment is active
	- Reinstall dependencies
- Type or state-shape errors while extending the graph:
	- Ensure node return values match `BlogState`

## Next Improvements

- Add a FastAPI endpoint in `app.py`
- Add tests for node outputs and graph transitions
- Add structured logging and retry policies

## License

No license file is included yet. Add one if you plan to distribute this project.
