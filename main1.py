def maxArea(self, height: List[int]) -> int:
    # BRUTE FORCE, time is O(n^2)
    result = 0

    for l in range(len(height)):
        for r in range(l + 1, len(height)):  # r is one pos. ahead of l
            area = (r - l) * min(height[l], height[r])
            result = max(result, area)

    return result