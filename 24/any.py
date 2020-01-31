# 任意张牌计算任意数
TARGET = 60

def calculate_target_recur(nums, seq):
    if len(nums) == 2:
        a = max(nums[0], nums[1])
        b = min(nums[0], nums[1])
        new_nums = dict()
        new_nums["+"] = a + b
        new_nums["-"] = a - b
        new_nums["*"] = a * b
        if (b != 0):
            new_nums["/"] = a / b
        for op, num in new_nums.items():
            if num == TARGET:
                return (True, seq + ["%d%s%d=%d" % (a, op, b, num)])
        return (False, [])
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            a = max(nums[i], nums[j])
            b = min(nums[i], nums[j])
            new_nums = dict()
            new_nums["+"] = a + b
            new_nums["-"] = a - b
            new_nums["*"] = a * b
            if (b != 0):
                new_nums["/"] = a / b
            new_list = []
            for k in range(len(nums)):
                if k != i and k != j:
                    new_list.append(nums[k])
            for op, num in new_nums.items():
                (result, sequence) = calculate_target_recur([num] + new_list, seq + ["%d%s%d=%d" % (a, op, b, num)])
                if result:
                    return (result, sequence)
    return (False, [])

def calculate_target(nums):
    return calculate_target_recur(nums, [])

def generateNcards(n, min, max, seq):
    if n == 0:
        yield seq
    else:
        for i in range(min, max+1):
            yield from generateNcards(n-1, i, max, seq + [i])

if __name__ == "__main__":
    for comp in generateNcards(6, 1, 10, []):
        print (comp, calculate_target(comp))


        

    