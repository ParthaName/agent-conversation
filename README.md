# 🧠 Multi-Agent AI Discussion System

An experimental multi-agent AI system where two autonomous agents discuss a given topic while an evaluator monitors topic drift and conversation type in real time.

Built using:
- **CrewAI** (Agent orchestration)
- **Groq API** (LLM inference)
- **LiteLLM** (Provider routing)
- **Gradio** (UI streaming interface)

## 🚀 Features

- 👤 **Two autonomous AI agents** with distinct personalities
- 🔁 **Turn-based structured discussion**
- 📊 **Evaluator agent detects**:
  - Topic drift
  - Conversation type
  - Repetition
- ⚡ **Real-time streaming** via Gradio
- 🔄 **Automatic retry** on Groq rate limits
- 🧠 **Clean modular architecture**
- 🧪 **Built for multi-agent behavior experimentation**

## 🏗 Project Structure

```
agent-conversation/
│
├── agents/
│   ├── base_llm.py
│   ├── discussion_agents.py
│   └── evaluator_agent.py
│
├── orchestrator/
│   └── conversation_manager.py
│
├── config/
│   └── settings.py
│
├── ui/
│   └── gradio_app.py
│
├── .env
├── run.py
└── README.md
```

## 🧩 System Architecture

```
User Topic
     ↓
Conversation Orchestrator
     ↓
Agent 1 ↔ Agent 2 (Turn-based loop)
     ↓
Evaluator Agent
     ↓
Drift Detection / Stop Condition
     ↓
Gradio Streaming UI
```

## 🧠 Agents

### Agent 1 — Senior Data Scientist
- Analytical
- Skeptical
- Evidence-driven
- Technical focus

### Agent 2 — AI Futurist
- Visionary
- Speculative
- Big-picture thinker
- Philosophical angle

### Evaluator Agent
- Detects topic drift
- Classifies conversation type:
  - Debate
  - Agreement
  - Speculative
  - Technical
  - Philosophical
  - Repetitive
- Stops discussion if drift detected

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd agent-conversation
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install crewai litellm gradio python-dotenv
```

### 4️⃣ Add Groq API Key

Create a `.env` file in project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from:
https://console.groq.com/keys

### 5️⃣ Run the App

```bash
python run.py
```

Open:
```
http://127.0.0.1:7860
```

## 🔥 Recommended Groq Models

- **For experimentation** (low token usage):
  - `groq/llama-3.1-8b-instant`

- **For high reasoning quality**:
  - `groq/llama-3.3-70b-versatile`

## ⚠️ Rate Limit Handling

The system includes automatic retry logic when:
- Tokens per minute (TPM) exceeded
- Requests per minute exceeded

It waits and resumes automatically.

**Groq Free Tier Limits:**
- 30 Requests / minute
- 12,000 Tokens / minute

## 🧪 Experiment Ideas

- Change temperature → observe drift behavior
- Increase max turns → analyze stability
- Trim history window → reduce token usage
- Swap models (8B vs 70B)
- Add embedding-based drift scoring
- Add self-reflection turn every 4 turns

## 🧠 Research Applications

This project can be used for:
- Multi-agent alignment studies
- Topic drift analysis
- Emergent behavior observation
- Debate simulation
- Personality amplification testing
- LLM interaction experiments

## 📈 Future Improvements

- Token-level streaming
- JSON-based evaluator parsing
- Conversation similarity scoring (embeddings)
- Automatic temperature adjustment
- LangGraph implementation
- Conversation entropy tracking
- Agent memory compression

## 🏆 Key Learnings

This project highlights differences between:

| Framework | LLM Call Style |
|-----------|----------------|
| LangChain  | `.invoke()`    |
| CrewAI    | `.call()`      |

It also demonstrates:
- LiteLLM provider routing
- Groq rate-limit management
- Multi-agent orchestration patterns

## 👨‍💻 Author

Built as a multi-agent AI experimentation system.
