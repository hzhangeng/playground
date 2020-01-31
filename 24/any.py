# 任意张牌计算任意数
TARGET = 60

SIMPLE_CACHE = dict()

def calculate_target_recur(nums, seq):
    if len(nums) == 1:
        if nums[0] == TARGET:
            return (True, seq)
        else:
            return (False, [])
    nums.sort()
    cache_key = tuple(nums)
    if cache_key in SIMPLE_CACHE:
        return SIMPLE_CACHE[cache_key]
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
                    SIMPLE_CACHE[cache_key] = (result, sequence)
                    return SIMPLE_CACHE[cache_key]
    SIMPLE_CACHE[cache_key] = (False, [])
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


        

    