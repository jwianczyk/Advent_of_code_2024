def day_1(arr: list, arr2: list) -> tuple[int, int]:
    arr.sort()
    arr2.sort()

    # Calculate distance from both elements and sum them
    # Account for negative numbers
    res_part1 = sum(list(map(lambda x, y: abs(x - y), arr, arr2)))

    # Count number of occurrences from list 1 in list 2 and multiply element value by it
    # Then sum the list values
    res_part2 = sum(list(map(lambda x: x * arr2.count(x), arr)))
    return res_part1, res_part2


if __name__ == '__main__':
    list1 = []
    list2 = []
    with open('input') as f:
        for line in f:
            list1.append(int(line.split('   ')[0]))
            list2.append(int(line.split('   ')[1]))
    f.close()

    part1, part2 = day_1(list1, list2)
    print(f'Day 1 part 1 answer: {part1}')
    print(f'Day 1 part 2 answer: {part2}')