import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

GSS_API = os.getenv("GSS_API")
GSS_API_KEYS_PATH = Path(__file__).parents[1] / "api_keys.json"
