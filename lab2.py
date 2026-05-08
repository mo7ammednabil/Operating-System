# First Come First Serve
n = int(input("How many jobs: "))
burst = []
waiting = [0]
for i in range(n):
    bt = int(input(f"Job {i+1} Burst Time: "))
    burst.append(bt)

for i in range (1,n):
    waiting.append(waiting[i-1] + burst [i-1])

average = sum(waiting) / n
print(f"\nBurust Time {burst}")
print(f"\nWaiting Time {waiting}")
print(f"average waitnig time {average}")