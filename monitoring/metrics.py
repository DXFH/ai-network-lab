from prometheus_client import Gauge

# Gauge 类型表示一个数值指标
# 例如 latency

latency_metric = Gauge(
    'network_latency',
    'Latency to AI services',
    ['target']
)