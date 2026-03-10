import time
from orchestrator.engine import choose_best_route

def scheduler():

    while True:

        result = choose_best_route()

        print("Best Route:", result)

        time.sleep(300)