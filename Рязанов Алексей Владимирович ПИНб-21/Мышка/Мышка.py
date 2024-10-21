W, H, R = map(int, input().strip().split())
if W >= 2 * R and H >= 2 * R:
    print("YES")
else:
    print("NO")
