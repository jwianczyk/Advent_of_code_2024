def day2(arr:list[list[int]]) -> int:
    # Either increasing or decreasing order 
    # Difference of at least one and at max three    
    res_part1 = list(map(check_list, arr))
    print(list(enumerate(res_part1, 1)))
    return res_part1.count(True)

def check_list(input_arr: list[int]) -> bool:
    res:bool = True
    counter = 1
    sorting_global = None
    while counter is not len(input_arr):
        p1 = input_arr[counter - 1]
        p2 = input_arr[counter]
        num = p1 - p2
        sorting = 'Asc' if num < 0 else 'Desc'
        if (sorting != sorting_global and sorting_global is not None) or res is False:
            return False
        sorting_global = sorting if sorting_global is None else None
        # print(p1, p2, num, res, sorting)
        if res is False:
            return res
        match sorting:
            case 'Asc':
                res = True if 0 > num > -4 else False
            case 'Desc':
                res = True if 0 < num < 4 else False
        counter += 1
    return res

def parse_input(path: str) -> list[list[int]]:
    res = []
    with open(path, 'r') as f:
        for line in f:
            line = line.replace('/n', '')
            res.append(list(map(int, line.split(' '))))
    return res
            

if __name__ == '__main__':
    print(day2(parse_input('input.txt')))
