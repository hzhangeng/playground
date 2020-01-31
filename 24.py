def calculate24(nums, seq):
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
            if num == 24:
                print (seq + ["%d%s%d" % (a, op, b)])
                return True
        return False
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
                if (calculate24([num] + new_list, seq + ["%d%s%d" % (a, op, b)])):
                    return True
    return False

if __name__ == "__main__":
    print(calculate24([6, 4, 1, 1], []))
    print(calculate24([4, 4, 9, 10], []))
    pass


        

    