import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

# Binary search range
left = 0
right = 10**9 + 1

while left < right:
    mid = (left + right) // 2
    
    # sellers with Ai <= mid
    sellers = bisect.bisect_right(A, mid)
    
    # buyers with Bi >= mid
    buyers = M - bisect.bisect_left(B, mid)
    
    if sellers >= buyers:
        right = mid
    else:
        left = mid + 1

print(left)
