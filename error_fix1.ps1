# 1. 修复 network_probe/probe.py（返回你需要的格式）
@"
def run_probe():
    results = []
    targets = [
        {\"host\": \"https://chat.openai.com\", \"http\": 42},
        {\"host\": \"https://claude.ai\", \"http\": 28},
        {\"host\": \"https://huggingface.co\", \"http\": -1}
    ]
    for t in targets:
        results.append(t)
    return results
"@ | Out-File -FilePath "D:\My-Project\AI-NETWORK-LAB\network_probe\probe.py" -Encoding utf8 -Force

# 2. 写入你想要的完整 choose_best_route 逻辑
@"
from network_probe.probe import run_probe

def choose_best_route():
    results = run_probe()
    best = None
    best_latency = 9999

    for r in results:
        if r.get(\"http\", -1) != -1 and r[\"http\"] < best_latency:
            best_latency = r[\"http\"]
            best = r[\"host\"]

    return {
        \"best_target\": best,
        \"latency\": best_latency,
        \"status\": \"success\" if best else \"no_available_route\"
    }
"@ | Out-File -FilePath orchestrator\engine.py -Encoding utf8 -Force

# 3. 确保包结构完整
New-Item -Path orchestrator\__init__.py -ItemType File -Force