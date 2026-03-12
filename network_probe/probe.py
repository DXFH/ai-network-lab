import socket
import requests
import time
from monitoring.metrics import latency_metric

targets = [
    "chat.openai.com",
    "claude.ai",
    "huggingface.co",
    "github.com"
]

def tcp_test(host, port=443):
    start = time.time()
    try:
        sock = socket.create_connection((host, port), timeout=5)
        sock.close()
        latency = round((time.time()-start)*1000,2)
    except:
        latency = -1

    return latency


def http_test(url):
    start = time.time()
    try:
        requests.get(url, timeout=5)
        latency = round((time.time()-start)*1000,2)
    except:
        latency = -1

    return latency


def run_probe():

    results = []

    for host in targets:

        tcp_latency = tcp_test(host)
        http_latency = http_test("https://" + host)

        results.append({
            "host":host,
            "tcp":tcp_latency,
            "http":http_latency
        })

    return results

def http_test(url):

    start = time.time()

    try:

        requests.get(url, timeout=5)

        latency = round((time.time()-start)*1000,2)

    except:

        latency = -1

    # 把数据发送给 Prometheus
    latency_metric.labels(target=url).set(latency)

    return latency