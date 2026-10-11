def FIFO_FF(k, n, m, requests):
    # Please write your algorithm here:
    # Return the FIFO and Furthest-in-Future cache-miss counts, respectively.

    # .................................
    return fifo, ff

#You are allowed to use some built-in functions, such as the Python heap library, including heapq.heapify(). 

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
