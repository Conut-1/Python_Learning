def solve(stack_size, start_idx):
    if stack_size == M:
        print(*stack)
        return
    for i in range(start_idx, N):
        stack.append(nums[i])
        solve(stack_size + 1, i + 1)
        stack.pop()
    return


N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
stack = []
solve(0, 0)
