def day_1(arr: list, arr2: list) -> tuple[int, int]:
    # Calculate distance from both elements and sum them
    # Account for negative numbers
    res_part1 = sum(list(map(lambda x, y: abs(x - y), arr, arr2)))

    # Count number of occurrences from list 1 in list 2 and multiply element value by it
    # Then sum the list values
    res_part2 = sum(list(map(lambda x: x * arr2.count(x), arr)))
    return res_part1, res_part2

def parse_input(path: str) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []
    with open(path, 'r') as f:
        for line in f:
            list1.append(int(line.split('   ')[0]))
            list2.append(int(line.split('   ')[1]))
    f.close()
    list1.sort()
    list2.sort()
    return list1, list2

if __name__ == '__main__':
    input1, input2 = parse_input('input')
    part1, part2 = day_1(input1, input2)
    print(f'Day 1 part 1 answer: {part1}')
    print(f'Day 1 part 2 answer: {part2}')