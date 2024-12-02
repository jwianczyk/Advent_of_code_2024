def day2(arr:list[list[int]]) -> int:
    # Either increasing or decreasing order 
    # Difference of at least one and at max three
    res_part1 = list(map(check_list, arr))
    return res_part1.count(True)

def check_list(input_arr: list[int]) -> bool:
    res: list[bool] = []
    counter = 1
    sorting_global = None
    while counter is not len(input_arr):
        p1 = input_arr[counter - 1]
        p2 = input_arr[counter]
        num = p1 - p2
        sorting = 'Asc' if num < 0 else 'Desc'
        if sorting != sorting_global and sorting_global is not None:
            return False
        if sorting_global is None:
            sorting_global = sorting
        match sorting:
            case 'Asc':
                res.append(True if -1 >= num >= -3 else False)
            case 'Desc':
                res.append(True if 1 <= num <= 3 else False)
        counter += 1
    return all(res)

def parse_input(path: str) -> list[list[int]]:
    res = []
    with open(path, 'r') as f:
        for line in f:
            line = line.replace('/n', '')
            res.append(list(map(int, line.split(' '))))
    return res
            

if __name__ == '__main__':
    print(day2(parse_input('input.txt')))
