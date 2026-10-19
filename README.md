# 🧳 Wanderlust - Multi-Agent Smart Travel Planner

A sophisticated multi-agent system for intelligent trip planning using **LangGraph**, **LangChain**, **Ollama** (local LLM), **Supabase** (pgvector), and **Streamlit**.

## 🎯 Features

### Core Capabilities
- **🤝 Multi-Agent Orchestration**: 6 specialized agents (Memory, Supervisor, Workers, Explorer, Arbiter, Composer)
- **⚡ Parallel Execution**: Workers (Flight, Hotel, Weather, Visa, Attractions) run simultaneously via Send API
- **🧠 Smart Personalization**: Learns from past trips using pgvector similarity search
- **💡 Novel Suggestions**: Explorer Agent proposes destinations you haven't tried
- **💰 Budget Intelligence**: Detects conflicts (>₹15,000 or 30% of budget), suggests trade-offs
- **👤 Human-in-the-Loop**: Approval gates before expensive bookings and final itinerary
- **📅 Day-by-Day Planning**: Detailed itinerary with weather, costs, visa checklist
- **🌐 Offline Demo**: Runs completely offline with pre-cached data

## 🏗️ Architecture

```
INPUT (destination, dates, budget, preferences)
    ↓
MEMORY AGENT (load profile + top-3 similar past trips via pgvector)
    ↓
SUPERVISOR (parse request)
    ↓
PARALLEL WORKERS (Send API fan-out)
    ├→ FLIGHT AGENT (fast-flights lib + cache)
    ├→ HOTEL AGENT (Playwright scraper + cache)
    ├→ WEATHER AGENT (Open-Meteo)
    ├→ VISA AGENT (passport-index-dataset + RAG)
    └→ ATTRACTIONS AGENT (Overpass API + Wikipedia)
    ↓
EXPLORER AGENT (propose novel destination)
    ↓
BUDGET ARBITER (compare plans, detect conflicts, replan if needed)
    ↓
ITINERARY COMPOSER (build day-by-day plan)
    ↓
[HITL #1: Approve expensive items]
    ↓
[HITL #2: Final itinerary approval]
    ↓
MEMORY WRITE (save trip + feedback)
```

## 📁 Project Structure

```
wanderlust/
├── requirements.txt                # All dependencies
├── .env.example                   # Configuration template
├── README.md                      # This file
├── QUICKSTART.md                  # Quick start guide
├── IMPLEMENTATION_SUMMARY.md      # Implementation details
├── DELIVERABLES.md               # Complete checklist
│
├── src/
│   ├── config.py                 # Environment & settings
│   ├── schema.py                 # Pydantic models
│   ├── database.py               # Supabase CRUD + pgvector
│   ├── graph.py                  # LangGraph state machine
│   ├── tools/                    # Data tools
│   │   ├── flight.py
│   │   ├── hotel.py
│   │   ├── weather.py
│   │   ├── visa.py
│   │   ├── attractions.py
│   │   ├── geocoding.py
│   │   └── currency.py
│   └── agents/                   # Multi-agent logic
│       ├── memory.py
│       ├── supervisor.py
│       ├── worker.py
│       ├── explorer.py
│       ├── arbiter.py
│       └── composer.py
│
├── demo_data/                    # Pre-cached demo data
│   ├── flights.json
│   ├── hotels.json
│   ├── weather.json
│   ├── visa_rules.json
│   ├── attractions.json
│   └── past_trips.json
│
├── tests/
│   ├── test_graph.py            # 20+ end-to-end tests
│   ├── test_agents.py
│   └── test_tools.py
│
├── app_streamlit.py             # Interactive Streamlit UI
└── test_demo.py                 # CLI demo script
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env if using Ollama or Groq
```

### 3. Run Demo
```bash
# Option A: Command-line demo (shows 2 trips with personalization)
python test_demo.py

# Option B: Interactive Streamlit UI
streamlit run app_streamlit.py

# Option C: Run tests
pytest tests/ -v
```

## 🔑 Requirements Met

✅ Multi-agent system (6 agents)
✅ LangGraph orchestration with Send API
✅ Parallel workers (5 simultaneous)
✅ Local LLM support (Ollama)
✅ Supabase + pgvector for similarity search
✅ All 7 tools with caching & fallbacks
✅ Memory-based personalization
✅ Explorer Agent (novel suggestions)
✅ Budget Arbiter (conflict detection)
✅ HITL gates (2 approval points)
✅ Offline demo mode
✅ Complete documentation & tests

## 📚 Documentation

- **README.md** - This file
- **QUICKSTART.md** - Quick start guide
- **IMPLEMENTATION_SUMMARY.md** - Technical details
- **DELIVERABLES.md** - Feature checklist

## 🧪 Testing

Run comprehensive test suite:
```bash
pytest tests/ -v
```

## ⚙️ Configuration

Edit `.env` to customize:
- Ollama URL and model
- Groq API key (fallback)
- Supabase credentials
- Budget thresholds
- Cache TTLs

---

**Built with ❤️ for intelligent travel planning.**
