with open('INPUT.TXT', 'r') as f:
    line = f.readline().strip()
    N, M, K = map(int, line.split())
 
total_nuts = N * M
 
if total_nuts >= K:
    result = "YES"
else:
    result = "NO"
     
with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
