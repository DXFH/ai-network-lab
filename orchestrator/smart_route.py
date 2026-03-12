# Smart Route Engine
# 这个模块负责：
# 1 平滑网络 latency
# 2 计算线路评分
# 3 选择最佳线路

latency_history = {}

ALPHA = 0.3


def ewma(target, current_latency):

    """
    EWMA 平滑算法

    target: 网站
    current_latency: 当前检测值

    为什么需要？

    网络 latency 会波动，如果直接使用
    当前值会导致线路频繁切换。
    """

    if target not in latency_history:

        latency_history[target] = current_latency

    previous = latency_history[target]

    new_latency = ALPHA * current_latency + (1-ALPHA) * previous

    latency_history[target] = new_latency

    return new_latency


def choose_best(results):

    """
    根据 EWMA 结果选择最佳线路
    """

    best_target = None
    best_latency = 9999

    for r in results:

        if r["http"] == -1:
            continue

        smoothed = ewma(r["host"], r["http"])

        if smoothed < best_latency:

            best_latency = smoothed
            best_target = r["host"]

    return {
        "best_target": best_target,
        "latency": round(best_latency,2)
    }