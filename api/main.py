import sys
from pathlib import Path

# 🔥 自动把项目根目录加入 sys.path（解决所有子进程导入问题）
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import FastAPI
from network_probe.probe import run_probe
from orchestrator.engine import choose_best_route
import requests
import time
import threading
from orchestrator.scheduler import scheduler

app = FastAPI()

targets = [
    "https://chat.openai.com",
    "https://claude.ai",
    "https://huggingface.co"
]

@app.get("/network-test")
def network_test():
    results = []
    for url in targets:
        start = time.time()
        try:
            requests.get(url, timeout=5)
            latency = round((time.time() - start)*1000, 2)
        except:
            latency = -1
        results.append({"url": url, "latency": latency})
    return results

@app.get("/probe")
def probe():

    return run_probe()

@app.get("/route")
def route():

    return choose_best_route()

thread = threading.Thread(target=scheduler)
thread.daemon = True
thread.start()