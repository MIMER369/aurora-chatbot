import os
import json

def load_api_key():
    # Priority: environment variable > config.json
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key
    try:
        with open("config.json") as f:
            cfg = json.load(f)
        return cfg.get("openai_api_key")
    except FileNotFoundError:
        raise RuntimeError("OpenAI API key not found. Set OPENAI_API_KEY or create config.json.")

def load_products():
    try:
        with open("products.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
