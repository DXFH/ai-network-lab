import requests


targets = {
    "openai": "https://chat.openai.com",
    "claude": "https://claude.ai",
    "huggingface": "https://huggingface.co"
}


def check_ai_access():

    results = {}

    for name, url in targets.items():

        try:

            requests.get(url, timeout=5)

            results[name] = "ok"

        except:

            results[name] = "blocked"

    return results