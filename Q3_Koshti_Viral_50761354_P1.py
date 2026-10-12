def FIFO_FF(k, n, m, requests):
    # FIFO cache: queue order is oldest loaded page to newest loaded page.
    fifo_cache = set()
    fifo_queue = []
    fifo_misses = 0

    for page in requests:
        if page in fifo_cache:
            continue

        fifo_misses += 1

        if len(fifo_cache) == k:
            evicted = fifo_queue.pop(0)
            fifo_cache.remove(evicted)

        fifo_cache.add(page)
        fifo_queue.append(page)

    # next_use[i] is the next index where requests[i] appears,
    # or m + 1 if it never appears again.
    next_use = [m + 1] * m
    next_position = {}

    for i in range(m - 1, -1, -1):
        page = requests[i]
        next_use[i] = next_position.get(page, m + 1)
        next_position[page] = i

    # Furthest-in-Future cache.
    ff_cache = set()
    next_use_of_page = {}
    ff_misses = 0

    for i, page in enumerate(requests):
        if page in ff_cache:
            next_use_of_page[page] = next_use[i]
            continue

        ff_misses += 1

        if len(ff_cache) == k:
            # Evict the page whose next request is latest.
            # m + 1 means it is never requested again.
            victim = max(ff_cache, key=lambda p: next_use_of_page[p])
            ff_cache.remove(victim)
            del next_use_of_page[victim]

        ff_cache.add(page)
        next_use_of_page[page] = next_use[i]

    return fifo_misses, ff_misses


def read_input():
    k, n, m = map(int, input().split())
    requests = []
    for _ in range(m):
        request = int(input())
        requests.append(request)
    return k, n, m, requests


if __name__ == "__main__":
    k, n, m, requests = read_input()
    fifo, ff = FIFO_FF(k, n, m, requests)
    print(fifo)
    print(ff)
