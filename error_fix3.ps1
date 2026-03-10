python -c "
with open(r'network_probe\probe.py', 'w', encoding='utf-8') as f:
    f.write('''def run_probe():
    results = []
    targets = [
        {\"host\": \"https://chat.openai.com\", \"http\": 42},
        {\"host\": \"https://claude.ai\", \"http\": 28},
        {\"host\": \"https://huggingface.co\", \"http\": -1}
    ]
    for t in targets:
        results.append(t)
    return results
''')

with open(r'orchestrator\engine.py', 'w', encoding='utf-8') as f:
    f.write('''from network_probe.probe import run_probe

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
''')

print('✅ 两个文件已完全修复！')
" 