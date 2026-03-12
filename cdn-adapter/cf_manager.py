import CloudFlare

# Cloudflare API Token
# 这里使用 Token 而不是 Global API Key
# 因为 Token 权限可以限制，更安全
CF_TOKEN = "a2bae291b90a0d3d67ed07a51b690b5c70291"

# Zone ID 是 Cloudflare 给每个域名的唯一ID
ZONE_ID = "7516f976a2edf2b62e4aba2520bef973"

# 初始化 Cloudflare API 客户端
cf = CloudFlare.CloudFlare(token=CF_TOKEN)


def get_dns_records():
    """
    获取当前域名所有 DNS 记录

    为什么需要？
    ----------------
    在智能网络系统中，我们需要：
    1 判断当前DNS指向哪里
    2 判断是否需要切换CDN
    """

    dns_records = cf.zones.dns_records.get(ZONE_ID)

    return dns_records


def update_dns(record_id, new_ip):

    """
    修改 DNS 记录

    为什么需要？
    ----------------
    如果系统检测到：

    线路A latency = 300ms
    线路B latency = 90ms

    那么系统可以自动：

    DNS → 切换到B线路
    """

    data = {
        'type': 'A',
        'name': 'ai',
        'content': new_ip,
        'ttl': 120
    }

    cf.zones.dns_records.put(ZONE_ID, record_id, data=data)

    return "DNS updated"