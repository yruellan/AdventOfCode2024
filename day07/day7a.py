
f = open("data.txt", "r")
data = [
    (
        int(x.split(":")[0]), 
        list(map(int, x.split(":")[1].split()))
    )
    for x in f.readlines()
]

def get_results(nums):
    if len(nums) <= 1: return nums

    n = nums.pop()
    results = get_results(nums)
    return [x + n for x in results] + [x * n for x in results]

s = 0
for n, nums in data:
    res = get_results(nums)
    if n in res: s += n

print(s)