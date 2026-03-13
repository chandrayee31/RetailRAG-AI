import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"


def generate_rag_answer(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)

    if response.status_code != 200:
        raise Exception(f"Ollama request failed: {response.text}")

    result = response.json()
    return result["response"]