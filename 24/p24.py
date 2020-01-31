TARGET = 24

def calculate24_recur(nums, seq):
    if len(nums) == 1:
        if nums[0] == TARGET:
            return (True, seq)
        else:
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
                (result, sequence) = calculate24_recur([num] + new_list, seq + ["%d%s%d" % (a, op, b)])
                if result:
                    return (result, sequence)
    return (False, [])

def calculate24(nums):
    return calculate24_recur(nums, [])

if __name__ == "__main__":
    for i in range(1, 11):
        for j in range(i, 11):
            for k in range(j, 11):
                for l in range(k, 11):
                    nums = [i, j, k, l]
                    print (nums, calculate24(nums))
    pass


        

    