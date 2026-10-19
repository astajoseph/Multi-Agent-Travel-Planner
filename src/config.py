import os
from dotenv import load_dotenv

load_dotenv()

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

# LLM Fallback
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
USE_GROQ = os.getenv("USE_GROQ", "false").lower() == "true"

# Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# Application
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
DEMO_MODE = os.getenv("DEMO_MODE", "true").lower() == "true"

# Cache TTLs
CACHE_TTL_FLIGHTS_DAYS = int(os.getenv("CACHE_TTL_FLIGHTS_DAYS", "7"))
CACHE_TTL_HOTELS_DAYS = int(os.getenv("CACHE_TTL_HOTELS_DAYS", "30"))
CACHE_TTL_WEATHER_HOURS = int(os.getenv("CACHE_TTL_WEATHER_HOURS", "24"))

# Budget Thresholds
HITL_EXPENSIVE_ITEM_THRESHOLD = 15000  # INR
HITL_BUDGET_PERCENTAGE_THRESHOLD = 0.30

# Embedding
EMBEDDING_DIMENSION = 768
SIMILARITY_SEARCH_K = 3

# Replan
MAX_REPLAN_ROUNDS = 3
REPLAN_DATE_SHIFT_DAYS = 3
