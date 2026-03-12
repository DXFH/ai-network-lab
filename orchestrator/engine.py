from network_probe.probe import run_probe

def choose_best_route():

    results = run_probe()

    best = None
    best_latency = 9999

    for r in results:

        if r["http"] != -1 and r["http"] < best_latency:

            best_latency = r["http"]
            best = r["host"]

    return {
        "best_target":best,
        "latency":best_latency
    }
from network_probe.probe import run_probe
from orchestrator.smart_route import choose_best


def choose_best_route():

    results = run_probe()

    best = choose_best(results)

    return best