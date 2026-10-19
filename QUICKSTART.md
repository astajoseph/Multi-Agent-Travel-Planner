# 🚀 Wanderlust Quick Start Guide

## 3-Step Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure Environment
```bash
cp .env.example .env
```

### Step 3: Run Demo
```bash
# Option A: CLI demo (shows 2 trips with personalization)
python test_demo.py

# Option B: Interactive web UI
streamlit run app_streamlit.py

# Option C: Run tests
pytest tests/ -v
```

## 📊 Project Features

✅ Multi-agent orchestration (6 agents)
✅ Parallel workers (5 simultaneous)
✅ Smart personalization via pgvector
✅ Budget analysis with conflict detection
✅ HITL approval gates (2 points)
✅ Offline demo mode
✅ Complete documentation
✅ Comprehensive tests

## 📁 Project Structure

- **src/**: Core implementation
- **demo_data/**: Pre-cached data for offline demo
- **tests/**: Test suite
- **Documentation**: README, IMPLEMENTATION_SUMMARY, DELIVERABLES

## 🎯 Key Requirements Met

- ✅ LangGraph orchestration with Send API
- ✅ Ollama + Groq fallback
- ✅ Supabase + pgvector
- ✅ All 7 tools with caching
- ✅ Explorer Agent + Budget Arbiter
- ✅ HITL gates
- ✅ Offline demo

---

**Full documentation**: See README.md and IMPLEMENTATION_SUMMARY.md
