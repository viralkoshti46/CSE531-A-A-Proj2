def merge_sort(intervals):
    if len(intervals) <= 1:
        return intervals[:]

    mid = len(intervals) // 2
    left = merge_sort(intervals[:mid])
    right = merge_sort(intervals[mid:])

    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # Sort by finish time, then by start time.
        if (left[i][1], left[i][0]) <= (right[j][1], right[j][0]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def interval_scheduling_coving(n, intervals):
    ordered = merge_sort(intervals)
    selected_count = 0
    first_interval = None
    last_finish = None

    for start, finish in ordered:
        # Half-open intervals [start, finish): touching endpoints are compatible.
        if last_finish is None or start >= last_finish:
            if first_interval is None:
                first_interval = (start, finish)
            selected_count += 1
            last_finish = finish

    # The assignment specifies n >= 1, but retain a safe empty-input result.
    if first_interval is None:
        first_interval = (0, 0)

    return selected_count, first_interval


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
