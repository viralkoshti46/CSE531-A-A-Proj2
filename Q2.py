def interval_scheduling_coving(n, intervals):
    # Please write your algorithm here:
    # Implement merge sort; do not use sort() or sorted().
    # Select by earliest finish time, breaking ties by earlier start time.
    # A job may start exactly when the previous selected job finishes.
    # Return the maximum count and the first selected interval as (start, finish).

    # .................................
    return maximum, first_interval


def read_input():
    n = int(input())
    intervals = []
    for _ in range(n):
        s, f = map(int, input().split())
        intervals.append((s, f))
    return n, intervals


if __name__ == "__main__":
    n, intervals = read_input()
    maximum, first_interval = interval_scheduling_coving(n, intervals)
    print(maximum)
    print(first_interval[0], first_interval[1])
