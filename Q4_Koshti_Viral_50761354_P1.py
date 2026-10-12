def ascending_sort(cities):
    arr = cities[:]

    def city_key(city):
        return (city[1], -city[0])

    def median_of_three(a, b, c):
        if a < b:
            if b < c:
                return b
            return c if a < c else a
        else:
            if a < c:
                return a
            return c if b < c else b

    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        while low < high:
            mid = (low + high) // 2

            pivot = median_of_three(
                city_key(arr[low]), city_key(arr[mid]), city_key(arr[high])
            )

            lt = low
            i = low
            gt = high

            while i <= gt:
                current = city_key(arr[i])

                if current < pivot:
                    arr[lt], arr[i] = arr[i], arr[lt]
                    lt += 1
                    i += 1
                elif current > pivot:
                    arr[i], arr[gt] = arr[gt], arr[i]
                    gt -= 1
                else:
                    i += 1

            left_size = lt - low
            right_size = high - gt

            if left_size < right_size:
                if gt + 1 < high:
                    stack.append((gt + 1, high))
                high = lt - 1
            else:
                if low < lt - 1:
                    stack.append((low, lt - 1))
                low = gt + 1

    return arr


def read_input():
    cities = []
    while True:
        try:
            city_input = input().strip()
        except EOFError:
            break
        if not city_input:
            continue
        city_info = city_input.split()
        city_index, population = int(city_info[0]), int(city_info[1])
        cities.append((city_index, population))

    return cities


if __name__ == "__main__":
    cities = read_input()
    sorted_cities = ascending_sort(cities)
    for city in sorted_cities:
        print(city[0], city[1])
