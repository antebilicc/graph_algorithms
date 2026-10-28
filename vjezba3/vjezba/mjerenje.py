import time


def measure(f, *args, repeat=3):
    """Najkrace od repeat mjerenja vremena poziva f(*args), u sekundama."""
    best = float('inf')
    for _ in range(repeat):
        start = time.perf_counter()
        f(*args)
        best = min(best, time.perf_counter() - start)
    return best
